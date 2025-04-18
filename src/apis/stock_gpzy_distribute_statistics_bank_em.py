import asyncio
from typing import List, Dict, Any
import akshare as ak
import pandas as pd

async def execute() -> List[Dict[str, Any]]:
    """
    获取东方财富网-数据中心-特色数据-股权质押-质押机构分布统计-银行数据
    
    Returns:
        List[Dict[str, Any]]: 返回质押机构分布统计数据的字典列表
        
    Raises:
        Exception: 当获取数据失败时抛出异常
    """
    try:
        # 调用akshare接口获取数据
        df = ak.stock_gpzy_distribute_statistics_bank_em()
        
        # 将DataFrame转换为字典列表
        result = df.to_dict(orient='records')
        
        return result
    except Exception as e:
        raise Exception(f"获取质押机构分布统计数据失败: {e}")

def test() -> List[Dict[str, Any]]:
    """
    同步测试方法，用于自动化测试
    
    Returns:
        List[Dict[str, Any]]: 返回质押机构分布统计数据的字典列表
        
    Raises:
        Exception: 当获取数据失败时抛出异常
    """
    try:
        return asyncio.run(execute())
    except Exception as e:
        raise e

if __name__ == '__main__':
    # 演示如何调用异步函数并打印结果
    async def main():
        try:
            data = await execute()
            for item in data:
                print(item)
        except Exception as e:
            print(f"发生错误: {e}")
    
    asyncio.run(main())