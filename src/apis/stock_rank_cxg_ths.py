import asyncio
from typing import List, Dict, Any
import akshare as ak

async def execute(symbol: str = "创月新高") -> List[Dict[str, Any]]:
    """
    异步获取同花顺创新高股票数据
    
    Args:
        symbol: 创新高类型, 可选值: "创月新高", "半年新高", "一年新高", "历史新高"
        
    Returns:
        创新高股票数据列表, 每个股票为一个字典
        
    Raises:
        Exception: 当获取数据失败时抛出异常
    """
    try:
        # 调用akshare同步接口, 使用await asyncio.to_thread在异步环境中运行同步代码
        df = await asyncio.to_thread(ak.stock_rank_cxg_ths, symbol=symbol)
        return df.to_dict("records")
    except Exception as e:
        raise Exception(f"获取创新高股票数据失败: {e}")

def test() -> List[Dict[str, Any]]:
    """
    同步测试方法, 用于自动化测试
    
    Returns:
        创新高股票数据列表
        
    Raises:
        原样抛出execute方法中的异常
    """
    return asyncio.run(execute(symbol="创月新高"))

if __name__ == "__main__":
    # 演示如何调用异步函数
    async def main():
        try:
            data = await execute(symbol="创月新高")
            print(data[:2])  # 打印前两条数据
        except Exception as e:
            print(f"Error: {e}")
    
    asyncio.run(main())