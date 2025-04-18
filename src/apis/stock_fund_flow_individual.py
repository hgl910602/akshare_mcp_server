import asyncio
from typing import Any, Dict, List, Optional
import akshare as ak
import pandas as pd

async def execute(symbol: str = "即时") -> List[Dict[str, Any]]:
    """
    同花顺-数据中心-资金流向-个股资金流
    
    Args:
        symbol: choice of {"即时", "3日排行", "5日排行", "10日排行", "20日排行"}
    
    Returns:
        List[Dict[str, Any]]: 返回资金流向数据列表
    
    Raises:
        Exception: 当获取数据失败时抛出异常
    """
    try:
        # 调用akshare同步接口
        df = ak.stock_fund_flow_individual(symbol=symbol)
        
        # 处理可能的None返回
        if df is None:
            raise ValueError("No data returned from akshare")
            
        # 将DataFrame转换为List[Dict]
        result = df.to_dict(orient="records")
        return result
    except Exception as e:
        raise Exception(f"Failed to fetch stock fund flow individual data: {str(e)}")

def test():
    """
    同步测试方法，用于自动化测试
    
    Raises:
        Exception: 当execute方法执行失败时抛出异常
    """
    try:
        # 模拟调用示例中的参数
        data = asyncio.run(execute(symbol="3日排行"))
        print(data)
        return data
    except Exception as e:
        raise Exception(f"Test failed: {str(e)}")

if __name__ == "__main__":
    # 演示如何调用异步函数
    async def main():
        try:
            data = await execute(symbol="5日排行")
            print(data)
        except Exception as e:
            print(f"Error occurred: {e}")
    
    asyncio.run(main())