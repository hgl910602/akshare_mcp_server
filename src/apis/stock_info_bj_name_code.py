import asyncio
from typing import List, Dict, Any
import akshare as ak
import pandas as pd

async def execute() -> List[Dict[str, Any]]:
    """
    异步获取北京证券交易所股票代码和简称数据
    
    Returns:
        List[Dict[str, Any]]: 北证股票信息列表，每个元素为包含股票信息的字典
        
    Raises:
        Exception: 当数据获取失败时抛出异常
    """
    try:
        # 调用akshare接口获取数据
        df = ak.stock_info_bj_name_code()
        
        # 将DataFrame转换为List[Dict]格式
        result = df.to_dict(orient='records')
        return result
    except Exception as e:
        raise Exception(f"获取北证股票信息失败: {str(e)}")

def test() -> List[Dict[str, Any]]:
    """
    同步测试方法，用于自动化测试
    
    Returns:
        List[Dict[str, Any]]: 北证股票信息列表
        
    Raises:
        Exception: 当数据获取失败时抛出异常
    """
    try:
        return asyncio.run(execute())
    except Exception as e:
        raise e

if __name__ == '__main__':
    # 演示如何调用异步函数
    async def main():
        try:
            data = await execute()
            print(f"获取到{len(data)}条北证股票信息")
            for item in data[:5]:  # 打印前5条记录
                print(item)
        except Exception as e:
            print(f"发生错误: {e}")
    
    asyncio.run(main())