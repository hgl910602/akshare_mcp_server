import asyncio
from typing import List, Dict, Any
import akshare as ak
import pandas as pd

async def execute(symbol: str) -> List[Dict[str, Any]]:
    """
    异步获取巨潮资讯个股历史分红数据
    
    Args:
        symbol: 股票代码, 如 "600009"
    
    Returns:
        历史分红数据列表, 每个元素为包含各字段的字典
        
    Raises:
        Exception: 当数据获取失败时抛出异常
    """
    try:
        # 调用akshare同步接口获取数据
        df = ak.stock_dividend_cninfo(symbol=symbol)
        
        # 处理空数据情况
        if df.empty:
            return []
            
        # 转换DataFrame为List[Dict]格式
        result = df.to_dict(orient="records")
        
        # 处理可能的NaN值
        for item in result:
            for key, value in item.items():
                if pd.isna(value):
                    item[key] = None
                    
        return result
    except Exception as e:
        raise Exception(f"Failed to fetch dividend data for {symbol}: {str(e)}")

def test():
    """
    同步测试方法, 用于自动化测试
    
    Raises:
        Exception: 当execute方法执行失败时抛出异常
    """
    # 使用示例中的测试参数
    test_symbol = "600009"
    try:
        result = asyncio.run(execute(symbol=test_symbol))
        print(f"Test executed successfully. Got {len(result)} records.")
    except Exception as e:
        print(f"Test failed: {str(e)}")
        raise

if __name__ == "__main__":
    # 演示如何调用异步函数
    async def main():
        try:
            data = await execute(symbol="600009")
            print(f"Got {len(data)} dividend records:")
            for item in data[:3]:  # 打印前3条记录
                print(item)
        except Exception as e:
            print(f"Error: {str(e)}")
    
    asyncio.run(main())