import asyncio
from typing import Any, Dict, List
import akshare as ak
import pandas as pd


async def stock_sse_summary() -> pd.DataFrame:
    """
    上海证券交易所-股票数据总貌
    :return: 上海证券交易所股票数据总貌
    :rtype: pandas.DataFrame
    """
    try:
        # 使用akshare同步接口获取数据
        loop = asyncio.get_event_loop()
        result = await loop.run_in_executor(None, ak.stock_sse_summary)
        return result
    except Exception as e:
        raise ValueError(f"获取上海证券交易所股票数据总貌失败: {e}")


async def execute() -> pd.DataFrame:
    """
    执行函数，获取上海证券交易所股票数据总貌
    :return: 上海证券交易所股票数据总貌
    :rtype: pandas.DataFrame
    """
    return await stock_sse_summary()


if __name__ == "__main__":
    async def main():
        try:
            df = await execute()
            print(df)
        except Exception as e:
            print(f"发生错误: {e}")

    asyncio.run(main())