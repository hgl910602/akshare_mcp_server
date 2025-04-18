import asyncio
from typing import List, Dict, Any
import akshare as ak
import pandas as pd

async def execute(
    symbol: str,
    start_date: str = "1979-09-01 09:32:00",
    end_date: str = "2222-01-01 09:32:00",
    period: str = "5",
    adjust: str = "",
) -> List[Dict[str, Any]]:
    """
    获取东方财富网-沪深京A股每日分时行情数据(异步版本)
    
    Args:
        symbol: 股票代码
        start_date: 开始日期时间
        end_date: 结束日期时间
        period: 分时周期，可选 {'1', '5', '15', '30', '60'}
        adjust: 复权类型，可选 {'', 'qfq', 'hfq'}
    
    Returns:
        List[Dict[str, Any]]: 分时行情数据列表
    
    Raises:
        Exception: 当获取数据失败时抛出异常
    """
    try:
        # 由于akshare没有原生异步接口，这里使用run_in_executor来异步执行
        loop = asyncio.get_running_loop()
        df = await loop.run_in_executor(
            None,
            lambda: ak.stock_zh_a_hist_min_em(
                symbol=symbol,
                start_date=start_date,
                end_date=end_date,
                period=period,
                adjust=adjust,
            )
        )
        
        # 将DataFrame转换为List[Dict]格式
        if not df.empty:
            return df.to_dict("records")
        return []
    except Exception as e:
        raise Exception(f"获取分时行情数据失败: {e}")

def test():
    """
    同步测试方法，用于自动化测试
    
    Raises:
        Exception: 当execute方法执行失败时抛出异常
    """
    try:
        # 使用示例参数调用execute方法
        result = asyncio.run(
            execute(
                symbol="000001",
                start_date="2024-03-20 09:30:00",
                end_date="2024-03-20 15:00:00",
                period="5",
                adjust="hfq",
            )
        )
        print(result)
    except Exception as e:
        raise Exception(f"测试执行失败: {e}")

if __name__ == "__main__":
    # 演示如何调用异步函数并打印结果
    async def main():
        try:
            data = await execute(
                symbol="000300",
                start_date="2024-03-20 09:30:00",
                end_date="2024-03-20 15:00:00",
                period="5",
                adjust="",
            )
            print(data)
        except Exception as e:
            print(f"Error: {e}")

    asyncio.run(main())