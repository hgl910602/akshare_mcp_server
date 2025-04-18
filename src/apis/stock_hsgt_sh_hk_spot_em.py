import asyncio
from typing import List, Dict, Any
import akshare as ak
import pandas as pd

async def execute() -> List[Dict[str, Any]]:
    """
    获取东方财富网-行情中心-沪深港通-港股通(沪>港)-股票实时行情数据
    
    Returns:
        List[Dict[str, Any]]: 返回港股通(沪>港)实时行情数据列表，每个元素为一个字典代表一行数据
        
    Raises:
        Exception: 当获取数据失败时抛出异常
    """
    try:
        # 调用akshare接口获取数据
        df = ak.stock_hsgt_sh_hk_spot_em()
        
        # 将DataFrame转换为List[Dict]格式
        result = df.to_dict(orient='records')
        
        return result
    except Exception as e:
        raise Exception(f"获取港股通(沪>港)实时行情数据失败: {str(e)}")

def test() -> List[Dict[str, Any]]:
    """
    同步测试方法，用于自动化测试
    
    Returns:
        List[Dict[str, Any]]: 返回港股通(沪>港)实时行情数据列表
        
    Raises:
        Exception: 当execute方法执行失败时抛出异常
    """
    try:
        return asyncio.run(execute())
    except Exception as e:
        raise Exception(f"测试执行失败: {str(e)}")

if __name__ == '__main__':
    # 演示如何调用异步函数并打印结果
    async def main():
        try:
            data = await execute()
            print(f"获取到 {len(data)} 条港股通(沪>港)实时行情数据:")
            for item in data[:5]:  # 打印前5条数据
                print(item)
        except Exception as e:
            print(f"执行出错: {str(e)}")
    
    asyncio.run(main())