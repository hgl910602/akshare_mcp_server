import asyncio
from typing import List, Dict, Any
import akshare as ak
import pandas as pd

async def execute(symbol: str) -> List[Dict[str, Any]]:
    """
    异步获取东方财富网股票热度历史趋势及粉丝特征数据
    
    Args:
        symbol: 股票代码，例如 "SZ000665"
        
    Returns:
        包含股票热度数据的字典列表
        
    Raises:
        Exception: 当数据获取失败时抛出异常
    """
    try:
        # 调用akshare的同步接口，使用await包装
        df = await asyncio.get_event_loop().run_in_executor(
            None, 
            ak.stock_hot_rank_detail_em, 
            symbol
        )
        
        # 将DataFrame转换为字典列表
        if isinstance(df, pd.DataFrame) and not df.empty:
            return df.to_dict("records")
        return []
    except Exception as e:
        raise Exception(f"Failed to fetch stock hot rank details: {str(e)}")

def test():
    """
    同步测试方法，用于自动化测试
    
    Raises:
        原样抛出execute方法中的异常
    """
    # 使用示例参数调用
    symbol = "SZ000665"
    return asyncio.run(execute(symbol))

if __name__ == "__main__":
    # 演示如何调用异步函数
    async def main():
        try:
            data = await execute(symbol="SZ000665")
            print(data)
        except Exception as e:
            print(f"Error occurred: {e}")
    
    asyncio.run(main())