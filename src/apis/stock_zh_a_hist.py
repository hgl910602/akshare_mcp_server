import asyncio
from typing import List, Dict, Any
import akshare as ak
import pandas as pd

async def execute(
    symbol: str,
    period: str = "daily",
    start_date: str = "20210301",
    end_date: str = "20210616",
    adjust: str = "",
    timeout: float = None,
) -> List[Dict[str, Any]]:
    """
    异步获取东方财富-沪深京 A 股日频率数据
    
    Args:
        symbol: 股票代码
        period: 周期, 可选 daily, weekly, monthly
        start_date: 开始日期
        end_date: 结束日期
        adjust: 复权类型, qfq: 前复权, hfq: 后复权
        timeout: 超时时间
        
    Returns:
        List[Dict[str, Any]]: 历史行情数据列表
        
    Raises:
        Exception: 当获取数据失败时抛出异常
    """
    try:
        # 调用akshare同步接口，使用await在异步环境中运行
        df = await asyncio.get_event_loop().run_in_executor(
            None,
            lambda: ak.stock_zh_a_hist(
                symbol=symbol,
                period=period,
                start_date=start_date,
                end_date=end_date,
                adjust=adjust,
                timeout=timeout,
            )
        )
        
        # 将DataFrame转换为List[Dict]格式
        if not df.empty:
            # 确保日期列是字符串类型
            df["日期"] = df["日期"].astype(str)
            return df.to_dict("records")
        return []
    except Exception as e:
        raise Exception(f"Failed to fetch stock data: {e}")


def test():
    """
    同步测试方法，用于验证execute函数
    
    Raises:
        Exception: 当execute调用失败时抛出异常
    """
    try:
        # 使用示例参数调用execute
        result = asyncio.run(
            execute(
                symbol="000001",
                period="daily",
                start_date="20230301",
                end_date="20230528",
                adjust="hfq",
            )
        )
        print(f"Test executed successfully. Got {len(result)} records.")
        return result
    except Exception as e:
        print(f"Test failed: {e}")
        raise


if __name__ == "__main__":
    # 演示如何调用异步execute函数
    async def main():
        try:
            data = await execute(
                symbol="000001",
                period="daily",
                start_date="20230301",
                end_date="20230528",
                adjust="hfq",
            )
            print(f"Fetched {len(data)} records")
            if data:
                print("Sample record:", data[0])
        except Exception as e:
            print(f"Error in main: {e}")

    asyncio.run(main())