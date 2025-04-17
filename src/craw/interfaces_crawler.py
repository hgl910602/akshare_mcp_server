import re
from tracemalloc import start
from numpy.strings import startswith
import requests  # 添加requests导入
from typing import List, Dict
from bs4 import BeautifulSoup
import markdown2
from pathlib import Path
import pandas as pd  # 添加pandas导入
import sqlite3
import schedule
import time
from persistence.stock_interface_repository import StockInterfaceRepository

class NewDataFetcher:
    def __init__(self):
        # 移除本地Milvus Lite启动代码
        self.milvus_host = "47.97.117.10"
        self.milvus_port = 19530
        self.interface_repo = StockInterfaceRepository()

    def __del__(self):
        """不再需要停止本地服务"""
        pass

    def fetch_markdown(self, url: str) -> str:
        """获取Markdown文档内容"""
        response = requests.get(url)
        response.raise_for_status()
        return response.text
        
    def parse_markdown(self, md_content: str) -> List[Dict]:
        """解析Markdown文档"""
        html = markdown2.Markdown(extras={'code-friendly': None}).convert(md_content)
        soup = BeautifulSoup(html, 'html.parser')
        structured_data = []
        print("开始解析Markdown文档...")
        
        # 获取所有标题节点
        headers = soup.find_all(['h3', 'h4', 'h5'])
        print(f"总标题节点数: {len(headers)}")  # 添加总节点数日志
        current_h3 = ""
        current_h4 = ""
        current_h5 = ""
        
        # 使用for循环替代while循环
        for i in range(len(headers)):
            header = headers[i]
            # print(f"正在处理节点 {i+1}/{len(headers)}: {header.name} - {header.get_text().strip()}")  # 添加节点处理日志
            
            # 更新当前分类变量
            if header.name == 'h3':
                current_h3 = header.get_text().strip()
                current_h4 = ""
                current_h5 = ""
                # print(f"处理h3: {current_h3}")
                
                # 检查是否有直接下级h4
                if i+1 < len(headers) and headers[i+1].name == 'h4':
                    # print(f"跳过h3直接处理h4: {current_h3}")  # 添加跳过日志
                    continue
                    
            elif header.name == 'h4':
                current_h4 = header.get_text().strip()
                current_h5 = ""
                # print(f"  处理h4: {current_h4}")
                
                # 检查是否有直接下级h5
                if i+1 < len(headers) and headers[i+1].name == 'h5':
                    # print(f"  跳过h4直接处理h5: {current_h4}")  # 添加跳过日志
                    continue
                    
            elif header.name == 'h5':
                current_h5 = header.get_text().strip()
                # print(f"    处理h5: {current_h5}")

            if current_h3 == "手续费":
                # print(f"跳过手续费分类: {current_h3}")  # 添加手续费跳过日志
                continue

            # 获取当前节点后的内容
            content_nodes = []
            next_node = header.next_sibling
            while next_node and (i+1 >= len(headers) or next_node != headers[i+1]):
                content_nodes.append(str(next_node))
                next_node = next_node.next_sibling
            
            # 解析原始数据中的各个字段
            record = {
                '功能分类': current_h3,  # 修正变量名
                '子分类': current_h4,    # 修正变量名
                '三级分类': current_h5,   # 修正变量名
                '接口': '',
                '目标地址': '',
                '描述': '',
                '使用限制': '',
                '输入参数': '',
                '输出参数': '',
                '接口示例': '',
                '数据示例': ''
            }
            
            # 获取当前节点到下一个标题节点之间的所有内容
            content_nodes = []
            next_node = header.next_sibling  # 修正：将tag改为header
            while next_node and (i+1 >= len(headers) or next_node != headers[i+1]):
                content_nodes.append(next_node)
                next_node = next_node.next_sibling
            
            # 解析内容节点
            current_field = None
            field_content = []
            for node in content_nodes:
                if node.name == 'p':
                    text = node.get_text().strip()
                    if text.startswith('接口') and 'stock_zh_a_daily' in text:  # 修改这里
                        continue
                    field_match = re.match(r'^(接口示例|接口|数据示例|目标地址|描述|限量|输入参数|输出参数)[:：]?\s*(.*)', text)
                    if field_match:
                        if current_field:
                            record[current_field] = '\n'.join(field_content).strip()
                        current_field = field_match.group(1).strip()
                        field_content = [field_match.group(2).strip()]
                    else:
                        field_content.append(text)
                elif node.name in ['ul', 'ol', 'pre', 'table']:
                    field_content.append(node.get_text().strip())
            
            if current_field:
                record[current_field] = '\n'.join(field_content).strip()

            # 在记录添加前打印日志
            # print(f"生成记录 #{len(structured_data)+1}: {current_h3} - {current_h4} - {current_h5}")
            structured_data.append(record)
        
        print(f"解析完成，共找到{len(structured_data)}条记录")  # 修改最终日志
        return structured_data

    def fetch_stock_markdown(self) -> str:
        """获取股票数据的Markdown文档内容"""
        url = "https://akshare.akfamily.xyz/_sources/data/stock/stock.md.txt"
        return self.fetch_markdown(url)

    def save_to_sqlite(self, data: List[Dict]):
        """将数据保存到SQLite数据库"""
        self.interface_repo.create_table()
        self.interface_repo.save_interfaces(data)
        print(f"数据已保存到SQLite数据库: {self.interface_repo.db_path}")

    def scheduled_update(self, interval_minutes: int = 60):
        """定时更新数据，改进版本"""
        last_run_time = None
        
        def update_job():
            nonlocal last_run_time
            try:
                current_time = time.strftime('%Y-%m-%d %H:%M:%S')
                print(f"\n=== 开始定时更新数据，当前时间: {current_time} ===")
                print(f"上次执行时间: {last_run_time or '首次运行'}")
                
                md_content = self.fetch_stock_markdown()
                data = self.parse_markdown(md_content)
                self.save_to_sqlite(data)
                # self.save_to_milvus(data)
                
                last_run_time = current_time
                print(f"=== 数据更新完成，时间: {current_time} ===\n")
            except Exception as e:
                print(f"定时任务执行出错: {str(e)}")
                import traceback
                traceback.print_exc()
        
        # 立即执行一次
        update_job()
        
        # 设置定时任务
        schedule.every(interval_minutes).minutes.do(update_job)
        print(f"定时任务已启动，每隔 {interval_minutes} 分钟执行一次")
        
        # 改进的主循环
        while True:
            try:
                schedule.run_pending()
                time.sleep(1)  # 降低CPU占用
            except KeyboardInterrupt:
                print("\n定时任务已停止")
                break
            except Exception as e:
                print(f"定时任务循环出错: {str(e)}")
                time.sleep(5)  # 出错后等待5秒再继续

if __name__ == "__main__":
    fetcher = NewDataFetcher()
    
    # 使用定时更新
    fetcher.scheduled_update()
    
    # 或者手动执行一次
    # md_content = fetcher.fetch_stock_markdown()
    # data = fetcher.parse_markdown(md_content)
    # fetcher.save_to_sqlite(data)
    # output_path = str(Path(__file__).parent.absolute() / "new_stock_data.xlsx")
    # df = pd.DataFrame(data)
    # df.to_excel(output_path, index=False)
    # print(f"数据已保存到Excel文件: {output_path}")