import asyncio
from typing import List, Dict, Any
import akshare as ak
import pandas as pd

async def execute(symbol: str = "5") -> List[Dict[str, Any]]:
    """
    异步获取新浪财经龙虎榜个股上榜统计数据
    
    Args:
        symbol: 统计周期，可选值 {"5": 最近5天, "10": 最近10天, "30": 最近30天, "60": 最近60天}
    
    Returns:
        返回龙虎榜个股统计数据的字典列表
    
    Raises:
        Exception: 当akshare接口调用失败时抛出异常
    """
    try:
        # 调用akshare接口获取数据
        df = ak.stock_lhb_ggtj_sina(symbol=symbol)
        
        # 将DataFrame转换为字典列表
        result = df.to_dict(orient="records")
        return result
    except Exception as e:
        raise Exception(f"获取龙虎榜个股统计数据失败: {e}")

def test():
    """
    同步测试方法，用于自动化测试
    
    Returns:
        返回execute方法的执行结果
    
    Raises:
        直接抛出execute方法可能产生的异常
    """
    try:
        # 使用默认参数测试
        result = asyncio.run(execute(symbol="5"))
        return result
    except Exception as e:
        raise

if __name__ == "__main__":
    # 演示如何调用异步函数
    async def main():
        try:
            data = await execute(symbol="5")
            print("获取龙虎榜个股统计数据成功:")
            for item in data:
                print(item)
        except Exception as e:
            print(f"发生错误: {e}")
    
    asyncio.run(main())