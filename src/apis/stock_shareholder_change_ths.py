import asyncio
from typing import List, Dict, Any
import akshare as ak
import pandas as pd

async def execute(symbol: str) -> List[Dict[str, Any]]:
    """
    异步获取同花顺公司股东持股变动数据
    
    Args:
        symbol: 股票代码
        
    Returns:
        股东持股变动数据列表，每个元素为一个字典
        
    Raises:
        Exception: 当获取数据失败时抛出异常
    """
    try:
        # 调用akshare接口获取数据
        df = ak.stock_shareholder_change_ths(symbol=symbol)
        
        # 将DataFrame转换为List[Dict]格式
        if not df.empty:
            return df.to_dict(orient="records")
        return []
    except Exception as e:
        raise Exception(f"Failed to fetch shareholder change data: {str(e)}")

def test():
    """
    同步测试方法，用于自动化测试
    
    Raises:
        Exception: 当execute方法执行失败时抛出异常
    """
    # 使用示例中的股票代码进行测试
    test_symbol = "688981"
    try:
        result = asyncio.run(execute(symbol=test_symbol))
        print(f"Test successful. Got {len(result)} records.")
        return result
    except Exception as e:
        print(f"Test failed: {str(e)}")
        raise

if __name__ == "__main__":
    # 演示如何调用该函数
    async def main():
        try:
            data = await execute(symbol="688981")
            print(f"Got {len(data)} records:")
            for item in data[:3]:  # 打印前3条记录
                print(item)
        except Exception as e:
            print(f"Error: {str(e)}")
    
    asyncio.run(main())