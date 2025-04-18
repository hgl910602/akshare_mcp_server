import asyncio
from typing import List, Dict, Any
import akshare as ak
import pandas as pd

async def execute(symbol: str) -> List[Dict[str, Any]]:
    """
    异步获取新浪财经-发行分配-限售解禁数据
    
    Args:
        symbol: 股票代码
        
    Returns:
        限售解禁数据列表，每个元素为字典格式
        
    Raises:
        Exception: 当获取数据失败时抛出异常
    """
    try:
        # 调用akshare同步接口
        df = ak.stock_restricted_release_queue_sina(symbol=symbol)
        
        # 处理可能的空数据情况
        if df.empty:
            return []
            
        # 转换DataFrame为List[Dict]格式
        result = df.to_dict(orient="records")
        return result
    except Exception as e:
        raise Exception(f"获取限售解禁数据失败: {str(e)}")

def test():
    """
    同步测试方法，用于自动化测试
    
    Returns:
        限售解禁数据列表
        
    Raises:
        原样抛出execute方法中的异常
    """
    symbol = "600000"  # 使用示例中的测试股票代码
    return asyncio.run(execute(symbol))

if __name__ == "__main__":
    # 演示如何调用异步函数
    async def main():
        try:
            data = await execute(symbol="600000")
            for item in data:
                print(item)
        except Exception as e:
            print(f"Error: {e}")
    
    asyncio.run(main())