import asyncio
from typing import List, Dict, Any
import akshare as ak

async def execute(symbol: str = "上证A股") -> List[Dict[str, Any]]:
    """
    异步获取乐咕乐股-A股股息率数据
    
    Args:
        symbol: 股票市场类型，可选值: "上证A股", "深证A股", "创业板", "科创板"
        
    Returns:
        List[Dict[str, Any]]: 包含股息率数据的字典列表
        
    Raises:
        Exception: 当获取数据失败时抛出异常
    """
    try:
        # 调用akshare同步接口，使用await包装
        df = await asyncio.get_event_loop().run_in_executor(
            None, 
            lambda: ak.stock_a_gxl_lg(symbol=symbol)
        )
        # 将DataFrame转换为List[Dict]格式
        return df.to_dict("records")
    except Exception as e:
        raise Exception(f"获取A股股息率数据失败: {str(e)}")

def test():
    """
    同步测试方法，用于自动化测试
    
    Raises:
        原样抛出execute方法中的异常
    """
    try:
        # 使用asyncio.run运行异步方法
        result = asyncio.run(execute(symbol="上证A股"))
        return result
    except Exception as e:
        raise  # 异常上抛

if __name__ == "__main__":
    # 演示如何调用异步函数
    async def main():
        try:
            data = await execute(symbol="上证A股")
            print(data)
        except Exception as e:
            print(f"Error: {e}")
    
    asyncio.run(main())