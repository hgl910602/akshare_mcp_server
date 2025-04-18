import asyncio
from typing import List, Dict, Any
import akshare as ak
import pandas as pd

async def execute() -> List[Dict[str, Any]]:
    """
    东方财富网-数据中心-特色数据-股权质押-质押机构分布统计-证券公司
    返回: 质押机构分布统计数据的字典列表
    """
    try:
        # 调用akshare接口获取数据
        df = ak.stock_gpzy_distribute_statistics_company_em()
        
        # 将DataFrame转换为字典列表
        result = df.to_dict(orient='records')
        return result
    except Exception as e:
        raise Exception(f"获取股票质押机构分布统计数据失败: {e}")

def test() -> List[Dict[str, Any]]:
    """
    同步测试方法，用于自动化测试
    返回: 质押机构分布统计数据的字典列表
    """
    try:
        return asyncio.run(execute())
    except Exception as e:
        raise e

if __name__ == '__main__':
    # 异步调用示例
    async def main():
        try:
            data = await execute()
            print(data)
        except Exception as e:
            print(f"Error: {e}")
    
    asyncio.run(main())