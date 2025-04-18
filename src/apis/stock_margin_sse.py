import asyncio
from typing import List, Dict, Any
import akshare as ak
import pandas as pd

async def execute(start_date: str, end_date: str) -> List[Dict[str, Any]]:
    """
    异步获取上海证券交易所融资融券汇总数据
    
    Args:
        start_date: 开始日期，格式为"YYYYMMDD"
        end_date: 结束日期，格式为"YYYYMMDD"
        
    Returns:
        融资融券数据列表，每个元素为一个字典，包含各字段数据
        
    Raises:
        Exception: 当akshare接口调用失败时抛出异常
    """
    try:
        # 调用akshare接口获取数据
        df = ak.stock_margin_sse(start_date=start_date, end_date=end_date)
        
        # 将DataFrame转换为List[Dict]格式
        result = []
        for _, row in df.iterrows():
            record = {
                "信用交易日期": str(row["信用交易日期"]),
                "融资余额": int(row["融资余额"]),
                "融资买入额": int(row["融资买入额"]),
                "融券余量": int(row["融券余量"]),
                "融券余量金额": int(row["融券余量金额"]),
                "融券卖出量": int(row["融券卖出量"]),
                "融资融券余额": int(row["融资融券余额"]),
            }
            result.append(record)
            
        return result
    except Exception as e:
        raise Exception(f"获取上海证券交易所融资融券数据失败: {str(e)}")

def test():
    """
    同步测试方法，用于自动化测试
    
    Raises:
        任何execute方法可能抛出的异常
    """
    # 使用示例中的参数进行测试
    start_date = "20010106"
    end_date = "20210208"
    
    # 异步调用execute方法
    result = asyncio.run(execute(start_date=start_date, end_date=end_date))
    return result

if __name__ == "__main__":
    # 演示如何调用异步函数
    async def main():
        try:
            # 使用示例参数调用
            data = await execute(start_date="20010106", end_date="20210208")
            # 打印结果
            for item in data[:5]:  # 只打印前5条记录
                print(item)
        except Exception as e:
            print(f"Error: {e}")
    
    # 运行主函数
    asyncio.run(main())