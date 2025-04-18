import asyncio
from typing import List, Dict, Any
import akshare as ak
import pandas as pd

async def execute(symbol: str) -> List[Dict[str, Any]]:
    """
    异步获取东方财富网个股主营构成数据
    
    Args:
        symbol: 股票代码，例如 "SH688041"
        
    Returns:
        主营构成数据列表，每个元素是一个字典
        
    Raises:
        Exception: 当数据获取失败时抛出异常
    """
    try:
        # 调用akshare同步接口获取数据
        df = ak.stock_zygc_em(symbol=symbol)
        
        # 将DataFrame转换为List[Dict]格式
        if not df.empty:
            # 处理可能的NaN值
            df = df.fillna(0)
            return df.to_dict("records")
        return []
    except Exception as e:
        raise Exception(f"获取主营构成数据失败: {e}")

def test():
    """
    同步测试方法，用于自动化测试
    
    Returns:
        主营构成数据列表
        
    Raises:
        异常上抛，不捕获
    """
    # 使用示例参数调用
    return asyncio.run(execute(symbol="SH688041"))

if __name__ == "__main__":
    # 演示如何调用异步函数
    async def main():
        try:
            data = await execute(symbol="SH688041")
            for item in data:
                print(item)
        except Exception as e:
            print(f"Error: {e}")
    
    asyncio.run(main())