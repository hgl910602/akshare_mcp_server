import asyncio
from typing import List, Dict, Any
import akshare as ak
import pandas as pd

async def execute(symbol: str = '近三月') -> List[Dict[str, Any]]:
    """
    异步获取东方财富网-数据中心-大宗交易-营业部排行数据
    
    Args:
        symbol: 时间周期，可选值: '近一月', '近三月', '近六月', '近一年'
        
    Returns:
        返回营业部排行数据的字典列表
        
    Raises:
        Exception: 当获取数据失败时抛出异常
    """
    try:
        # 调用akshare同步接口获取数据
        df = ak.stock_dzjy_yybph(symbol=symbol)
        
        # 将DataFrame转换为字典列表
        result = df.to_dict('records')
        
        return result
    except Exception as e:
        raise Exception(f"获取营业部排行数据失败: {str(e)}")

def test():
    """
    同步测试方法，用于自动化测试
    
    Returns:
        返回execute方法的执行结果
        
    Raises:
        直接抛出execute方法可能产生的异常
    """
    try:
        # 使用asyncio.run运行异步方法
        result = asyncio.run(execute(symbol='近三月'))
        return result
    except Exception as e:
        raise e

if __name__ == '__main__':
    # 演示如何调用异步函数
    async def main():
        try:
            data = await execute(symbol='近三月'))
            print(data)
        except Exception as e:
            print(f"Error: {e}")
    
    asyncio.run(main())