import asyncio
from typing import Any, Dict, List
import akshare as ak

async def execute(symbol: str) -> List[Dict[str, Any]]:
    """
    异步获取东方财富-A股数据-股本结构
    
    Args:
        symbol: 股票代码，例如 "603392.SH"
        
    Returns:
        返回股本结构数据的字典列表
        
    Raises:
        Exception: 当获取数据失败时抛出异常
    """
    try:
        # 调用akshare同步接口，使用await包装
        loop = asyncio.get_event_loop()
        df = await loop.run_in_executor(None, ak.stock_zh_a_gbjg_em, symbol)
        # 将DataFrame转换为List[Dict]格式
        return df.to_dict("records")
    except Exception as e:
        raise Exception(f"获取股本结构数据失败: {e}")

def test():
    """
    同步测试方法，用于自动化测试
    
    Raises:
        Exception: 当execute方法执行失败时抛出异常
    """
    symbol = "603392.SH"  # 使用示例中的测试参数
    try:
        result = asyncio.run(execute(symbol))
        print(result)
        return result
    except Exception as e:
        raise Exception(f"测试execute方法失败: {e}")

if __name__ == "__main__":
    # 演示如何调用异步execute方法
    async def main():
        try:
            result = await execute("603392.SH")
            print(result)
        except Exception as e:
            print(f"Error: {e}")
    
    asyncio.run(main())