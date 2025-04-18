import asyncio
from typing import List, Dict, Any
import akshare as ak

async def execute(symbol: str, token: str = None, timeout: float = None) -> List[Dict[str, Any]]:
    """
    异步获取美股个股基本信息(雪球)
    
    Args:
        symbol: 股票代码
        token: 访问令牌(可选)
        timeout: 超时时间(可选)
        
    Returns:
        包含个股信息的字典列表
        
    Raises:
        Exception: 当获取数据失败时抛出异常
    """
    try:
        # 调用akshare同步接口，使用run_in_executor避免阻塞事件循环
        loop = asyncio.get_running_loop()
        df = await loop.run_in_executor(
            None, 
            lambda: ak.stock_individual_basic_info_us_xq(symbol=symbol, token=token, timeout=timeout)
        )
        # 将DataFrame转换为List[Dict]格式
        return df.to_dict('records')
    except Exception as e:
        raise Exception(f"Failed to fetch stock info for {symbol}: {str(e)}")

def test():
    """
    同步测试方法，用于自动化测试
    
    Raises:
        Exception: 当execute方法执行失败时抛出异常
    """
    try:
        result = asyncio.run(execute(symbol="NVDA"))
        print(result)
        return result
    except Exception as e:
        print(f"Test failed: {str(e)}")
        raise

if __name__ == '__main__':
    # 演示如何异步调用该函数
    async def main():
        try:
            result = await execute(symbol="NVDA")
            print(result)
        except Exception as e:
            print(f"Error: {str(e)}")
    
    asyncio.run(main())