import asyncio
from typing import List, Dict, Any
import akshare as ak
import pandas as pd

async def execute() -> List[Dict[str, Any]]:
    """
    异步获取新浪财经-行情中心-沪深股市-次新股数据
    
    Returns:
        List[Dict[str, Any]]: 次新股数据列表，每个元素为一个字典代表一只股票的信息
        
    Raises:
        Exception: 当获取数据失败时抛出异常
    """
    try:
        # 调用akshare同步接口获取数据
        df = ak.stock_zh_a_new()
        
        # 将DataFrame转换为List[Dict]格式
        if not df.empty:
            return df.to_dict(orient='records')
        return []
    except Exception as e:
        raise Exception(f"获取次新股数据失败: {str(e)}")

def test() -> List[Dict[str, Any]]:
    """
    同步测试函数，用于自动化测试
    
    Returns:
        List[Dict[str, Any]]: 次新股数据列表
        
    Raises:
        Exception: 当execute方法执行失败时抛出异常
    """
    try:
        return asyncio.run(execute())
    except Exception as e:
        raise Exception(f"测试执行失败: {str(e)}")

if __name__ == '__main__':
    # 演示如何调用异步函数
    async def main():
        try:
            data = await execute()
            print(f"获取到 {len(data)} 条次新股数据")
            if data:
                print("第一条数据示例:")
                print(data[0])
        except Exception as e:
            print(f"执行出错: {e}")
    
    asyncio.run(main())