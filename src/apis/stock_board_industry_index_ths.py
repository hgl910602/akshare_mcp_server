import asyncio
from typing import List, Dict, Any
import akshare as ak
import pandas as pd

async def execute(symbol: str, start_date: str, end_date: str) -> List[Dict[str, Any]]:
    """
    异步获取同花顺行业板块指数数据
    
    Args:
        symbol: 行业名称，可通过 ak.stock_board_industry_name_ths() 获取
        start_date: 开始日期，格式为YYYYMMDD
        end_date: 结束日期，格式为YYYYMMDD
    
    Returns:
        行业板块指数数据列表，每个元素为一个字典代表一行数据
        
    Raises:
        Exception: 当akshare接口调用失败时抛出
    """
    try:
        # 调用akshare接口获取数据
        df = ak.stock_board_industry_index_ths(symbol=symbol, start_date=start_date, end_date=end_date)
        
        # 将DataFrame转换为List[Dict]格式
        result = df.to_dict(orient='records')
        return result
    except Exception as e:
        raise Exception(f"Failed to fetch stock board industry index: {str(e)}")

def test():
    """
    同步测试方法，用于自动化测试
    
    Raises:
        任何execute方法可能抛出的异常
    """
    # 使用示例参数调用execute方法
    result = asyncio.run(execute(symbol="元件", start_date="20240101", end_date="20240718"))
    return result

if __name__ == '__main__':
    # 演示如何调用该函数
    async def main():
        try:
            data = await execute(symbol="元件", start_date="20240101", end_date="20240718")
            print(f"获取到{len(data)}条数据")
            if data:
                print("第一条数据示例:")
                print(data[0])
        except Exception as e:
            print(f"发生错误: {e}")
    
    asyncio.run(main())