import asyncio
from typing import List, Dict, Any
import akshare as ak
import pandas as pd

async def execute() -> List[Dict[str, Any]]:
    """
    异步获取东方财富网站-股票热度数据
    
    Returns:
        List[Dict[str, Any]]: 股票热度数据列表，每个元素为包含股票信息的字典
        
    Raises:
        Exception: 当获取数据失败时抛出异常
    """
    try:
        # 调用akshare的同步接口，使用run_in_executor避免阻塞事件循环
        loop = asyncio.get_running_loop()
        df = await loop.run_in_executor(None, ak.stock_hot_rank_em)
        
        # 将DataFrame转换为List[Dict]格式
        result = df.to_dict(orient='records')
        return result
    except Exception as e:
        raise Exception(f"获取股票热度数据失败: {str(e)}")

def test() -> List[Dict[str, Any]]:
    """
    同步测试方法，用于测试execute函数
    
    Returns:
        List[Dict[str, Any]]: 股票热度数据列表
        
    Raises:
        Exception: 当execute执行失败时抛出异常
    """
    try:
        return asyncio.run(execute())
    except Exception as e:
        raise Exception(f"测试执行失败: {str(e)}")

if __name__ == '__main__':
    # 演示异步调用
    async def main():
        try:
            data = await execute()
            print("获取股票热度数据成功:")
            for item in data[:5]:  # 打印前5条数据
                print(item)
        except Exception as e:
            print(f"错误: {str(e)}")
    
    asyncio.run(main())