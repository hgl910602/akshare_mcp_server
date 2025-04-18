import asyncio
from typing import List, Dict, Any
import akshare as ak
import pandas as pd

async def execute(symbol: str) -> List[Dict[str, Any]]:
    """
    异步获取东方财富网分红送配详情数据
    
    Args:
        symbol: 股票代码, 如 "300073"
        
    Returns:
        分红送配详情数据列表, 每个元素为字典格式
        
    Raises:
        Exception: 当数据获取失败时抛出异常
    """
    try:
        # 调用akshare同步接口获取数据
        df = ak.stock_fhps_detail_em(symbol=symbol)
        
        # 将DataFrame转换为List[Dict]格式
        if not df.empty:
            # 处理可能的NaN值
            df = df.where(pd.notnull(df), None)
            return df.to_dict("records")
        return []
    except Exception as e:
        raise Exception(f"Failed to fetch stock_fhps_detail_em data: {str(e)}")

def test():
    """
    同步测试方法, 用于验证execute函数
    
    Raises:
        直接抛出execute方法中的异常
    """
    # 使用示例参数调用
    return asyncio.run(execute(symbol="300073"))

if __name__ == "__main__":
    # 演示如何调用异步函数
    async def main():
        try:
            data = await execute(symbol="300073")
            print(data)
        except Exception as e:
            print(f"Error occurred: {e}")
    
    asyncio.run(main())