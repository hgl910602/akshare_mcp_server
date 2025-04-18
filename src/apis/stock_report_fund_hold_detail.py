import asyncio
from typing import List, Dict, Any
import akshare as ak
import pandas as pd

async def execute(symbol: str, date: str) -> List[Dict[str, Any]]:
    """
    异步获取基金持仓明细数据
    
    Args:
        symbol: 基金代码
        date: 财报发布日期(格式: xxxx0331, xxxx0630, xxxx0930, xxxx1231)
    
    Returns:
        基金持仓明细数据列表，每个条目为字典格式
    
    Raises:
        Exception: 当akshare接口调用失败时抛出异常
    """
    try:
        # 调用akshare接口获取数据
        df = ak.stock_report_fund_hold_detail(symbol=symbol, date=date)
        
        # 将DataFrame转换为List[Dict]格式
        if not df.empty:
            # 处理可能的NaN值
            df = df.fillna(0)
            # 转换数据类型
            df = df.astype({
                '序号': int,
                '持股数': int,
                '持股市值': float,
                '占总股本比例': float,
                '占流通股本比例': float
            })
            return df.to_dict('records')
        return []
    except Exception as e:
        raise Exception(f"获取基金持仓明细数据失败: {str(e)}")

def test():
    """
    同步测试方法，用于自动化测试
    
    Raises:
        直接抛出execute方法可能产生的异常
    """
    # 使用示例参数
    symbol = "005827"
    date = "20201231"
    
    # 异步调用execute方法
    result = asyncio.run(execute(symbol=symbol, date=date))
    return result

if __name__ == '__main__':
    # 演示如何调用异步函数
    async def main():
        try:
            data = await execute(symbol="005827", date="20201231")
            print(data[:2])  # 打印前两条记录
        except Exception as e:
            print(f"Error: {e}")
    
    asyncio.run(main())