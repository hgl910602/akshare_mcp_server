import asyncio
from typing import List, Dict, Any
import akshare as ak

async def execute(stock: str) -> List[Dict[str, Any]]:
    """
    异步获取新股发行信息
    
    Args:
        stock: 股票代码
        
    Returns:
        新股发行信息列表
        
    Raises:
        Exception: 当获取数据失败时抛出异常
    """
    try:
        # 使用akshare同步接口，通过run_in_executor转换为异步
        loop = asyncio.get_event_loop()
        df = await loop.run_in_executor(None, ak.stock_ipo_info, stock)
        return df.to_dict(orient="records")
    except Exception as e:
        raise Exception(f"Failed to fetch IPO info for stock {stock}: {str(e)}")

def test():
    """
    同步测试方法，用于自动化测试
    
    Raises:
        Exception: 当execute方法执行失败时抛出异常
    """
    stock_code = "600004"
    try:
        result = asyncio.run(execute(stock_code))
        print(result)
        return result
    except Exception as e:
        print(f"Test failed: {str(e)}")
        raise

if __name__ == "__main__":
    # 演示如何调用异步函数
    async def main():
        stock_code = "600004"
        try:
            result = await execute(stock_code)
            print(result)
        except Exception as e:
            print(f"Error: {str(e)}")
    
    asyncio.run(main())