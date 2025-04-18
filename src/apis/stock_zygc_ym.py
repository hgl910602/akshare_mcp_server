import asyncio
from typing import List, Dict, Any
import akshare as ak

async def execute(symbol: str) -> List[Dict[str, Any]]:
    """
    异步获取益盟-F10-主营构成数据
    
    Args:
        symbol: 股票代码，例如 "000001"
        
    Returns:
        主营构成数据列表，每个元素为一个字典
        
    Raises:
        Exception: 当akshare接口调用失败时抛出异常
    """
    try:
        # 调用akshare同步接口，使用await避免阻塞
        df = await asyncio.get_event_loop().run_in_executor(
            None, 
            lambda: ak.stock_zygc_ym(symbol=symbol)
        
        # 将DataFrame转换为List[Dict]格式
        result = df.to_dict(orient="records")
        return result
    except Exception as e:
        raise Exception(f"获取主营构成数据失败: {e}")

def test() -> List[Dict[str, Any]]:
    """
    同步测试方法，用于自动化测试
    
    Returns:
        主营构成数据列表
        
    Raises:
        原样抛出execute方法中的异常
    """
    # 使用示例中的参数进行测试
    symbol = "000001"
    return asyncio.run(execute(symbol))

if __name__ == "__main__":
    # 演示如何调用异步函数
    async def main():
        try:
            data = await execute(symbol="000001")
            print(data)
        except Exception as e:
            print(f"Error: {e}")
    
    asyncio.run(main())