import asyncio
from typing import List, Dict, Any
import akshare as ak
import pandas as pd

async def execute() -> List[Dict[str, Any]]:
    """
    异步获取A+H股实时行情数据
    
    Returns:
        List[Dict[str, Any]]: A+H股实时行情数据列表，每个元素为一个字典表示一条股票数据
        
    Raises:
        Exception: 当获取数据失败时抛出异常
    """
    try:
        # 调用akshare同步接口获取数据
        df = ak.stock_zh_ah_spot()
        
        # 将DataFrame转换为List[Dict]格式
        if not df.empty:
            return df.to_dict("records")
        return []
    except Exception as e:
        raise Exception(f"Failed to fetch A+H stock data: {str(e)}")

def test() -> List[Dict[str, Any]]:
    """
    同步测试方法，用于自动化测试
    
    Returns:
        List[Dict[str, Any]]: A+H股实时行情数据列表
        
    Raises:
        Exception: 当execute方法执行失败时抛出异常
    """
    return asyncio.run(execute())

if __name__ == "__main__":
    # 演示如何调用异步函数
    async def main():
        try:
            data = await execute()
            print(f"Got {len(data)} A+H stock records")
            if data:
                print("Sample record:", data[0])
        except Exception as e:
            print(f"Error: {e}")
    
    asyncio.run(main())