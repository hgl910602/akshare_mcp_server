import asyncio
from typing import List, Dict, Any
import akshare as ak

async def execute(symbol: str) -> List[Dict[str, Any]]:
    """
    异步获取益盟-F10-管理层讨论与分析数据
    
    Args:
        symbol: 股票代码，例如 "000001"
        
    Returns:
        返回包含管理层讨论与分析数据的列表，每个元素为字典格式
        
    Raises:
        Exception: 当数据获取失败时抛出异常
    """
    try:
        # 调用akshare同步接口，使用await在异步环境中执行
        df = await asyncio.get_event_loop().run_in_executor(
            None, 
            lambda: ak.stock_mda_ym(symbol=symbol)
        )
        # 将DataFrame转换为List[Dict]格式
        return df.to_dict("records")
    except Exception as e:
        raise Exception(f"Failed to fetch stock_mda_ym data: {str(e)}")

def test():
    """
    同步测试方法，用于自动化测试
    
    Raises:
        原样抛出execute方法中的异常
    """
    # 使用示例参数调用execute方法
    result = asyncio.run(execute(symbol="000001"))
    return result

if __name__ == "__main__":
    # 演示如何调用异步函数
    async def main():
        try:
            data = await execute(symbol="000001")
            print(data)
        except Exception as e:
            print(f"Error occurred: {e}")
    
    asyncio.run(main())