import asyncio
from typing import List, Dict, Any
import akshare as ak
import pandas as pd

async def execute() -> List[Dict[str, Any]]:
    """
    获取同花顺-数据中心-资金流向-大单追踪数据
    
    Returns:
        List[Dict[str, Any]]: 大单追踪数据列表，每个元素为一条大单记录
        
    Raises:
        Exception: 当获取数据失败时抛出异常
    """
    try:
        # 调用akshare接口获取数据
        df = ak.stock_fund_flow_big_deal()
        
        # 将DataFrame转换为List[Dict]格式
        result = df.to_dict(orient='records')
        return result
    except Exception as e:
        raise Exception(f"获取大单追踪数据失败: {str(e)}")

def test() -> List[Dict[str, Any]]:
    """
    同步测试方法，用于自动化测试
    
    Returns:
        List[Dict[str, Any]]: 大单追踪数据列表
        
    Raises:
        原样抛出execute方法中的异常
    """
    return asyncio.run(execute())

if __name__ == '__main__':
    # 异步调用示例
    async def main():
        try:
            data = await execute()
            for item in data[:5]:  # 打印前5条记录
                print(item)
        except Exception as e:
            print(f"Error: {e}")
    
    asyncio.run(main())