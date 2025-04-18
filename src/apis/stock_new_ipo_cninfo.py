import asyncio
from typing import List, Dict, Any
import akshare as ak
import pandas as pd

async def execute() -> List[Dict[str, Any]]:
    """
    异步获取巨潮资讯-数据中心-新股数据-新股发行数据
    
    Returns:
        List[Dict[str, Any]]: 新股发行数据列表，每个字典代表一条新股数据
        
    Raises:
        Exception: 当数据获取失败时抛出异常
    """
    try:
        # 调用akshare接口获取数据
        df = ak.stock_new_ipo_cninfo()
        
        # 将DataFrame转换为List[Dict]格式
        if not df.empty:
            # 处理可能的NaN值
            df = df.where(pd.notnull(df), None)
            return df.to_dict(orient='records')
        return []
    except Exception as e:
        raise Exception(f"Failed to fetch stock new IPO data: {str(e)}")

def test() -> List[Dict[str, Any]]:
    """
    同步测试方法，用于自动化测试
    
    Returns:
        List[Dict[str, Any]]: 新股发行数据列表
        
    Raises:
        Exception: 当execute方法执行失败时抛出异常
    """
    try:
        return asyncio.run(execute())
    except Exception as e:
        raise Exception(f"Test failed: {str(e)}")

if __name__ == '__main__':
    # 演示如何调用异步函数
    async def main():
        try:
            data = await execute()
            print(f"Fetched {len(data)} IPO records")
            if data:
                print("Sample record:")
                print(data[0])
        except Exception as e:
            print(f"Error: {str(e)}")
    
    asyncio.run(main())