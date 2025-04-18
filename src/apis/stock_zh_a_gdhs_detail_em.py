import asyncio
from typing import Any, Dict, List
import akshare as ak
import pandas as pd

async def execute(symbol: str) -> List[Dict[str, Any]]:
    """
    异步获取东方财富网股东户数详情数据
    
    Args:
        symbol: 股票代码, 如 "000001"
        
    Returns:
        返回股东户数详情数据的字典列表
        
    Raises:
        Exception: 当数据获取失败时抛出异常
    """
    try:
        # 调用akshare同步接口获取数据
        df = ak.stock_zh_a_gdhs_detail_em(symbol=symbol)
        
        # 将DataFrame转换为字典列表
        result = df.to_dict(orient="records")
        
        return result
    except Exception as e:
        raise Exception(f"获取股东户数详情数据失败: {e}")

def test():
    """
    同步测试方法，用于自动化测试
    
    Returns:
        返回execute方法的执行结果
        
    Raises:
        当execute方法执行异常时直接上抛
    """
    # 使用示例中的参数进行测试
    symbol = "000001"
    
    # 异步调用execute方法
    try:
        result = asyncio.run(execute(symbol))
        return result
    except Exception as e:
        raise e

if __name__ == "__main__":
    # 演示如何调用该函数
    async def main():
        try:
            data = await execute(symbol="000001")
            for item in data:
                print(item)
        except Exception as e:
            print(f"Error: {e}")
    
    asyncio.run(main())