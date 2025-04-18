import asyncio
from typing import Any, Dict, List
import akshare as ak
import pandas as pd

async def execute() -> List[Dict[str, Any]]:
    """
    获取东方财富网-数据中心-新股数据-增发-全部增发数据
    
    Returns:
        List[Dict[str, Any]]: 返回全部增发数据列表，每个元素为字典形式的数据
        
    Raises:
        Exception: 当获取数据失败时抛出异常
    """
    try:
        # 调用akshare接口获取数据
        df = ak.stock_qbzf_em()
        
        # 处理空数据情况
        if df.empty:
            return []
            
        # 转换DataFrame为List[Dict]格式
        result = df.to_dict(orient='records')
        return result
    except Exception as e:
        raise Exception(f"获取增发数据失败: {str(e)}")

def test() -> List[Dict[str, Any]]:
    """
    同步测试方法，用于自动化测试
    
    Returns:
        List[Dict[str, Any]]: 返回全部增发数据列表
        
    Raises:
        原样抛出execute方法中的异常
    """
    return asyncio.run(execute())

if __name__ == '__main__':
    # 演示如何调用异步函数
    async def main():
        try:
            data = await execute()
            print(f"获取到{len(data)}条增发数据")
            if data:
                print("第一条数据示例:")
                print(data[0])
        except Exception as e:
            print(f"获取数据出错: {e}")
    
    asyncio.run(main())