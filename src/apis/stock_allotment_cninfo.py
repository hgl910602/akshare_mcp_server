import asyncio
from typing import List, Dict, Any
import akshare as ak
import pandas as pd

async def execute(symbol: str, start_date: str, end_date: str) -> List[Dict[str, Any]]:
    """
    异步获取巨潮资讯-个股-配股实施方案数据
    
    Args:
        symbol: 股票代码，如 "600030"
        start_date: 开始日期，格式 "YYYYMMDD"
        end_date: 结束日期，格式 "YYYYMMDD"
        
    Returns:
        配股实施方案数据列表，每个元素为字典格式
        
    Raises:
        Exception: 当akshare接口调用失败时抛出
    """
    try:
        # 调用akshare接口获取数据
        df = ak.stock_allotment_cninfo(symbol=symbol, start_date=start_date, end_date=end_date)
        
        # 处理空数据情况
        if df.empty:
            return []
            
        # 转换DataFrame为List[Dict]格式
        result = df.to_dict(orient='records')
        return result
    except Exception as e:
        raise Exception(f"获取配股实施方案数据失败: {str(e)}")

def test():
    """
    同步测试方法，用于自动化测试
    
    Raises:
        直接抛出execute方法中的异常
    """
    # 使用示例参数进行测试
    symbol = "600030"
    start_date = "19900101"
    end_date = "20241022"
    
    # 调用异步方法
    result = asyncio.run(execute(symbol=symbol, start_date=start_date, end_date=end_date))
    return result

if __name__ == '__main__':
    # 演示如何调用异步函数
    async def main():
        try:
            data = await execute(symbol="600030", start_date="19900101", end_date="20241022")
            for item in data:
                print(item)
        except Exception as e:
            print(f"Error: {e}")
    
    asyncio.run(main())