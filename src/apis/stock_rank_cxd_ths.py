import asyncio
from typing import List, Dict, Any
import akshare as ak
import pandas as pd

async def execute(symbol: str = "创月新低") -> List[Dict[str, Any]]:
    """
    异步获取同花顺创新低股票数据
    
    Args:
        symbol: 创新低类型，可选值: "创月新低", "半年新低", "一年新低", "历史新低"
    
    Returns:
        创新低股票数据列表，每个股票为字典形式
    
    Raises:
        ValueError: 当输入参数不合法时抛出
        Exception: 当获取数据失败时抛出
    """
    valid_symbols = {"创月新低", "半年新低", "一年新低", "历史新低"}
    if symbol not in valid_symbols:
        raise ValueError(f"symbol参数必须为以下值之一: {valid_symbols}")
    
    try:
        # 使用akshare同步接口获取数据
        df = ak.stock_rank_cxd_ths(symbol=symbol)
        
        # 处理可能的空数据情况
        if df.empty:
            return []
            
        # 转换DataFrame为List[Dict]格式
        result = df.to_dict(orient="records")
        return result
    except Exception as e:
        raise Exception(f"获取创新低股票数据失败: {str(e)}")

def test():
    """
    同步测试函数，用于自动化测试
    
    Raises:
        原样抛出execute方法中的任何异常
    """
    try:
        # 使用asyncio.run运行异步函数
        result = asyncio.run(execute(symbol="创月新低"))
        return result
    except Exception as e:
        raise e

if __name__ == "__main__":
    # 演示如何调用异步函数
    async def main():
        try:
            data = await execute(symbol="创月新低")
            print(data[:2])  # 打印前两条数据
        except Exception as e:
            print(f"发生错误: {e}")
    
    asyncio.run(main())