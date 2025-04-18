import asyncio
from typing import List, Dict, Any
import akshare as ak

async def execute(date: str) -> List[Dict[str, Any]]:
    """
    异步获取百度股市通-交易提醒-停复牌数据
    
    Args:
        date: 日期, 格式为"YYYYMMDD"
    
    Returns:
        停复牌数据列表, 每个元素为包含字段的字典
    
    Raises:
        Exception: 当获取数据失败时抛出异常
    """
    try:
        df = ak.news_trade_notify_suspend_baidu(date=date)
        return df.to_dict("records")
    except Exception as e:
        raise Exception(f"获取停复牌数据失败: {e}")

def test():
    """
    同步测试方法, 用于自动化测试
    
    Raises:
        原样抛出execute方法中的异常
    """
    try:
        result = asyncio.run(execute(date="20241107"))
        print(result)
        return result
    except Exception as e:
        print(f"测试失败: {e}")
        raise

if __name__ == "__main__":
    # 演示如何调用异步函数
    async def main():
        try:
            data = await execute(date="20241107")
            print(data)
        except Exception as e:
            print(f"调用失败: {e}")
    
    asyncio.run(main())