import asyncio
from typing import List, Dict, Any
import akshare as ak

async def execute(symbol: str) -> List[Dict[str, Any]]:
    """
    异步获取东方财富指定个股的新闻资讯数据
    
    Args:
        symbol: 股票代码或其他关键词
        
    Returns:
        返回包含新闻数据的字典列表
        
    Raises:
        Exception: 当获取数据失败时抛出异常
    """
    try:
        # 调用akshare的同步接口，使用await在异步环境中执行
        loop = asyncio.get_event_loop()
        df = await loop.run_in_executor(None, ak.stock_news_em, symbol)
        # 将DataFrame转换为字典列表
        return df.to_dict('records')
    except Exception as e:
        raise Exception(f"Failed to fetch stock news: {str(e)}")

def test():
    """
    同步测试方法，用于自动化测试
    
    Raises:
        Exception: 当execute方法执行失败时抛出异常
    """
    try:
        # 使用asyncio.run运行异步方法
        result = asyncio.run(execute(symbol="300059"))
        print("Test executed successfully")
        return result
    except Exception as e:
        print(f"Test failed: {str(e)}")
        raise

if __name__ == '__main__':
    # 演示如何调用异步函数
    async def main():
        try:
            data = await execute(symbol="300059")
            print(data)
        except Exception as e:
            print(f"Error: {str(e)}")
    
    asyncio.run(main())