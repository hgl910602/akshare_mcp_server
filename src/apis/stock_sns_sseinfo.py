import asyncio
from typing import List, Dict, Any
import akshare as ak

async def execute(symbol: str) -> List[Dict[str, Any]]:
    """
    异步获取上证e互动-提问与回答数据
    
    Args:
        symbol: 股票代码
        
    Returns:
        返回包含互动问答数据的字典列表
        
    Raises:
        Exception: 当akshare接口调用失败时抛出异常
    """
    try:
        # 调用akshare同步接口，使用await包装
        df = await asyncio.get_event_loop().run_in_executor(
            None, 
            ak.stock_sns_sseinfo, 
            symbol
        )
        # 将DataFrame转换为List[Dict]格式
        return df.to_dict("records")
    except Exception as e:
        raise Exception(f"获取上证e互动数据失败: {e}")

def test():
    """
    同步测试方法，用于自动化测试
    
    Returns:
        返回execute方法的执行结果
        
    Raises:
        直接抛出execute方法可能产生的异常
    """
    # 使用示例中的参数进行测试
    symbol = "603119"
    return asyncio.run(execute(symbol))

if __name__ == "__main__":
    # 演示如何调用异步函数
    async def main():
        try:
            data = await execute(symbol="603119")
            print(data)
        except Exception as e:
            print(f"Error: {e}")

    asyncio.run(main())