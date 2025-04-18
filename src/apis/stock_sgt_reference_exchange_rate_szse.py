import asyncio
from typing import List, Dict, Any
import akshare as ak
import pandas as pd

async def execute() -> List[Dict[str, Any]]:
    """
    异步获取深港通-港股通业务信息-参考汇率数据
    
    Returns:
        List[Dict[str, Any]]: 返回处理后的参考汇率数据列表
        
    Raises:
        Exception: 当获取数据或处理数据过程中出现错误时抛出异常
    """
    try:
        # 调用akshare接口获取数据
        df = ak.stock_sgt_reference_exchange_rate_szse()
        
        # 将DataFrame转换为List[Dict]格式
        result = df.to_dict(orient='records')
        
        return result
    except Exception as e:
        raise Exception(f"获取深港通参考汇率数据失败: {str(e)}")

def test() -> List[Dict[str, Any]]:
    """
    同步测试方法，用于自动化测试
    
    Returns:
        List[Dict[str, Any]]: 返回处理后的参考汇率数据列表
        
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
            print("深港通参考汇率数据:")
            for item in data:
                print(item)
        except Exception as e:
            print(f"发生错误: {e}")
    
    asyncio.run(main())