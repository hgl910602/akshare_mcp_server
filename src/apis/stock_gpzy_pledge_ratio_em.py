import asyncio
from typing import List, Dict, Any
import akshare as ak
import pandas as pd

async def execute(date: str) -> List[Dict[str, Any]]:
    """
    异步获取东方财富网-数据中心-特色数据-股权质押-上市公司质押比例数据
    
    Args:
        date: 查询日期，格式为"YYYYMMDD"
        
    Returns:
        返回处理后的字典列表，每个字典代表一行数据
        
    Raises:
        Exception: 当akshare接口调用失败或数据处理出错时抛出
    """
    try:
        # 调用akshare接口获取数据
        df = await asyncio.to_thread(ak.stock_gpzy_pledge_ratio_em, date=date)
        
        # 处理数据为字典列表
        if not df.empty:
            # 处理可能的NaN值
            df = df.fillna(0)
            # 转换数据类型
            df = df.astype({
                '序号': 'int64',
                '质押比例': 'float64',
                '质押股数': 'float64',
                '质押市值': 'float64',
                '质押笔数': 'float64',
                '无限售股质押数': 'float64',
                '限售股质押数': 'float64',
                '近一年涨跌幅': 'float64'
            })
            return df.to_dict('records')
        return []
    except Exception as e:
        raise Exception(f"获取股票质押数据失败: {str(e)}")

def test():
    """
    同步测试方法，用于自动化测试
    
    Returns:
        返回execute方法的执行结果
        
    Raises:
        直接抛出execute方法可能产生的异常
    """
    # 使用示例中的日期参数
    test_date = "20241220"
    return asyncio.run(execute(date=test_date))

if __name__ == '__main__':
    # 演示如何调用异步函数
    async def main():
        try:
            data = await execute(date="20240906")
            print(f"获取到{len(data)}条数据")
            if data:
                print("第一条数据示例:")
                print(data[0])
        except Exception as e:
            print(f"执行出错: {e}")
    
    asyncio.run(main())