import asyncio
from typing import List, Dict, Any
import akshare as ak
import pandas as pd

async def execute(
    symbol: str,
    period: str = '5',
    adjust: str = '',
    start_date: str = "1979-09-01 09:32:00",
    end_date: str = "2222-01-01 09:32:00"
) -> List[Dict[str, Any]]:
    """
    获取港股分时行情数据
    
    Args:
        symbol: 港股代码
        period: 分时周期，可选 {'1', '5', '15', '30', '60'}
        adjust: 复权类型，可选 {'', 'qfq', 'hfq'}
        start_date: 开始日期时间
        end_date: 结束日期时间
    
    Returns:
        港股分时行情数据列表
    
    Raises:
        Exception: 获取数据失败时抛出异常
    """
    try:
        # 调用akshare接口获取数据
        df = ak.stock_hk_hist_min_em(
            symbol=symbol,
            period=period,
            adjust=adjust,
            start_date=start_date,
            end_date=end_date
        )
        
        # 将DataFrame转换为List[Dict]格式
        result = df.to_dict(orient='records')
        return result
    except Exception as e:
        raise Exception(f"获取港股分时行情数据失败: {str(e)}")

def test():
    """
    同步测试方法，用于自动化测试
    
    Raises:
        Exception: 执行失败时抛出异常
    """
    try:
        # 使用示例参数调用execute方法
        result = asyncio.run(execute(
            symbol="01611",
            period='5',
            adjust='hfq',
            start_date="2021-09-01 09:32:00",
            end_date="2021-09-07 18:32:00"
        ))
        print(result)
    except Exception as e:
        raise Exception(f"测试执行失败: {str(e)}")

if __name__ == '__main__':
    # 演示如何调用异步函数并打印结果
    async def main():
        try:
            data = await execute(
                symbol="01611",
                period='5',
                adjust='hfq',
                start_date="2021-09-01 09:32:00",
                end_date="2021-09-07 18:32:00"
            )
            print(data)
        except Exception as e:
            print(f"执行出错: {str(e)}")
    
    asyncio.run(main())