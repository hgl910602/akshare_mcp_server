import asyncio
from typing import List, Dict, Any
import akshare as ak

async def execute(symbol: str) -> List[Dict[str, Any]]:
    """
    异步获取同花顺分红配送详情
    
    Args:
        symbol: 股票代码，如 "603444"
        
    Returns:
        分红配送详情列表，每个元素为字典形式
        
    Raises:
        Exception: 当接口调用失败时抛出异常
    """
    try:
        # 调用akshare同步接口，使用run_in_executor避免阻塞事件循环
        loop = asyncio.get_running_loop()
        df = await loop.run_in_executor(None, ak.stock_fhps_detail_ths, symbol)
        return df.to_dict("records")
    except Exception as e:
        raise Exception(f"Failed to fetch stock_fhps_detail_ths: {str(e)}")

def test():
    """
    同步测试方法，用于自动化测试
    
    Returns:
        同execute方法的返回
        
    Raises:
        原样抛出execute方法中的异常
    """
    symbol = "603444"  # 使用示例中的测试参数
    return asyncio.run(execute(symbol))

if __name__ == "__main__":
    # 演示如何调用异步函数
    async def main():
        try:
            result = await execute(symbol="603444")
            print(result)
        except Exception as e:
            print(f"Error occurred: {e}")
    
    asyncio.run(main())