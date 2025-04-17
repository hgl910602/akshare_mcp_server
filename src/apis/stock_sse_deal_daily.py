import asyncio
from typing import Any, Dict, List
import akshare as ak
import pandas as pd


async def fetch_stock_sse_deal_daily(date: str) -> pd.DataFrame:
    """
    异步获取上海证券交易所每日股票成交概况数据
    
    Args:
        date: 日期, 格式为YYYYMMDD, 例如"20250221"
        
    Returns:
        pd.DataFrame: 包含每日股票成交概况数据的DataFrame
        
    Raises:
        ValueError: 当日期格式不正确或数据获取失败时抛出
    """
    try:
        # 使用akshare同步接口获取数据
        loop = asyncio.get_event_loop()
        df = await loop.run_in_executor(
            None, 
            lambda: ak.stock_sse_deal_daily(date=date)
        )
        
        # 检查返回结果是否有效
        if df.empty:
            raise ValueError("No data returned for the given date")
            
        return df
        
    except Exception as e:
        raise ValueError(f"Failed to fetch stock sse deal daily data: {str(e)}")


async def main():
    """
    测试函数，演示如何使用fetch_stock_sse_deal_daily
    """
    try:
        # 示例调用
        date = "20250221"  # 替换为实际需要的日期
        df = await fetch_stock_sse_deal_daily(date=date)
        print(f"Successfully fetched data for date: {date}")
        print(df)
        
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")


if __name__ == "__main__":
    asyncio.run(main())