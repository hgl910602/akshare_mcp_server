import asyncio
from typing import List, Dict, Any
import akshare as ak
import pandas as pd

async def execute() -> List[Dict[str, Any]]:
    """
    获取东方财富网股票回购数据(异步版本)
    
    Returns:
        List[Dict[str, Any]]: 股票回购数据列表，每个元素为一个字典代表一条记录
        
    Raises:
        Exception: 当数据获取失败时抛出异常
    """
    try:
        # 调用akshare同步接口
        df = ak.stock_repurchase_em()
        
        # 将DataFrame转换为List[Dict]格式
        if not df.empty:
            # 处理可能的NaN值
            df = df.fillna(0)
            return df.to_dict("records")
        return []
    except Exception as e:
        raise Exception(f"获取股票回购数据失败: {str(e)}")

def test() -> List[Dict[str, Any]]:
    """
    同步测试方法
    
    Returns:
        List[Dict[str, Any]]: 股票回购数据
        
    Raises:
        Exception: 当execute方法执行失败时抛出异常
    """
    try:
        return asyncio.run(execute())
    except Exception as e:
        raise Exception(f"测试执行失败: {str(e)}")

if __name__ == "__main__":
    # 演示异步调用
    async def main():
        try:
            data = await execute()
            print(f"获取到{len(data)}条股票回购数据")
            if data:
                print("第一条记录:")
                print(data[0])
        except Exception as e:
            print(f"执行出错: {e}")
    
    asyncio.run(main())