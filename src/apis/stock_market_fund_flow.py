import asyncio
from typing import List, Dict, Any
import akshare as ak
import pandas as pd

async def execute() -> List[Dict[str, Any]]:
    """
    获取东方财富网-数据中心-资金流向-大盘数据
    
    Returns:
        List[Dict[str, Any]]: 返回资金流向数据的字典列表
        
    Raises:
        Exception: 当获取数据失败时抛出异常
    """
    try:
        # 调用akshare接口获取数据
        df = ak.stock_market_fund_flow()
        
        # 将DataFrame转换为字典列表
        result = df.to_dict(orient='records')
        
        return result
    except Exception as e:
        raise Exception(f"获取大盘资金流向数据失败: {str(e)}")

def test() -> List[Dict[str, Any]]:
    """
    同步测试方法，用于测试execute函数
    
    Returns:
        List[Dict[str, Any]]: 返回资金流向数据的字典列表
        
    Raises:
        Exception: 当execute执行失败时抛出异常
    """
    try:
        return asyncio.run(execute())
    except Exception as e:
        raise e

if __name__ == '__main__':
    # 异步调用示例
    async def main():
        try:
            data = await execute()
            print(data)
        except Exception as e:
            print(f"Error: {e}")
    
    asyncio.run(main())