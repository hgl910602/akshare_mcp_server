import sqlite3
import os
from typing import List, Dict

class StockInterfaceRepository:
    def __init__(self):
        """初始化仓库，使用固定路径的数据库文件"""
        current_dir = os.path.dirname(os.path.abspath(__file__))
        self.db_path = os.path.join(current_dir, "stock_meta.db")
        
    def create_table(self):
        """创建数据表"""
        conn = sqlite3.connect(self.db_path)
        try:
            cursor = conn.cursor()
            cursor.execute('''
            CREATE TABLE IF NOT EXISTS stock_interfaces (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                category TEXT,
                sub_category TEXT,
                third_category TEXT,
                interface_name TEXT,
                target_url TEXT,
                description TEXT,
                limit_info TEXT,
                input_params TEXT,
                output_params TEXT,
                example TEXT,
                data_example TEXT,
                update_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
            ''')
            conn.commit()
        finally:
            conn.close()
            
    def save_interfaces(self, data: List[Dict]):
        """保存接口数据"""
        conn = sqlite3.connect(self.db_path)
        try:
            cursor = conn.cursor()
            # 清空旧数据
            cursor.execute("DELETE FROM stock_interfaces")
            
            # 插入新数据
            for item in data:
                cursor.execute('''
                INSERT INTO stock_interfaces (
                    category, sub_category, third_category, interface_name,
                    target_url, description, limit_info, input_params,
                    output_params, example, data_example
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                ''', (
                    item.get('功能分类', ''),
                    item.get('子分类', ''),
                    item.get('三级分类', ''),
                    item.get('接口', ''),
                    item.get('目标地址', ''),
                    item.get('描述', ''),
                    item.get('使用限制', ''),
                    item.get('输入参数', ''),
                    item.get('输出参数', ''),
                    item.get('接口示例', ''),
                    item.get('数据示例', '')
                ))
            conn.commit()
        finally:
            conn.close()
    
    def get_all_interfaces(self) -> List[Dict]:
        """获取所有接口数据"""
        conn = sqlite3.connect(self.db_path)
        try:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM stock_interfaces")
            columns = [column[0] for column in cursor.description]
            return [dict(zip(columns, row)) for row in cursor.fetchall()]
        finally:
            conn.close()

    def get_table_columns(self) -> List[str]:
        """获取表列名"""
        conn = sqlite3.connect(self.db_path)
        try:
            cursor = conn.cursor()
            cursor.execute("PRAGMA table_info(stock_interfaces)")
            return [column[1] for column in cursor.fetchall()]
        finally:
            conn.close()