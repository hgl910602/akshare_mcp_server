import asyncio
from typing import List, Dict, Any
import akshare as ak
import pandas as pd

async def execute(symbol: str, date: str) -> List[Dict[str, Any]]:
    """
    异步获取东方财富网个股十大流通股东数据
    
    Args:
        symbol: 带市场标识的股票代码, 如 "sh688686"
        date: 财报发布季度最后日, 如 "20240930"
    
    Returns:
        十大流通股东数据列表, 每个股东信息以字典形式存储
    
    Raises:
        Exception: 当akshare接口调用失败时抛出异常
    """
    try:
        # 调用akshare同步接口, 使用await asyncio.to_thread在异步环境中运行同步代码
        df = await asyncio.to_thread(ak.stock_gdfx_free_top_10_em, symbol=symbol, date=date)
        
        # 将DataFrame转换为List[Dict]格式
        result = df.to_dict(orient="records")
        return result
    except Exception as e:
        raise Exception(f"Failed to fetch stock top 10 free shareholders: {str(e)}")

def test():
    """
    同步测试方法, 用于自动化测试
    
    Raises:
        Exception: 当execute方法调用失败时抛出异常
    """
    try:
        # 使用asyncio.run运行异步方法
        result = asyncio.run(execute(symbol="sh688686", date="20240930"))
        print(result)
    except Exception as e:
        raise Exception(f"Test failed: {str(e)}")

if __name__ == "__main__":
    # 演示如何调用异步函数
    async def main():
        try:
            data = await execute(symbol="sh688686", date="20240930")
            print("十大流通股东数据:")
            for item in data:
                print(item)
        except Exception as e:
            print(f"Error: {str(e)}")
    
    asyncio.run(main())