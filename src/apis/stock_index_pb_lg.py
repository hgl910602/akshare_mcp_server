import asyncio
from typing import List, Dict, Any
import akshare as ak

async def execute(symbol: str = "上证50") -> List[Dict[str, Any]]:
    """
    异步获取乐咕乐股-指数市净率数据
    
    Args:
        symbol: 指数名称, 可选值见参数说明
        
    Returns:
        返回处理后的字典列表数据
        
    Raises:
        Exception: 当akshare接口调用失败时抛出异常
    """
    try:
        # 调用akshare同步接口
        df = ak.stock_index_pb_lg(symbol=symbol)
        
        # 转换为字典列表
        result = df.to_dict(orient="records")
        
        return result
    except Exception as e:
        raise Exception(f"获取指数市净率数据失败: {e}")

def test():
    """
    同步测试方法，用于自动化测试
    
    Raises:
        直接抛出execute方法中的异常
    """
    try:
        # 使用asyncio.run运行异步方法
        result = asyncio.run(execute(symbol="上证50"))
        return result
    except Exception as e:
        raise e

if __name__ == "__main__":
    # 演示如何调用异步函数
    async def main():
        try:
            data = await execute(symbol="上证50")
            print(data)
        except Exception as e:
            print(f"Error: {e}")
    
    asyncio.run(main())