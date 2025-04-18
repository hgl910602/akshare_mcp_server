import asyncio
from typing import List, Dict, Any
import akshare as ak
import pandas as pd

async def execute(symbol: str = "北向资金") -> List[Dict[str, Any]]:
    """
    获取东方财富-沪深港通分时数据
    
    Args:
        symbol: 资金类型, "北向资金" 或 "南向资金"
        
    Returns:
        List[Dict[str, Any]]: 转换后的数据列表
        
    Raises:
        ValueError: 当symbol参数不合法时
        Exception: 当akshare接口调用失败时
    """
    if symbol not in ["北向资金", "南向资金"]:
        raise ValueError("symbol参数必须是'北向资金'或'南向资金'")
    
    try:
        # 调用akshare接口
        df = ak.stock_hsgt_fund_min_em(symbol=symbol)
        
        # 将DataFrame转换为List[Dict]格式
        result = df.to_dict(orient="records")
        return result
    except Exception as e:
        raise Exception(f"获取沪深港通分时数据失败: {e}")

def test():
    """
    同步测试方法
    """
    try:
        # 使用示例参数调用execute方法
        data = asyncio.run(execute(symbol="南向资金"))
        print(data)
        return data
    except Exception as e:
        print(f"测试失败: {e}")
        raise

if __name__ == "__main__":
    # 演示如何调用异步函数
    async def main():
        try:
            data = await execute(symbol="南向资金")
            print(data)
        except Exception as e:
            print(f"调用失败: {e}")
    
    asyncio.run(main())