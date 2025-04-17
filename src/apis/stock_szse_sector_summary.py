import asyncio
from typing import Any, Dict, List
import akshare as ak
import pandas as pd

async def fetch_stock_szse_sector_summary(symbol: str = "当月", date: str = "202501") -> pd.DataFrame:
    """
    异步获取深圳证券交易所-统计资料-股票行业成交数据
    
    Args:
        symbol: 统计周期, "当月" 或 "当年"
        date: 年月格式, 如 "202501"
    
    Returns:
        pandas.DataFrame: 包含股票行业成交数据的DataFrame
    
    Raises:
        Exception: 当获取数据失败时抛出异常
    """
    try:
        # 使用akshare同步接口获取数据
        loop = asyncio.get_event_loop()
        df = await loop.run_in_executor(
            None, 
            lambda: ak.stock_szse_sector_summary(symbol=symbol, date=date)
        )
        return df
    except Exception as e:
        raise Exception(f"获取深圳证券交易所股票行业成交数据失败: {e}")

async def main():
    """测试函数"""
    try:
        # 示例调用
        df = await fetch_stock_szse_sector_summary(symbol="当年", date="202501")
        print("深圳证券交易所股票行业成交数据:")
        print(df)
    except Exception as e:
        print(f"发生错误: {e}")

if __name__ == "__main__":
    asyncio.run(main())