import asyncio
from typing import List, Dict, Any
import akshare as ak
import pandas as pd

async def execute(symbol: str) -> List[Dict[str, Any]]:
    """
    异步获取东方财富-行情报价数据
    
    Args:
        symbol: 股票代码, 如 "000001"
        
    Returns:
        返回包含行情数据的字典列表
        
    Raises:
        Exception: 当获取数据失败时抛出异常
    """
    try:
        # 调用akshare接口获取数据
        df = ak.stock_bid_ask_em(symbol=symbol)
        
        # 将DataFrame转换为字典列表
        if not df.empty:
            return df.to_dict("records")
        return []
    except Exception as e:
        raise Exception(f"获取行情数据失败: {e}")

def test():
    """
    同步测试方法, 用于自动化测试
    
    Raises:
        异常上抛, 不捕获
    """
    # 使用示例参数调用
    result = asyncio.run(execute(symbol="000001"))
    print(result)

if __name__ == "__main__":
    # 演示如何调用异步函数
    async def main():
        try:
            data = await execute(symbol="000001")
            print(data)
        except Exception as e:
            print(f"Error: {e}")
    
    asyncio.run(main())