import asyncio
from typing import List, Dict, Any
import akshare as ak
import pandas as pd

async def execute() -> List[Dict[str, Any]]:
    """
    异步获取同花顺-数据中心-新股数据-新股上市首日数据
    
    Returns:
        List[Dict[str, Any]]: 新股上市首日数据列表，每个元素为包含字段的字典
        
    Raises:
        Exception: 当获取数据失败时抛出异常
    """
    try:
        # 调用akshare接口获取数据
        df = ak.stock_xgsr_ths()
        
        # 将DataFrame转换为List[Dict]格式
        if not df.empty:
            # 处理可能的NaN值
            df = df.fillna('')
            return df.to_dict('records')
        return []
    except Exception as e:
        raise Exception(f"获取新股上市首日数据失败: {e}")

def test() -> List[Dict[str, Any]]:
    """
    同步测试方法，用于自动化测试
    
    Returns:
        List[Dict[str, Any]]: 新股上市首日数据列表
        
    Raises:
        Exception: 当execute方法执行失败时抛出异常
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
            print(f"获取到 {len(data)} 条新股上市首日数据")
            if data:
                print("示例数据:")
                print(data[0])
        except Exception as e:
            print(f"执行出错: {e}")
    
    asyncio.run(main())