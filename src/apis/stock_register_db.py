import asyncio
from typing import List, Dict, Any
import akshare as ak
import pandas as pd

async def execute() -> List[Dict[str, Any]]:
    """
    获取东方财富网-数据中心-新股数据-注册制审核-达标企业数据
    
    Returns:
        List[Dict[str, Any]]: 返回注册制审核达标企业数据列表
    """
    try:
        # 调用akshare接口获取数据
        df = ak.stock_register_db()
        
        # 将DataFrame转换为List[Dict]格式
        result = df.to_dict(orient='records')
        
        return result
    except Exception as e:
        raise Exception(f"获取注册制审核达标企业数据失败: {e}")

def test() -> List[Dict[str, Any]]:
    """
    同步测试方法，用于自动化测试
    
    Returns:
        List[Dict[str, Any]]: 返回注册制审核达标企业数据列表
        
    Raises:
        Exception: 当execute方法执行失败时抛出异常
    """
    try:
        return asyncio.run(execute())
    except Exception as e:
        raise Exception(f"测试获取注册制审核达标企业数据失败: {e}")

if __name__ == '__main__':
    # 演示如何调用异步函数
    async def main():
        try:
            data = await execute()
            print(f"获取到{len(data)}条注册制审核达标企业数据")
            if len(data) > 0:
                print("第一条数据示例:")
                print(data[0])
        except Exception as e:
            print(f"获取数据出错: {e}")
    
    asyncio.run(main())