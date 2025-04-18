import asyncio
from typing import List, Dict, Any
import akshare as ak
import pandas as pd

async def execute() -> List[Dict[str, Any]]:
    """
    异步获取B股实时行情数据
    
    Returns:
        List[Dict[str, Any]]: B股实时行情数据列表，每个元素为一个字典代表一只股票的数据
        
    Raises:
        Exception: 当获取数据失败时抛出异常
    """
    try:
        # 调用akshare同步接口，使用run_in_executor避免阻塞事件循环
        loop = asyncio.get_running_loop()
        df = await loop.run_in_executor(None, ak.stock_zh_b_spot)
        
        # 将DataFrame转换为List[Dict]格式
        result = df.to_dict(orient='records')
        return result
    except Exception as e:
        raise Exception(f"Failed to fetch B stock spot data: {str(e)}")

def test() -> List[Dict[str, Any]]:
    """
    同步测试方法，用于测试execute函数
    
    Returns:
        List[Dict[str, Any]]: B股实时行情数据
        
    Raises:
        Exception: 当execute执行失败时抛出异常
    """
    try:
        return asyncio.run(execute())
    except Exception as e:
        raise Exception(f"Test failed: {str(e)}")

if __name__ == '__main__':
    # 演示如何异步调用该函数
    async def main():
        try:
            data = await execute()
            print(f"Successfully fetched {len(data)} B stocks")
            if data:
                print("Sample data:")
                print(data[0])  # 打印第一条数据作为示例
        except Exception as e:
            print(f"Error: {e}")
    
    asyncio.run(main())