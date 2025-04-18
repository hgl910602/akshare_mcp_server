import asyncio
from typing import List, Dict, Any
import akshare as ak

async def execute(symbol: str) -> List[Dict[str, Any]]:
    """
    异步获取同花顺主营介绍数据
    
    Args:
        symbol: 股票代码，例如 "000066"
        
    Returns:
        主营介绍数据的字典列表
        
    Raises:
        Exception: 当akshare接口调用失败时抛出异常
    """
    try:
        # 调用akshare同步接口，使用run_in_executor转为异步
        loop = asyncio.get_running_loop()
        df = await loop.run_in_executor(None, ak.stock_zyjs_ths, symbol)
        return df.to_dict(orient="records")
    except Exception as e:
        raise Exception(f"Failed to fetch stock_zyjs_ths data: {str(e)}")

def test():
    """
    同步测试方法，用于自动化测试
    
    Raises:
        Exception: 当execute方法调用失败时抛出异常
    """
    symbol = "000066"  # 使用示例中的测试参数
    try:
        result = asyncio.run(execute(symbol))
        print(result)
    except Exception as e:
        raise Exception(f"Test failed: {str(e)}")

if __name__ == "__main__":
    # 演示如何调用异步函数
    async def main():
        try:
            result = await execute("000066")  # 使用示例中的测试参数
            print(result)
        except Exception as e:
            print(f"Error occurred: {e}")
    
    asyncio.run(main())