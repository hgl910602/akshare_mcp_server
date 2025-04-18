import asyncio
from typing import List, Dict, Any
import akshare as ak
import pandas as pd

async def execute(market: str = "北向持股", start_date: str = "20201218", end_date: str = "20201218") -> List[Dict[str, Any]]:
    """
    异步获取东方财富网-沪深港通持股-机构排行数据
    
    Args:
        market: 市场类型，可选 {"北向持股", "沪股通持股", "深股通持股", "南向持股"}
        start_date: 开始日期，格式如 "20201218"
        end_date: 结束日期，格式如 "20201218"
    
    Returns:
        机构排行数据列表，每个机构信息以字典形式存储
    
    Raises:
        Exception: 当获取数据失败时抛出异常
    """
    try:
        # 调用akshare同步接口，使用await在异步环境中执行
        df = await asyncio.get_event_loop().run_in_executor(
            None,
            lambda: ak.stock_hsgt_institution_statistics_em(
                market=market,
                start_date=start_date,
                end_date=end_date
            )
        )
        
        # 将DataFrame转换为List[Dict]格式
        if not df.empty:
            return df.to_dict(orient="records")
        return []
    except Exception as e:
        raise Exception(f"获取沪深港通机构排行数据失败: {str(e)}")

def test():
    """
    同步测试方法，用于自动化测试
    
    Raises:
        Exception: 当execute方法执行失败时抛出异常
    """
    try:
        result = asyncio.run(execute(
            market="北向持股",
            start_date="20201218",
            end_date="20201218"
        ))
        print("测试成功，返回数据条数:", len(result))
    except Exception as e:
        raise Exception(f"测试失败: {str(e)}")

if __name__ == "__main__":
    # 演示如何调用异步函数并打印结果
    async def main():
        try:
            data = await execute(
                market="北向持股",
                start_date="20201218",
                end_date="20201218"
            )
            print("获取到的机构排行数据:")
            for item in data[:5]:  # 打印前5条记录
                print(item)
        except Exception as e:
            print(f"执行出错: {str(e)}")
    
    asyncio.run(main())