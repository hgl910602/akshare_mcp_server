import asyncio
from typing import List, Dict, Any
import akshare as ak
import pandas as pd

async def execute(indicator: str = "今日", sector_type: str = "行业资金流") -> List[Dict[str, Any]]:
    """
    东方财富网-数据中心-资金流向-板块资金流-排名
    
    Args:
        indicator: choice of {"今日", "5日", "10日"}
        sector_type: choice of {"行业资金流", "概念资金流", "地域资金流"}
    
    Returns:
        List[Dict[str, Any]]: 板块资金流排名数据
    
    Raises:
        Exception: 当获取数据失败时抛出异常
    """
    try:
        # 调用akshare同步接口
        df = ak.stock_sector_fund_flow_rank(indicator=indicator, sector_type=sector_type)
        
        # 将DataFrame转换为List[Dict]
        result = df.to_dict(orient="records")
        return result
    except Exception as e:
        raise Exception(f"获取板块资金流排名数据失败: {str(e)}")

def test():
    """
    同步测试方法，用于自动化测试
    
    Returns:
        List[Dict[str, Any]]: 板块资金流排名数据
    
    Raises:
        Exception: 当execute方法执行失败时抛出异常
    """
    try:
        # 使用asyncio.run调用异步方法
        result = asyncio.run(execute(indicator="今日", sector_type="行业资金流"))
        return result
    except Exception as e:
        raise Exception(f"测试execute方法失败: {str(e)}")

if __name__ == "__main__":
    # 演示如何调用异步execute方法
    async def main():
        try:
            data = await execute(indicator="今日", sector_type="行业资金流")
            print(data[:2])  # 打印前两条数据示例
        except Exception as e:
            print(f"执行失败: {e}")
    
    asyncio.run(main())