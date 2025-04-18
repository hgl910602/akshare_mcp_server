import asyncio
from typing import List, Dict, Any
import akshare as ak
import pandas as pd

async def execute(symbol: str) -> List[Dict[str, Any]]:
    """
    获取东方财富网个股限售解禁数据(异步版本)
    
    Args:
        symbol: 股票代码, 如 "600000"
        
    Returns:
        限售解禁数据列表, 每个元素是一个字典
        
    Raises:
        Exception: 当获取数据失败时抛出异常
    """
    try:
        # 调用akshare同步接口获取数据
        df = ak.stock_restricted_release_queue_em(symbol=symbol)
        
        # 将DataFrame转换为List[Dict]格式
        if not df.empty:
            # 处理可能的NaN值
            df = df.fillna(0)
            return df.to_dict("records")
        return []
    except Exception as e:
        raise Exception(f"获取限售解禁数据失败: {e}")

def test():
    """
    同步测试方法, 用于自动化测试
    
    Raises:
        原样抛出execute方法中的异常
    """
    # 使用示例中的参数进行测试
    symbol = "600000"
    try:
        result = asyncio.run(execute(symbol))
        print(f"测试成功, 获取到{len(result)}条数据")
        return result
    except Exception as e:
        print(f"测试失败: {e}")
        raise

if __name__ == "__main__":
    # 演示如何调用异步函数
    async def main():
        try:
            data = await execute(symbol="600000")
            print(f"获取到{len(data)}条限售解禁数据:")
            for item in data:
                print(item)
        except Exception as e:
            print(f"发生错误: {e}")
    
    asyncio.run(main())