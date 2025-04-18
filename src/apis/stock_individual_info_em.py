import asyncio
from typing import List, Dict, Any
import akshare as ak

async def execute(symbol: str, timeout: float = None) -> List[Dict[str, Any]]:
    """
    东方财富-个股-股票信息(异步版本)
    
    Args:
        symbol: 股票代码, 如 "000001"
        timeout: 超时时间, 默认为None
        
    Returns:
        List[Dict[str, Any]]: 包含股票信息的字典列表
        
    Raises:
        Exception: 当获取数据失败时抛出异常
    """
    try:
        # 由于akshare目前没有原生异步支持，这里使用run_in_executor来异步化同步调用
        loop = asyncio.get_running_loop()
        df = await loop.run_in_executor(
            None, 
            lambda: ak.stock_individual_info_em(symbol=symbol, timeout=timeout)
        )
        # 将DataFrame转换为List[Dict]格式
        return df.to_dict('records')
    except Exception as e:
        raise Exception(f"获取股票信息失败: {e}")

def test():
    """
    同步测试方法，用于自动化测试
    
    Returns:
        List[Dict[str, Any]]: 包含股票信息的字典列表
        
    Raises:
        Exception: 当获取数据失败时抛出异常
    """
    # 使用示例参数进行测试
    symbol = "000001"  # 平安银行
    try:
        result = asyncio.run(execute(symbol=symbol))
        return result
    except Exception as e:
        raise Exception(f"测试失败: {e}")

if __name__ == '__main__':
    # 演示如何调用异步函数
    async def main():
        try:
            symbol = "600000"  # 浦发银行
            result = await execute(symbol=symbol)
            print(result)
        except Exception as e:
            print(f"Error: {e}")
    
    asyncio.run(main())