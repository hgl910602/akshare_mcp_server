import asyncio
from typing import List, Dict, Any
import akshare as ak

async def execute(symbol: str = "最热门") -> List[Dict[str, Any]]:
    """
    异步获取雪球-沪深股市-热度排行榜-讨论排行榜数据
    
    Args:
        symbol: 排行榜类型, "本周新增" 或 "最热门"
    
    Returns:
        List[Dict[str, Any]]: 返回处理后的数据列表
    
    Raises:
        Exception: 当akshare接口调用失败时抛出异常
    """
    try:
        # 调用akshare接口获取数据
        df = ak.stock_hot_tweet_xq(symbol=symbol)
        
        # 将DataFrame转换为List[Dict]格式
        result = df.to_dict(orient="records")
        return result
    except Exception as e:
        raise Exception(f"获取雪球热度数据失败: {str(e)}")

def test() -> List[Dict[str, Any]]:
    """
    同步测试方法, 用于自动化测试
    
    Returns:
        List[Dict[str, Any]]: 返回处理后的数据列表
    
    Raises:
        Exception: 当execute方法调用失败时抛出异常
    """
    try:
        # 使用asyncio.run调用异步方法
        result = asyncio.run(execute(symbol="最热门"))
        return result
    except Exception as e:
        raise Exception(f"测试执行失败: {str(e)}")

if __name__ == "__main__":
    # 演示如何调用异步函数
    async def main():
        try:
            data = await execute(symbol="最热门")
            print(data)
        except Exception as e:
            print(f"Error: {str(e)}")
    
    asyncio.run(main())