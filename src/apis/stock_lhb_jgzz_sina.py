import asyncio
from typing import List, Dict, Any
import akshare as ak
import pandas as pd

async def execute(symbol: str = "5") -> List[Dict[str, Any]]:
    """
    异步获取新浪财经-龙虎榜-机构席位追踪数据
    
    Args:
        symbol: 时间周期, choice of {"5": 最近5天; "10": 最近10天; "30": 最近30天; "60": 最近60天}
    
    Returns:
        List[Dict[str, Any]]: 机构席位追踪数据列表
    
    Raises:
        Exception: 当akshare接口调用失败时抛出异常
    """
    try:
        # 调用akshare接口获取数据
        df = ak.stock_lhb_jgzz_sina(symbol=symbol)
        
        # 将DataFrame转换为List[Dict]格式
        result = df.to_dict(orient="records")
        return result
    except Exception as e:
        raise Exception(f"获取机构席位追踪数据失败: {e}")

def test() -> List[Dict[str, Any]]:
    """
    同步测试方法, 用于自动化测试
    
    Returns:
        List[Dict[str, Any]]: 机构席位追踪数据列表
    
    Raises:
        Exception: 当execute方法调用失败时抛出异常
    """
    try:
        # 使用asyncio.run调用异步方法
        return asyncio.run(execute(symbol="5"))
    except Exception as e:
        raise Exception(f"测试失败: {e}")

if __name__ == "__main__":
    # 演示如何调用异步函数
    async def main():
        try:
            data = await execute(symbol="5")
            print(data)
        except Exception as e:
            print(f"Error: {e}")
    
    asyncio.run(main())