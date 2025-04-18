import asyncio
from typing import Any, Dict, List, Optional
import aiohttp
import akshare as ak
import pandas as pd

async def execute(symbol: str = "全部股票") -> List[Dict[str, Any]]:
    """
    异步获取东方财富网-数据中心-新股数据-新股申购与中签查询数据
    
    Args:
        symbol: 股票类型，可选值: "全部股票", "沪市主板", "科创板", "深市主板", "创业板", "北交所"
    
    Returns:
        返回新股申购与中签数据的字典列表
    
    Raises:
        Exception: 当获取数据失败时抛出异常
    """
    try:
        # 使用akshare同步接口获取数据
        df = ak.stock_xgsglb_em(symbol=symbol)
        
        # 将DataFrame转换为字典列表
        result = df.to_dict(orient="records")
        
        return result
    except Exception as e:
        raise Exception(f"获取新股申购与中签数据失败: {e}")

def test() -> List[Dict[str, Any]]:
    """
    同步测试方法，用于自动化测试
    
    Returns:
        返回新股申购与中签数据的字典列表
    
    Raises:
        原样抛出execute方法中的异常
    """
    try:
        # 使用asyncio.run运行异步方法
        result = asyncio.run(execute(symbol="北交所"))
        return result
    except Exception as e:
        raise e

if __name__ == "__main__":
    # 演示如何调用异步函数
    async def main():
        try:
            data = await execute(symbol="北交所")
            print("获取数据成功:")
            for item in data[:2]:  # 打印前两条数据
                print(item)
        except Exception as e:
            print(f"发生错误: {e}")
    
    asyncio.run(main())