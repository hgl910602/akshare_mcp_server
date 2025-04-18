import asyncio
from typing import List, Dict, Any
import akshare as ak
import pandas as pd

async def execute(start_date: str, end_date: str) -> List[Dict[str, Any]]:
    """
    异步获取东方财富网-数据中心-限售股解禁-解禁详情一览数据
    
    Args:
        start_date: 开始日期, 格式为YYYYMMDD
        end_date: 结束日期, 格式为YYYYMMDD
        
    Returns:
        限售解禁详情数据列表
        
    Raises:
        Exception: 当获取数据失败时抛出异常
    """
    try:
        # 调用akshare同步接口获取数据
        df = ak.stock_restricted_release_detail_em(start_date=start_date, end_date=end_date)
        
        # 将DataFrame转换为List[Dict]格式
        if not df.empty:
            # 处理可能的NaN值
            df = df.fillna(0)
            return df.to_dict("records")
        return []
    except Exception as e:
        raise Exception(f"获取限售解禁数据失败: {e}")

def test():
    """
    同步测试方法，用于自动化测试
    
    Returns:
        限售解禁详情数据列表
        
    Raises:
        原样抛出execute方法中的异常
    """
    start_date = "20221202"
    end_date = "20221204"
    return asyncio.run(execute(start_date=start_date, end_date=end_date))

if __name__ == "__main__":
    # 演示如何调用异步函数
    async def main():
        try:
            data = await execute(start_date="20221202", end_date="20221204")
            for item in data:
                print(item)
        except Exception as e:
            print(f"发生错误: {e}")
    
    asyncio.run(main())