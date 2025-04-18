import asyncio
from typing import List, Dict, Any
import akshare as ak
import pandas as pd

async def execute(
    symbol: str,
    period: str = 'daily',
    start_date: str = "19700101",
    end_date: str = "22220101",
    adjust: str = "",
) -> List[Dict[str, Any]]:
    """
    异步获取港股历史行情数据
    
    Args:
        symbol: 港股代码
        period: 周期, 可选 daily, weekly, monthly
        start_date: 开始日期
        end_date: 结束日期
        adjust: 复权类型, ""(不复权), "qfq"(前复权), "hfq"(后复权)
    
    Returns:
        返回包含历史行情数据的字典列表
    
    Raises:
        Exception: 当获取数据失败时抛出异常
    """
    try:
        # 调用akshare同步接口获取数据
        df = ak.stock_hk_hist(
            symbol=symbol,
            period=period,
            start_date=start_date,
            end_date=end_date,
            adjust=adjust
        )
        
        # 将DataFrame转换为字典列表
        if not df.empty:
            # 转换日期列为字符串格式
            df['日期'] = df['日期'].astype(str)
            return df.to_dict('records')
        return []
    except Exception as e:
        raise Exception(f"获取港股历史行情数据失败: {e}")

def test():
    """
    同步测试方法，用于自动化测试
    
    Raises:
        Exception: 当execute方法执行失败时抛出异常
    """
    try:
        result = asyncio.run(execute(
            symbol="00593",
            period="daily",
            start_date="20200101",
            end_date="20201231",
            adjust="hfq"
        ))
        print(f"测试成功，获取到{len(result)}条数据")
    except Exception as e:
        raise Exception(f"测试失败: {e}")

if __name__ == '__main__':
    # 演示如何调用异步函数
    async def main():
        try:
            data = await execute(
                symbol="00593",
                period="daily",
                start_date="20200101",
                end_date="20201231",
                adjust="hfq"
            )
            print(f"获取到{len(data)}条数据")
            if data:
                print("第一条数据:", data[0])
        except Exception as e:
            print(f"执行出错: {e}")
    
    asyncio.run(main())