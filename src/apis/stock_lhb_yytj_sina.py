import asyncio
from typing import Any, Dict, List
import akshare as ak

async def execute(symbol: str = "5") -> List[Dict[str, Any]]:
    """
    异步获取新浪财经-龙虎榜-营业上榜统计数据
    
    Args:
        symbol: 统计天数，可选 {"5": 最近5天, "10": 最近10天, "30": 最近30天, "60": 最近60天}
    
    Returns:
        营业部上榜统计数据的字典列表
        
    Raises:
        Exception: 当akshare接口调用失败时抛出异常
    """
    try:
        # 调用akshare同步接口，使用run_in_executor避免阻塞事件循环
        loop = asyncio.get_running_loop()
        df = await loop.run_in_executor(None, ak.stock_lhb_yytj_sina, symbol)
        
        # 将DataFrame转换为字典列表
        result = df.to_dict(orient="records")
        return result
    except Exception as e:
        raise Exception(f"Failed to fetch stock lhb yytj data: {str(e)}")

def test() -> List[Dict[str, Any]]:
    """
    同步测试方法，用于自动化测试
    
    Returns:
        营业部上榜统计数据的字典列表
        
    Raises:
        Exception: 当execute方法调用失败时抛出异常
    """
    try:
        # 使用asyncio.run调用异步方法
        result = asyncio.run(execute(symbol="5"))
        return result
    except Exception as e:
        raise Exception(f"Test failed: {str(e)}")

if __name__ == "__main__":
    # 演示如何调用异步函数并打印结果
    async def main():
        try:
            data = await execute(symbol="5")
            print(data)
        except Exception as e:
            print(f"Error occurred: {e}")
    
    asyncio.run(main())