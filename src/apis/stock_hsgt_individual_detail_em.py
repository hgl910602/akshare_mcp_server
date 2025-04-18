import asyncio
from typing import List, Dict, Any
import akshare as ak
import pandas as pd

async def execute(symbol: str, start_date: str, end_date: str) -> List[Dict[str, Any]]:
    """
    异步获取东方财富网-数据中心-沪深港通-沪深港通持股-具体股票-个股详情数据
    
    Args:
        symbol: 股票代码，如 "002008"
        start_date: 开始日期，格式 "YYYYMMDD"
        end_date: 结束日期，格式 "YYYYMMDD"
    
    Returns:
        返回处理后的数据列表，每个元素为字典形式
        
    Raises:
        Exception: 当akshare接口调用失败时抛出异常
    """
    try:
        # 调用akshare接口获取数据
        df = ak.stock_hsgt_individual_detail_em(
            symbol=symbol,
            start_date=start_date,
            end_date=end_date
        )
        
        # 将DataFrame转换为List[Dict]格式
        if not df.empty:
            # 处理可能的NaN值
            df = df.fillna(0)
            # 转换日期列为字符串格式
            if '持股日期' in df.columns:
                df['持股日期'] = df['持股日期'].astype(str)
            return df.to_dict('records')
        return []
    except Exception as e:
        raise Exception(f"获取沪深港通个股详情数据失败: {str(e)}")

def test():
    """
    同步测试方法，用于自动化测试
    
    Returns:
        返回execute方法的执行结果
        
    Raises:
        直接抛出execute方法可能产生的异常
    """
    # 使用示例参数调用
    return asyncio.run(execute(
        symbol="002008",
        start_date="20210830",
        end_date="20211026"
    ))

if __name__ == '__main__':
    # 演示如何调用异步函数
    async def main():
        try:
            data = await execute(
                symbol="002008",
                start_date="20210830",
                end_date="20211026"
            )
            print(data)  # 打印获取的数据
        except Exception as e:
            print(f"Error: {e}")
    
    asyncio.run(main())