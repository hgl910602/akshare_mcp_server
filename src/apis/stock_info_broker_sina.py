import asyncio
from typing import List, Dict, Any
import akshare as ak
import pandas as pd

async def execute(page: str = "1") -> List[Dict[str, Any]]:
    """
    异步获取新浪财经-证券-证券原创数据
    
    Args:
        page: 获取指定页面的数据，默认为"1"
        
    Returns:
        List[Dict[str, Any]]: 返回处理后的数据列表
        
    Raises:
        Exception: 当获取数据失败时抛出异常
    """
    try:
        # 调用akshare接口获取数据
        df = ak.stock_info_broker_sina(page=page)
        
        # 将DataFrame转换为List[Dict]格式
        if not df.empty:
            return df.to_dict("records")
        return []
    except Exception as e:
        raise Exception(f"Failed to fetch stock info from sina: {str(e)}")

def test():
    """
    同步测试方法，用于自动化测试
    
    Returns:
        List[Dict[str, Any]]: 返回execute方法的结果
        
    Raises:
        Exception: 当execute方法执行失败时抛出异常
    """
    try:
        # 模拟调用execute方法，使用默认参数
        result = asyncio.run(execute(page="1"))
        return result
    except Exception as e:
        raise Exception(f"Test failed: {str(e)}")

if __name__ == "__main__":
    # 演示如何调用异步函数
    async def main():
        try:
            data = await execute(page="1")
            print(data)
        except Exception as e:
            print(f"Error occurred: {e}")
    
    asyncio.run(main())