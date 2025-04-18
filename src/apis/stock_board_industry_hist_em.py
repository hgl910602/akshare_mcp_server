import asyncio
from typing import List, Dict, Any
import akshare as ak
import pandas as pd

async def execute(
    symbol: str,
    start_date: str,
    end_date: str,
    period: str = "日k",
    adjust: str = "",
) -> List[Dict[str, Any]]:
    """
    异步获取东方财富-沪深板块-行业板块历史行情数据
    
    Args:
        symbol: 行业板块名称，可通过 ak.stock_board_industry_name_em() 获取
        start_date: 开始日期，格式为YYYYMMDD
        end_date: 结束日期，格式为YYYYMMDD
        period: 周期，可选 "日k", "周k", "月k"
        adjust: 复权类型，可选 "", "qfq", "hfq"
        
    Returns:
        行业板块历史行情数据列表，每个元素为包含字段的字典
        
    Raises:
        Exception: 当获取数据失败时抛出异常
    """
    try:
        # 调用akshare同步接口获取数据
        df = ak.stock_board_industry_hist_em(
            symbol=symbol,
            start_date=start_date,
            end_date=end_date,
            period=period,
            adjust=adjust,
        )
        
        # 将DataFrame转换为List[Dict]格式
        if not df.empty:
            # 处理可能的NaN值
            df = df.fillna(0)
            # 转换日期列为字符串格式
            df["日期"] = df["日期"].astype(str)
            return df.to_dict("records")
        return []
    except Exception as e:
        raise Exception(f"获取行业板块历史数据失败: {e}")

def test() -> List[Dict[str, Any]]:
    """
    同步测试方法，用于自动化测试
    
    Returns:
        行业板块历史行情数据列表
        
    Raises:
        Exception: 当execute方法执行失败时抛出异常
    """
    try:
        # 使用示例参数调用execute方法
        return asyncio.run(
            execute(
                symbol="小金属",
                start_date="20211201",
                end_date="20220401",
                period="日k",
                adjust="",
            )
        )
    except Exception as e:
        raise Exception(f"测试执行失败: {e}")

if __name__ == "__main__":
    # 演示如何调用异步函数并打印结果
    async def main():
        try:
            data = await execute(
                symbol="小金属",
                start_date="20211201",
                end_date="20220401",
                period="日k",
                adjust="",
            )
            print(f"获取到 {len(data)} 条数据")
            if data:
                print("示例数据:")
                print(data[0])
        except Exception as e:
            print(f"执行出错: {e}")

    asyncio.run(main())