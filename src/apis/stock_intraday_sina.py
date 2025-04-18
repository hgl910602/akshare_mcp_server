import asyncio
from typing import List, Dict, Any
import akshare as ak
import pandas as pd

async def execute(symbol: str, date: str) -> List[Dict[str, Any]]:
    """
    异步获取新浪财经日内分时数据
    
    Args:
        symbol: 带市场标识的股票代码, 如 "sz000001"
        date: 交易日, 格式如 "20240321"
    
    Returns:
        返回处理后的分时数据列表, 每个元素是一个字典
        
    Raises:
        Exception: 当akshare接口调用失败或数据处理异常时抛出
    """
    try:
        # 调用akshare同步接口获取数据
        df = ak.stock_intraday_sina(symbol=symbol, date=date)
        
        # 处理数据为List[Dict]格式
        result = []
        for _, row in df.iterrows():
            item = {
                "symbol": row["symbol"],
                "name": row["name"],
                "ticktime": row["ticktime"],
                "price": row["price"],
                "volume": row["volume"],
                "prev_price": row["prev_price"],
                "kind": row["kind"]
            }
            result.append(item)
            
        return result
    except Exception as e:
        raise Exception(f"Failed to fetch intraday data: {str(e)}")

def test():
    """
    同步测试方法, 用于自动化测试
    
    Raises:
        原样抛出execute方法中的异常
    """
    try:
        # 使用示例参数调用
        result = asyncio.run(execute(symbol="sz000001", date="20240321"))
        return result
    except Exception as e:
        raise e

if __name__ == "__main__":
    # 演示如何调用异步函数
    async def main():
        try:
            data = await execute(symbol="sz000001", date="20240321")
            print(data[:5])  # 打印前5条数据
        except Exception as e:
            print(f"Error: {e}")
    
    asyncio.run(main())