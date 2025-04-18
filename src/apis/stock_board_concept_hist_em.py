import asyncio
from typing import List, Dict, Any
import akshare as ak
import pandas as pd

async def execute(
    symbol: str,
    period: str = "daily",
    start_date: str = "20220101",
    end_date: str = "20221128",
    adjust: str = "",
) -> List[Dict[str, Any]]:
    """
    异步获取东方财富-沪深板块-概念板块-历史行情数据
    
    Args:
        symbol: 概念板块名称，如"绿色电力"
        period: 周期，可选 "daily", "weekly", "monthly"
        start_date: 开始日期，格式 "YYYYMMDD"
        end_date: 结束日期，格式 "YYYYMMDD"
        adjust: 复权类型，可选 "", "qfq", "hfq"
        
    Returns:
        返回包含历史行情数据的字典列表
        
    Raises:
        Exception: 当akshare接口调用失败时抛出异常
    """
    try:
        # 调用akshare同步接口，使用await在异步环境中运行
        df = await asyncio.get_event_loop().run_in_executor(
            None,
            ak.stock_board_concept_hist_em,
            symbol,
            period,
            start_date,
            end_date,
            adjust
        )
        
        # 将DataFrame转换为字典列表
        if not df.empty:
            # 处理可能的NaN值
            df = df.fillna(0)
            return df.to_dict("records")
        return []
    except Exception as e:
        raise Exception(f"Failed to fetch concept board history data: {str(e)}")

def test() -> List[Dict[str, Any]]:
    """
    同步测试方法，用于验证execute函数
    
    Returns:
        返回execute函数的结果
        
    Raises:
        直接抛出execute函数可能产生的异常
    """
    # 使用示例参数调用execute方法
    return asyncio.run(
        execute(
            symbol="绿色电力",
            period="daily",
            start_date="20220101",
            end_date="20221128",
            adjust=""
        )
    )

if __name__ == "__main__":
    # 演示如何调用异步execute函数
    async def main():
        try:
            data = await execute(
                symbol="绿色电力",
                period="daily",
                start_date="20220101",
                end_date="20221128"
            )
            print(f"Fetched {len(data)} records")
            if data:
                print("Sample record:", data[0])
        except Exception as e:
            print(f"Error: {e}")
    
    asyncio.run(main())