import asyncio
from typing import Any, Dict, List
import akshare as ak
import pandas as pd

async def execute(stock: str, market: str) -> List[Dict[str, Any]]:
    """
    异步获取个股资金流向数据
    
    Args:
        stock: 股票代码
        market: 交易所代码(sh/sz/bj)
    
    Returns:
        资金流向数据列表，每个元素为包含字段的字典
    
    Raises:
        Exception: 当akshare接口调用失败时抛出
    """
    try:
        # 调用akshare同步接口，使用await包装
        df = await asyncio.get_event_loop().run_in_executor(
            None, 
            lambda: ak.stock_individual_fund_flow(stock=stock, market=market)
        )
        
        # 将DataFrame转换为List[Dict]格式
        if not df.empty:
            return df.to_dict("records")
        return []
    except Exception as e:
        raise Exception(f"Failed to fetch stock fund flow data: {str(e)}")

def test():
    """
    同步测试方法，用于自动化测试
    
    Returns:
        测试股票的资金流向数据
    
    Raises:
        原样抛出execute方法中的异常
    """
    # 使用示例参数进行测试
    return asyncio.run(execute(stock="600094", market="sh"))

if __name__ == "__main__":
    # 演示异步调用
    async def main():
        try:
            data = await execute(stock="000425", market="sz")
            for item in data:
                print(item)
        except Exception as e:
            print(f"Error occurred: {e}")
    
    asyncio.run(main())