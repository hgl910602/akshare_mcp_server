import asyncio
from typing import List, Dict, Any
import akshare as ak
import pandas as pd

async def execute(symbol: str) -> List[Dict[str, Any]]:
    """
    异步获取东方财富网个股估值数据
    
    Args:
        symbol: A股代码，如"002044"
    
    Returns:
        包含估值数据的字典列表
        
    Raises:
        Exception: 当获取数据失败时抛出异常
    """
    try:
        # 调用akshare接口获取数据
        df = ak.stock_value_em(symbol=symbol)
        
        # 将DataFrame转换为字典列表
        result = df.to_dict(orient="records")
        
        return result
    except Exception as e:
        raise Exception(f"获取股票估值数据失败: {str(e)}")

def test():
    """
    同步测试方法，用于自动化测试
    
    Raises:
        Exception: 当execute方法执行失败时抛出异常
    """
    try:
        # 使用示例参数调用execute方法
        result = asyncio.run(execute(symbol="300766"))
        print(result)
        return result
    except Exception as e:
        raise Exception(f"测试失败: {str(e)}")

if __name__ == "__main__":
    # 演示如何调用该函数
    async def main():
        try:
            data = await execute(symbol="300766"))
            print("获取数据成功:")
            for item in data:
                print(item)
        except Exception as e:
            print(f"发生错误: {e}")
    
    asyncio.run(main())