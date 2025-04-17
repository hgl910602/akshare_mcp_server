import asyncio
from typing import Any, Dict, List, Optional

import akshare as ak
import pandas as pd


async def fetch_stock_individual_info_em(
    symbol: str, timeout: Optional[float] = None
) -> pd.DataFrame:
    """
    东方财富-个股-股票信息

    Parameters
    ----------
    symbol : str
        股票代码, 如: "603777"
    timeout : Optional[float], optional
        超时时间, by default None

    Returns
    -------
    pd.DataFrame
        个股信息

    Raises
    ------
    ValueError
        当股票代码无效或请求失败时抛出
    """
    try:
        # 使用akshare同步接口，通过run_in_executor转换为异步
        loop = asyncio.get_event_loop()
        result = await loop.run_in_executor(
            None,
            lambda: ak.stock_individual_info_em(symbol=symbol, timeout=timeout),
        )
        return result
    except Exception as e:
        raise ValueError(f"获取股票信息失败: {e}")


async def main():
    try:
        # 示例调用
        symbol = "000001"  # 平安银行
        df = await fetch_stock_individual_info_em(symbol=symbol)
        print(df)
    except ValueError as e:
        print(e)


if __name__ == "__main__":
    asyncio.run(main())