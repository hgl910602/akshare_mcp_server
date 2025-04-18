import asyncio
from typing import List, Dict, Any
import akshare as ak
import pandas as pd

async def execute(symbol: str) -> List[Dict[str, Any]]:
    """
    异步获取A股历史分笔数据
    
    Args:
        symbol: 股票代码，例如 "sh600000"
        
    Returns:
        返回包含分笔数据的字典列表
        
    Raises:
        Exception: 当数据获取失败时抛出异常
    """
    try:
        # 调用akshare接口获取数据
        df = ak.stock_zh_a_tick_tx(symbol=symbol)
        
        # 将DataFrame转换为字典列表
        result = df.to_dict(orient='records')
        return result
    except Exception as e:
        raise Exception(f"Failed to fetch tick data for {symbol}: {str(e)}")

def test():
    """
    同步测试方法，用于自动化测试
    
    Raises:
        原样抛出execute方法中的异常
    """
    # 使用示例中的测试参数
    test_symbol = "sz000001"
    try:
        result = asyncio.run(execute(test_symbol))
        print(f"Test completed. Got {len(result)} records.")
        return result
    except Exception as e:
        print(f"Test failed: {str(e)}")
        raise

if __name__ == '__main__':
    # 演示如何调用该函数
    async def main():
        try:
            # 使用示例中的参数调用
            data = await execute(symbol="sh600000")
            print(f"Got {len(data)} records.")
            if data:
                print("Sample record:")
                print(data[0])
        except Exception as e:
            print(f"Error: {str(e)}")
    
    asyncio.run(main())