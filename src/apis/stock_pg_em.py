import asyncio
from typing import List, Dict, Any
import akshare as ak
import pandas as pd

async def execute() -> List[Dict[str, Any]]:
    """
    获取东方财富网-数据中心-新股数据-配股信息
    
    Returns:
        List[Dict[str, Any]]: 配股信息列表，每个元素为一个字典，包含股票代码、简称等信息
        
    Raises:
        Exception: 当获取数据失败时抛出异常
    """
    try:
        # 调用akshare接口获取数据
        df = ak.stock_pg_em()
        
        # 将DataFrame转换为List[Dict]格式
        result = df.to_dict(orient='records')
        
        # 处理可能的NaN值
        for item in result:
            for key, value in item.items():
                if pd.isna(value):
                    item[key] = None
        
        return result
    except Exception as e:
        raise Exception(f"获取配股数据失败: {str(e)}")

def test() -> List[Dict[str, Any]]:
    """
    同步测试方法，用于自动化测试
    
    Returns:
        List[Dict[str, Any]]: 配股信息列表
        
    Raises:
        Exception: 当execute方法执行失败时抛出异常
    """
    try:
        return asyncio.run(execute())
    except Exception as e:
        raise Exception(f"测试获取配股数据失败: {str(e)}")

if __name__ == '__main__':
    # 演示如何调用异步函数
    async def main():
        try:
            data = await execute()
            print(f"获取到{len(data)}条配股数据")
            if len(data) > 0:
                print("第一条数据示例:")
                print(data[0])
        except Exception as e:
            print(f"发生错误: {str(e)}")
    
    asyncio.run(main())