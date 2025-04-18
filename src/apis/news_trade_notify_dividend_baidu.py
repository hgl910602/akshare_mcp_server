import asyncio
from typing import List, Dict, Any
import akshare as ak

async def execute(date: str) -> List[Dict[str, Any]]:
    """
    异步获取百度股市通-交易提醒-分红派息数据
    
    Args:
        date: 日期, 格式为"YYYYMMDD"
    
    Returns:
        分红派息数据列表, 每个元素为字典形式
        
    Raises:
        Exception: 当akshare接口调用失败时抛出
    """
    try:
        # 调用akshare同步接口，使用await包装
        df = await asyncio.get_event_loop().run_in_executor(
            None, 
            lambda: ak.news_trade_notify_dividend_baidu(date=date)
        )
        # 将DataFrame转换为List[Dict]格式
        return df.to_dict(orient="records")
    except Exception as e:
        raise Exception(f"获取分红派息数据失败: {e}")

def test():
    """
    同步测试方法，用于自动化测试
    
    Returns:
        分红派息数据列表
        
    Raises:
        原样抛出execute方法中的异常
    """
    # 使用示例中的参数
    test_date = "20241107"
    return asyncio.run(execute(date=test_date))

if __name__ == "__main__":
    # 演示如何调用异步函数
    async def main():
        try:
            data = await execute(date="20241107")
            print(data)
        except Exception as e:
            print(f"Error: {e}")
    
    asyncio.run(main())