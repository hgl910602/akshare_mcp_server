import asyncio
from typing import List, Dict, Any
import akshare as ak
import pandas as pd

async def execute(
    symbol: str = "北向持股", 
    start_date: str = "20210601", 
    end_date: str = "20210608"
) -> List[Dict[str, Any]]:
    """
    获取东方财富网-数据中心-沪深港通-沪深港通持股-每日个股统计数据
    
    Args:
        symbol: 持股类型, choice of {"北向持股", "沪股通持股", "深股通持股", "南向持股"}
        start_date: 开始日期, 格式为YYYYMMDD
        end_date: 结束日期, 格式为YYYYMMDD
    
    Returns:
        返回列表字典形式的数据
        
    Raises:
        Exception: 当akshare接口调用失败时抛出异常
    """
    try:
        # 调用akshare接口获取数据
        df = ak.stock_hsgt_stock_statistics_em(
            symbol=symbol,
            start_date=start_date,
            end_date=end_date
        )
        
        # 将DataFrame转换为List[Dict]格式
        result = df.to_dict(orient="records")
        return result
    except Exception as e:
        raise Exception(f"获取沪深港通持股数据失败: {str(e)}")


def test():
    """
    同步测试方法，用于自动化测试
    
    Raises:
        当execute方法调用失败时直接抛出异常
    """
    try:
        # 使用示例参数调用execute方法
        result = asyncio.run(execute(
            symbol="北向持股",
            start_date="20211027",
            end_date="20211027"
        ))
        print("测试成功，获取数据条数:", len(result))
        return result
    except Exception as e:
        print("测试失败:", str(e))
        raise


if __name__ == "__main__":
    # 演示如何调用该函数
    async def main():
        try:
            data = await execute(
                symbol="北向持股",
                start_date="20211027",
                end_date="20211027"
            )
            print("获取数据成功，前5条记录:")
            for item in data[:5]:
                print(item)
        except Exception as e:
            print("调用失败:", str(e))
    
    asyncio.run(main())