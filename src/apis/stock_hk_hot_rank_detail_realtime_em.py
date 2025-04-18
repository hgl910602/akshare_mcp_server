import asyncio
from typing import List, Dict, Any
import akshare as ak

async def execute(symbol: str = "00700") -> List[Dict[str, Any]]:
    """
    获取东方财富网-港股个股人气榜-实时变动数据
    
    Args:
        symbol: 股票代码，例如"00700"
        
    Returns:
        List[Dict[str, Any]]: 包含实时排名数据的字典列表
        
    Raises:
        Exception: 当获取数据失败时抛出异常
    """
    try:
        # 调用akshare同步接口
        df = ak.stock_hk_hot_rank_detail_realtime_em(symbol=symbol)
        
        # 将DataFrame转换为List[Dict]格式
        result = df.to_dict("records")
        
        # 确保返回的是列表
        if not isinstance(result, list):
            return [result] if result is not None else []
        return result
    except Exception as e:
        raise Exception(f"Failed to fetch stock hot rank data: {str(e)}")

def test():
    """
    同步测试方法，用于自动化测试
    
    Returns:
        List[Dict[str, Any]]: 包含实时排名数据的字典列表
        
    Raises:
        Exception: 当execute方法执行失败时抛出异常
    """
    try:
        # 使用asyncio.run调用异步方法
        return asyncio.run(execute(symbol="00700"))
    except Exception as e:
        raise Exception(f"Test failed: {str(e)}")

if __name__ == "__main__":
    # 演示如何调用异步函数
    async def main():
        try:
            data = await execute(symbol="00700")
            print(data)
        except Exception as e:
            print(f"Error: {e}")
    
    asyncio.run(main())