import asyncio
from typing import List, Dict, Any
import akshare as ak
import pandas as pd

async def execute() -> List[Dict[str, Any]]:
    """
    获取美股粉单市场的实时行情数据
    
    Returns:
        List[Dict[str, Any]]: 美股粉单市场行情数据列表，每个元素是一个字典代表一只股票的信息
        
    Raises:
        Exception: 当获取数据失败时抛出异常
    """
    try:
        # 调用akshare接口获取数据
        df = ak.stock_us_pink_spot_em()
        
        # 将DataFrame转换为List[Dict]格式
        result = df.to_dict(orient='records')
        return result
    except Exception as e:
        raise Exception(f"Failed to fetch stock_us_pink_spot_em data: {str(e)}")

def test() -> List[Dict[str, Any]]:
    """
    同步测试方法，用于自动化测试
    
    Returns:
        List[Dict[str, Any]]: 美股粉单市场行情数据
        
    Raises:
        Exception: 当execute方法执行失败时抛出异常
    """
    try:
        return asyncio.run(execute())
    except Exception as e:
        raise Exception(f"Test failed: {str(e)}")

if __name__ == '__main__':
    # 演示如何异步调用该函数
    async def main():
        try:
            data = await execute()
            print(f"获取到{len(data)}条美股粉单市场数据:")
            for item in data[:3]:  # 打印前3条数据作为示例
                print(item)
        except Exception as e:
            print(f"Error: {str(e)}")
    
    asyncio.run(main())