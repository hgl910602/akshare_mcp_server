import asyncio
from typing import Any, Dict, List
import akshare as ak

async def execute(date: str) -> List[Dict[str, Any]]:
    """
    异步获取上海证券交易所每日股票成交概况数据
    
    Args:
        date: 日期, 格式为"YYYYMMDD", 例如"20250221"
        
    Returns:
        返回包含每日股票成交概况数据的字典列表
        
    Raises:
        Exception: 当获取数据失败时抛出异常
    """
    try:
        # 调用akshare同步接口，使用run_in_executor避免阻塞事件循环
        loop = asyncio.get_running_loop()
        df = await loop.run_in_executor(None, ak.stock_sse_deal_daily, date)
        
        # 将DataFrame转换为List[Dict]格式
        result = df.to_dict(orient="records")
        return result
    except Exception as e:
        raise Exception(f"获取上海证券交易所每日股票成交概况数据失败: {e}")

def test():
    """
    同步测试方法，用于自动化测试
    
    Raises:
        任何execute方法可能抛出的异常
    """
    # 使用示例中的测试日期
    test_date = "20250221"
    result = asyncio.run(execute(test_date))
    print(result)

if __name__ == "__main__":
    # 演示如何调用异步函数
    async def main():
        try:
            # 使用示例中的测试日期
            data = await execute("20250221")
            print(data)
        except Exception as e:
            print(f"Error: {e}")
    
    asyncio.run(main())