import asyncio
from typing import Any, Dict, List
import akshare as ak
import pandas as pd

async def execute(date: str = "20231231") -> List[Dict[str, Any]]:
    """
    异步获取东方财富-数据中心-年报季报-分红配送数据
    
    Args:
        date: 日期, 格式为"YYYY0630"或"YYYY1231", 默认为"20231231"
    
    Returns:
        分红配送数据列表, 每个元素为一个字典, 包含股票的分红配送信息
        
    Raises:
        Exception: 当获取数据失败时抛出异常
    """
    try:
        # 调用akshare同步接口获取数据
        df = ak.stock_fhps_em(date=date)
        
        # 将DataFrame转换为List[Dict]格式
        result = df.to_dict("records")
        
        return result
    except Exception as e:
        raise Exception(f"Failed to fetch stock fhps data: {str(e)}")

def test():
    """
    同步测试方法, 用于自动化测试
    
    Returns:
        分红配送数据列表
        
    Raises:
        Exception: 当execute方法执行失败时抛出异常
    """
    try:
        # 使用asyncio.run运行异步方法
        result = asyncio.run(execute(date="20231231"))
        return result
    except Exception as e:
        raise e

if __name__ == "__main__":
    # 演示如何调用异步函数并打印结果
    async def main():
        try:
            data = await execute(date="20231231")
            print(data[:2])  # 打印前两条数据作为示例
        except Exception as e:
            print(f"Error occurred: {e}")
    
    asyncio.run(main())