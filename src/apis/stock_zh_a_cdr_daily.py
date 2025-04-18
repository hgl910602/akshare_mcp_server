import asyncio
from typing import List, Dict, Any
import akshare as ak
import pandas as pd

async def execute(symbol: str, start_date: str, end_date: str) -> List[Dict[str, Any]]:
    """
    异步获取上海证券交易所-科创板-CDR历史行情数据
    
    Args:
        symbol: CDR股票代码，如'sh689009'
        start_date: 开始日期，格式'YYYYMMDD'
        end_date: 结束日期，格式'YYYYMMDD'
    
    Returns:
        返回包含历史行情数据的字典列表
    
    Raises:
        Exception: 当获取数据失败时抛出异常
    """
    try:
        # 调用akshare同步接口获取数据
        df = ak.stock_zh_a_cdr_daily(symbol=symbol, start_date=start_date, end_date=end_date)
        
        # 将DataFrame转换为字典列表
        if not df.empty:
            # 重置索引并将日期列转为字符串
            df = df.reset_index()
            df['date'] = df['date'].astype(str)
            return df.to_dict('records')
        return []
    except Exception as e:
        raise Exception(f"Failed to fetch CDR daily data: {str(e)}")

def test():
    """
    同步测试方法，用于自动化测试
    
    Raises:
        Exception: 当execute方法执行失败时抛出异常
    """
    try:
        # 使用示例参数调用execute方法
        result = asyncio.run(execute(symbol='sh689009', start_date='20201103', end_date='20201116'))
        print("Test executed successfully")
        return result
    except Exception as e:
        print(f"Test failed: {str(e)}")
        raise

if __name__ == '__main__':
    # 演示如何调用异步函数并打印结果
    async def main():
        try:
            data = await execute(symbol='sh689009', start_date='20201103', end_date='20201116')
            print("Fetched data:")
            for item in data:
                print(item)
        except Exception as e:
            print(f"Error in main: {str(e)}")
    
    asyncio.run(main())