import asyncio
from typing import Any, Dict, List, Optional
import akshare as ak
import pandas as pd


async def fetch_stock_individual_basic_info_xq(
    symbol: str, 
    token: Optional[str] = None, 
    timeout: Optional[float] = None
) -> pd.DataFrame:
    """
    异步获取雪球财经个股公司概况信息
    
    Args:
        symbol: 股票代码，例如 "SH601127"
        token: 可选token
        timeout: 超时时间(秒)
        
    Returns:
        pandas.DataFrame: 包含个股基本信息的DataFrame
        
    Raises:
        Exception: 当接口调用失败时抛出异常
    """
    try:
        # 使用akshare同步接口，通过run_in_executor转为异步
        loop = asyncio.get_running_loop()
        result = await loop.run_in_executor(
            None, 
            lambda: ak.stock_individual_basic_info_xq(
                symbol=symbol,
                token=token,
                timeout=timeout
            )
        )
        return result
    except Exception as e:
        raise Exception(f"获取股票基本信息失败: {e}")


async def main():
    """
    测试函数
    """
    try:
        # 示例调用
        df = await fetch_stock_individual_basic_info_xq(symbol="SH601127")
        print("股票基本信息获取成功:")
        print(df.head())
    except Exception as e:
        print(f"测试失败: {e}")


if __name__ == "__main__":
    asyncio.run(main())