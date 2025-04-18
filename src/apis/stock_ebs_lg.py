import asyncio
from typing import List, Dict, Any
import akshare as ak
import pandas as pd

async def execute() -> List[Dict[str, Any]]:
    """
    异步获取乐咕乐股-股债利差数据
    
    Returns:
        List[Dict[str, Any]]: 转换后的股债利差数据列表
    """
    try:
        # 调用akshare接口获取数据
        df = ak.stock_ebs_lg()
        
        # 将DataFrame转换为List[Dict]格式
        result = df.to_dict(orient='records')
        return result
    except Exception as e:
        raise Exception(f"获取股债利差数据失败: {str(e)}")

def test() -> List[Dict[str, Any]]:
    """
    同步测试方法，用于验证execute函数
    
    Returns:
        List[Dict[str, Any]]: 股债利差数据
        
    Raises:
        Exception: 当execute执行出错时抛出
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
            print(data[:5])  # 打印前5条数据
        except Exception as e:
            print(f"Error: {e}")
    
    asyncio.run(main())