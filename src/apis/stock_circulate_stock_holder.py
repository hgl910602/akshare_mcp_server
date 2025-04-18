import asyncio
from typing import List, Dict, Any
import akshare as ak

async def execute(symbol: str) -> List[Dict[str, Any]]:
    """
    异步获取股票流通股东信息
    
    Args:
        symbol: 股票代码，如 "600000"
        
    Returns:
        流通股东信息列表，每个股东信息为一个字典
        
    Raises:
        Exception: 当获取数据失败时抛出异常
    """
    try:
        # 调用akshare同步接口，使用run_in_executor避免阻塞事件循环
        loop = asyncio.get_event_loop()
        df = await loop.run_in_executor(None, ak.stock_circulate_stock_holder, symbol)
        
        # 将DataFrame转换为List[Dict]格式
        result = df.to_dict(orient='records')
        return result
    except Exception as e:
        raise Exception(f"获取股票流通股东信息失败: {str(e)}")

def test():
    """
    同步测试方法，用于自动化测试
    
    Raises:
        Exception: 当execute方法执行失败时抛出异常
    """
    symbol = "600000"  # 使用示例中的股票代码
    try:
        result = asyncio.run(execute(symbol))
        print(result)
        return result
    except Exception as e:
        raise Exception(f"测试执行失败: {str(e)}")

if __name__ == '__main__':
    # 演示如何调用异步函数
    async def main():
        try:
            symbol = "600000"
            result = await execute(symbol)
            print(result)
        except Exception as e:
            print(f"Error: {str(e)}")
    
    asyncio.run(main())