import asyncio
from typing import List, Dict, Any
import akshare as ak
import pandas as pd

async def execute(symbol: str, period: str) -> List[Dict[str, Any]]:
    """
    异步获取东方财富-沪深板块-概念板块-分时历史行情数据
    
    Args:
        symbol: 概念板块名称，如"长寿药"
        period: 分时周期，可选 {"1", "5", "15", "30", "60"}
    
    Returns:
        返回包含行情数据的字典列表
    
    Raises:
        Exception: 当获取数据失败时抛出异常
    """
    try:
        # 调用akshare的同步接口，使用await在异步环境中执行
        df = await asyncio.get_event_loop().run_in_executor(
            None, 
            ak.stock_board_concept_hist_min_em, 
            symbol, 
            period
        )
        
        # 将DataFrame转换为字典列表
        if not df.empty:
            return df.to_dict("records")
        return []
    except Exception as e:
        raise Exception(f"Failed to fetch concept board minute data: {str(e)}")

def test():
    """
    同步测试方法，用于自动化测试
    
    Raises:
        直接抛出execute方法可能产生的异常
    """
    try:
        # 使用asyncio.run运行异步方法
        result = asyncio.run(execute(symbol="长寿药", period="5"))
        print(f"Test executed successfully, got {len(result)} records")
        return result
    except Exception as e:
        print(f"Test failed: {str(e)}")
        raise

if __name__ == "__main__":
    # 演示如何调用异步函数
    async def main():
        try:
            data = await execute(symbol="长寿药", period="5")
            print(f"Got {len(data)} records")
            if data:
                print("Sample record:")
                print(data[0])
        except Exception as e:
            print(f"Error: {str(e)}")
    
    asyncio.run(main())