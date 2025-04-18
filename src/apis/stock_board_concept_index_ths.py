import asyncio
from typing import List, Dict, Any
import akshare as ak
import pandas as pd

async def execute(symbol: str, start_date: str, end_date: str) -> List[Dict[str, Any]]:
    """
    异步获取同花顺概念板块指数数据
    
    Args:
        symbol: 概念板块名称，如"阿里巴巴概念"
        start_date: 开始日期，格式"YYYYMMDD"
        end_date: 结束日期，格式"YYYYMMDD"
    
    Returns:
        概念板块指数数据列表，每个元素为包含日期和价格等信息的字典
    
    Raises:
        Exception: 当获取数据失败时抛出异常
    """
    try:
        # 调用akshare同步接口获取数据
        df = ak.stock_board_concept_index_ths(symbol=symbol, start_date=start_date, end_date=end_date)
        
        # 将DataFrame转换为List[Dict]格式
        result = df.to_dict(orient='records')
        return result
    except Exception as e:
        raise Exception(f"获取概念板块指数数据失败: {str(e)}")

def test():
    """
    同步测试方法，用于自动化测试
    
    Returns:
        概念板块指数数据列表
    
    Raises:
        原样抛出execute方法中的异常
    """
    # 使用示例中的参数进行测试
    symbol = "阿里巴巴概念"
    start_date = "20200101"
    end_date = "20250321"
    
    try:
        # 异步调用execute方法
        result = asyncio.run(execute(symbol=symbol, start_date=start_date, end_date=end_date))
        return result
    except Exception as e:
        raise

if __name__ == '__main__':
    # 演示如何调用异步函数
    async def main():
        try:
            data = await execute(symbol="阿里巴巴概念", start_date="20200101", end_date="20250321")
            print(data[:5])  # 打印前5条数据
        except Exception as e:
            print(f"Error: {e}")
    
    asyncio.run(main())