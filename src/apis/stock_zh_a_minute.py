import asyncio
from typing import List, Dict, Any
import akshare as ak
import pandas as pd

async def execute(symbol: str, period: str = '1', adjust: str = "") -> List[Dict[str, Any]]:
    """
    异步获取新浪财经-沪深京 A 股股票或者指数的分时数据
    
    Args:
        symbol: 股票或指数代码，如 'sh000300'
        period: 分钟周期，可选 '1', '5', '15', '30', '60'
        adjust: 复权类型，可选 ""(不复权), "qfq"(前复权), "hfq"(后复权)
    
    Returns:
        返回包含分时数据的字典列表
        
    Raises:
        Exception: 当获取数据失败时抛出异常
    """
    try:
        # 调用akshare同步接口获取数据
        df = ak.stock_zh_a_minute(symbol=symbol, period=period, adjust=adjust)
        
        # 将DataFrame转换为字典列表
        if not df.empty:
            # 确保列名是小写，避免不同版本akshare列名大小写不一致的问题
            df.columns = df.columns.str.lower()
            return df.to_dict('records')
        return []
    except Exception as e:
        raise Exception(f"Failed to fetch minute data for {symbol}: {str(e)}")

def test():
    """
    同步测试方法，用于验证execute函数
    
    Raises:
        直接抛出execute中可能出现的异常
    """
    try:
        # 使用示例参数调用execute
        result = asyncio.run(execute(symbol='sh600751', period='1', adjust="qfq"))
        print("Test executed successfully. Sample data:")
        if result:
            print(result[0])  # 打印第一条数据作为示例
    except Exception as e:
        print(f"Test failed: {str(e)}")
        raise

if __name__ == '__main__':
    # 演示如何调用异步函数
    async def main():
        try:
            data = await execute(symbol='sh000300', period='5')
            print(f"Fetched {len(data)} records")
            if data:
                print("Sample record:", data[0])
        except Exception as e:
            print(f"Error in main: {str(e)}")
    
    asyncio.run(main())