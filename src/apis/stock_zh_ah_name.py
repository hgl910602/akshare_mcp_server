import asyncio
from typing import List, Dict, Any
import akshare as ak

async def execute() -> List[Dict[str, Any]]:
    """
    异步获取A+H股股票名称和代码数据
    
    Returns:
        List[Dict[str, Any]]: 包含股票代码和名称的字典列表
        
    Raises:
        Exception: 当数据获取失败时抛出异常
    """
    try:
        # 调用akshare同步接口，使用run_in_executor避免阻塞事件循环
        loop = asyncio.get_event_loop()
        df = await loop.run_in_executor(None, ak.stock_zh_ah_name)
        return df.to_dict("records")
    except Exception as e:
        raise Exception(f"Failed to fetch A+H stock data: {str(e)}")

def test() -> List[Dict[str, Any]]:
    """
    同步测试方法，用于自动化测试
    
    Returns:
        List[Dict[str, Any]]: 包含股票代码和名称的字典列表
        
    Raises:
        Exception: 当execute方法执行失败时抛出异常
    """
    return asyncio.run(execute())

if __name__ == "__main__":
    # 演示异步调用方式
    async def main():
        try:
            data = await execute()
            print(data[:5])  # 打印前5条数据
        except Exception as e:
            print(f"Error occurred: {e}")
    
    asyncio.run(main())