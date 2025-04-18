import asyncio
from typing import List, Dict, Any
import akshare as ak
import pandas as pd

async def execute(symbol: str = "特朗普概念股") -> List[Dict[str, Any]]:
    """
    异步获取富途牛牛美股概念成分股数据
    
    Args:
        symbol: 概念板块名称，可选值: "巴菲特持仓", "佩洛西持仓", "特朗普概念股"
    
    Returns:
        概念成分股列表，每个元素为包含股票信息的字典
    
    Raises:
        Exception: 当akshare接口调用失败时抛出异常
    """
    try:
        # 调用akshare同步接口获取数据
        df = ak.stock_concept_cons_futu(symbol=symbol)
        
        # 将DataFrame转换为List[Dict]格式
        if not df.empty:
            # 处理可能的NaN值
            df = df.fillna("")
            return df.to_dict("records")
        return []
    except Exception as e:
        raise Exception(f"获取概念成分股数据失败: {str(e)}")

def test():
    """
    同步测试方法，用于自动化测试
    
    Returns:
        概念成分股列表
    
    Raises:
        原样抛出execute方法中的异常
    """
    try:
        return asyncio.run(execute(symbol="特朗普概念股"))
    except Exception as e:
        raise e

if __name__ == "__main__":
    # 演示如何调用异步函数
    async def main():
        try:
            data = await execute(symbol="特朗普概念股")
            print(data)
        except Exception as e:
            print(f"Error: {e}")
    
    asyncio.run(main())