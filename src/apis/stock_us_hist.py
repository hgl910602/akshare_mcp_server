import asyncio
from typing import List, Dict, Any
import akshare as ak
import pandas as pd

async def execute(
    symbol: str,
    period: str = "daily",
    start_date: str = "20210101",
    end_date: str = "20210601",
    adjust: str = "",
) -> List[Dict[str, Any]]:
    """
    异步获取美股历史行情数据
    
    Args:
        symbol: 美股代码
        period: 周期, 可选 daily, weekly, monthly
        start_date: 开始日期, 格式 YYYYMMDD
        end_date: 结束日期, 格式 YYYYMMDD
        adjust: 复权类型, ""(不复权), "qfq"(前复权), "hfq"(后复权)
    
    Returns:
        美股历史行情数据列表, 每个元素为包含字段的字典
    
    Raises:
        Exception: 当获取数据失败时抛出异常
    """
    try:
        # 调用akshare同步接口获取数据
        df = ak.stock_us_hist(
            symbol=symbol,
            period=period,
            start_date=start_date,
            end_date=end_date,
            adjust=adjust,
        )
        
        # 将DataFrame转换为List[Dict]格式
        if not df.empty:
            # 处理可能的NaN值
            df = df.fillna(0)
            return df.to_dict("records")
        return []
    except Exception as e:
        raise Exception(f"Failed to fetch US stock history data: {str(e)}")

def test():
    """
    同步测试方法, 用于自动化测试
    
    Raises:
        Exception: 当execute方法执行失败时抛出异常
    """
    try:
        # 使用示例参数调用execute方法
        result = asyncio.run(
            execute(
                symbol="106.TTE",
                period="daily",
                start_date="20200101",
                end_date="20240214",
                adjust="qfq",
            )
        )
        print("Test executed successfully")
        return result
    except Exception as e:
        raise Exception(f"Test failed: {str(e)}")

if __name__ == "__main__":
    # 演示如何调用异步函数
    async def main():
        try:
            data = await execute(
                symbol="106.TTE",
                period="daily",
                start_date="20200101",
                end_date="20240214",
                adjust="qfq",
            )
            print("Fetched data:")
            for item in data[:5]:  # 打印前5条记录
                print(item)
        except Exception as e:
            print(f"Error: {str(e)}")
    
    asyncio.run(main())