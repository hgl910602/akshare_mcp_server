import asyncio
from typing import List, Dict, Any
import akshare as ak
import pandas as pd

async def execute() -> List[Dict[str, Any]]:
    """
    获取同花顺-数据中心-技术选股-连续下跌数据
    
    Returns:
        List[Dict[str, Any]]: 返回连续下跌股票数据的字典列表
        
    Raises:
        Exception: 当获取数据失败时抛出异常
    """
    try:
        # 调用akshare接口获取数据
        df = ak.stock_rank_lxxd_ths()
        
        # 将DataFrame转换为字典列表
        result = df.to_dict(orient='records')
        
        return result
    except Exception as e:
        raise Exception(f"获取连续下跌股票数据失败: {e}")

def test() -> List[Dict[str, Any]]:
    """
    同步测试方法，用于自动化测试
    
    Returns:
        List[Dict[str, Any]]: 返回连续下跌股票数据的字典列表
        
    Raises:
        Exception: 当execute方法执行失败时抛出异常
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
            print("获取连续下跌股票数据成功:")
            for item in data[:5]:  # 打印前5条数据
                print(item)
        except Exception as e:
            print(f"获取数据时出错: {e}")
    
    asyncio.run(main())