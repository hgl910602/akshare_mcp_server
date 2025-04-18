import asyncio
from typing import List, Dict, Any
import akshare as ak

async def execute(symbol: str = "00700") -> List[Dict[str, Any]]:
    """
    东方财富-个股人气榜-最新排名
    
    Args:
        symbol: 股票代码，例如："00700"
        
    Returns:
        List[Dict[str, Any]]: 返回处理后的数据列表
        
    Raises:
        Exception: 当获取数据失败时抛出异常
    """
    try:
        # 调用akshare接口获取数据
        df = ak.stock_hk_hot_rank_latest_em(symbol=symbol)
        # 将DataFrame转换为List[Dict]格式
        result = df.to_dict(orient="records")
        return result
    except Exception as e:
        raise Exception(f"获取股票人气榜数据失败: {e}")

def test():
    """
    同步测试方法，用于自动化测试
    
    Returns:
        List[Dict[str, Any]]: 返回处理后的数据列表
        
    Raises:
        Exception: 当获取数据失败时抛出异常
    """
    try:
        # 使用示例参数调用异步方法
        result = asyncio.run(execute(symbol="00700"))
        return result
    except Exception as e:
        raise e

if __name__ == "__main__":
    # 演示如何调用该函数
    async def main():
        try:
            data = await execute(symbol="00700")
            print(data)
        except Exception as e:
            print(f"Error: {e}")

    asyncio.run(main())