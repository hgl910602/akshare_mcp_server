import asyncio
from typing import List, Dict, Any
import akshare as ak
import pandas as pd

async def execute() -> List[Dict[str, Any]]:
    """
    获取东方财富网美股实时行情数据
    
    Returns:
        List[Dict[str, Any]]: 美股实时行情数据列表，每个元素为一个字典代表一只股票的信息
        
    Raises:
        Exception: 当获取数据失败时抛出异常
    """
    try:
        # 调用akshare接口获取美股实时行情数据
        df = ak.stock_us_spot_em()
        
        # 将DataFrame转换为List[Dict]格式
        result = df.to_dict(orient='records')
        
        return result
    except Exception as e:
        raise Exception(f"获取美股实时行情数据失败: {str(e)}")

def test() -> List[Dict[str, Any]]:
    """
    同步测试方法，用于自动化测试
    
    Returns:
        List[Dict[str, Any]]: 美股实时行情数据列表
        
    Raises:
        Exception: 当execute方法执行失败时抛出异常
    """
    try:
        return asyncio.run(execute())
    except Exception as e:
        raise Exception(f"测试美股实时行情数据失败: {str(e)}")

if __name__ == '__main__':
    # 演示如何调用异步函数获取美股实时行情数据
    async def main():
        try:
            data = await execute()
            print(f"获取到 {len(data)} 条美股实时行情数据")
            if len(data) > 0:
                print("第一条数据示例:")
                print(data[0])
        except Exception as e:
            print(f"获取数据出错: {e}")
    
    asyncio.run(main())