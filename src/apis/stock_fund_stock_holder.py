import asyncio
from typing import List, Dict, Any
import akshare as ak

async def execute(symbol: str) -> List[Dict[str, Any]]:
    """
    异步获取新浪财经-股本股东-基金持股数据
    
    Args:
        symbol: 股票代码
        
    Returns:
        基金持股数据列表，每个元素是一个字典
        
    Raises:
        Exception: 当获取数据失败时抛出异常
    """
    try:
        # 调用akshare同步接口，使用run_in_executor避免阻塞事件循环
        loop = asyncio.get_event_loop()
        df = await loop.run_in_executor(None, ak.stock_fund_stock_holder, symbol)
        
        # 将DataFrame转换为List[Dict]格式
        result = df.to_dict(orient='records')
        return result
    except Exception as e:
        raise Exception(f"Failed to fetch fund stock holder data for {symbol}: {str(e)}")

def test():
    """
    同步测试方法，用于自动化测试
    
    Raises:
        Exception: 当execute方法执行失败时抛出异常
    """
    # 使用示例中的股票代码进行测试
    symbol = "601318"
    try:
        result = asyncio.run(execute(symbol))
        print(f"Test succeeded, got {len(result)} records")
    except Exception as e:
        raise Exception(f"Test failed: {str(e)}")

if __name__ == '__main__':
    # 演示如何调用异步函数
    async def main():
        try:
            data = await execute("600004")
            print(f"Got {len(data)} records:")
            for item in data[:3]:  # 打印前3条记录
                print(item)
        except Exception as e:
            print(f"Error: {str(e)}")
    
    asyncio.run(main())