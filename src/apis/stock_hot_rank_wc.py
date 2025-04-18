import asyncio
from typing import List, Dict, Any
import akshare as ak
import pandas as pd

async def execute(date: str = "20240920") -> List[Dict[str, Any]]:
    """
    异步获取问财-热门股票排名数据
    
    Args:
        date: 查询日期，格式为YYYYMMDD
        
    Returns:
        返回处理后的股票热度排名数据列表
        
    Raises:
        Exception: 当接口调用或数据处理出错时抛出
    """
    try:
        # 调用akshare接口获取数据
        df = ak.stock_hot_rank_wc(date=date)
        
        # 处理数据为List[Dict]格式
        result = []
        if not df.empty:
            # 替换NaN为None
            df = df.where(pd.notnull(df), None)
            # 转换每一行为字典
            result = df.to_dict(orient="records")
        return result
    except Exception as e:
        raise Exception(f"获取股票热度排名数据失败: {e}")

def test():
    """
    同步测试方法，用于自动化测试
    
    Returns:
        返回execute方法的执行结果
        
    Raises:
        直接抛出execute方法中的异常
    """
    return asyncio.run(execute(date="20240920"))

if __name__ == "__main__":
    # 演示如何调用异步函数
    async def main():
        try:
            data = await execute(date="20240920")
            print(data)
        except Exception as e:
            print(f"Error: {e}")
    
    asyncio.run(main())