import asyncio
from typing import Any, Dict, List
import akshare as ak
import pandas as pd


async def fetch_stock_sse_summary() -> pd.DataFrame:
    """
    异步获取上海证券交易所-股票数据总貌
    
    Returns:
        pd.DataFrame: 包含股票市场总貌数据的DataFrame
    """
    try:
        # 使用akshare同步接口，通过run_in_executor转换为异步
        loop = asyncio.get_event_loop()
        result = await loop.run_in_executor(None, ak.stock_sse_summary)
        return result
    except Exception as e:
        raise Exception(f"获取上海证券交易所股票数据总貌失败: {e}")


async def main() -> None:
    """
    主函数，用于测试fetch_stock_sse_summary
    """
    try:
        df = await fetch_stock_sse_summary()
        print("上海证券交易所股票数据总貌:")
        print(df)
    except Exception as e:
        print(f"测试失败: {e}")


if __name__ == "__main__":
    asyncio.run(main())