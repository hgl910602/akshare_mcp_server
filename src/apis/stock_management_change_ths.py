import asyncio
from typing import Any, Dict, List
import akshare as ak

async def execute(symbol: str) -> List[Dict[str, Any]]:
    """
    异步获取同花顺-公司大事-高管持股变动数据
    
    Args:
        symbol: 股票代码
        
    Returns:
        List[Dict[str, Any]]: 高管持股变动数据列表
        
    Raises:
        Exception: 当akshare接口调用失败时抛出异常
    """
    try:
        # 调用akshare同步接口，使用await在异步环境中运行
        df = await asyncio.get_event_loop().run_in_executor(
            None, 
            ak.stock_management_change_ths, 
            symbol
        )
        # 将DataFrame转换为List[Dict]格式
        return df.to_dict("records")
    except Exception as e:
        raise Exception(f"Failed to fetch stock management change data: {str(e)}")

def test():
    """
    同步测试方法，用于自动化测试
    
    Returns:
        List[Dict[str, Any]]: 高管持股变动数据列表
        
    Raises:
        Exception: 当execute方法调用失败时抛出异常
    """
    # 使用示例中的测试参数
    test_symbol = "688981"
    try:
        # 使用asyncio.run运行异步方法
        return asyncio.run(execute(test_symbol))
    except Exception as e:
        raise Exception(f"Test failed: {str(e)}")

if __name__ == "__main__":
    # 演示如何调用异步函数
    async def main():
        try:
            data = await execute("688981")
            print(data)
        except Exception as e:
            print(f"Error: {e}")
    
    asyncio.run(main())