import asyncio
from typing import List, Dict, Any
import akshare as ak
import pandas as pd

async def execute() -> List[Dict[str, Any]]:
    """
    获取东方财富网-行情中心-港股市场-知名港股实时行情数据
    
    Returns:
        List[Dict[str, Any]]: 返回知名港股实时行情数据列表，每个元素为一个字典代表一只股票的信息
        
    Raises:
        Exception: 当获取数据失败时抛出异常
    """
    try:
        # 调用akshare接口获取数据
        df = ak.stock_hk_famous_spot_em()
        
        # 将DataFrame转换为List[Dict]格式
        if not df.empty:
            # 处理可能的NaN值
            df = df.fillna(0)
            return df.to_dict("records")
        return []
    except Exception as e:
        raise Exception(f"获取知名港股数据失败: {str(e)}")

def test() -> List[Dict[str, Any]]:
    """
    同步测试方法，用于其他工具自动化测试
    
    Returns:
        List[Dict[str, Any]]: 返回知名港股实时行情数据列表
        
    Raises:
        Exception: 当execute方法执行失败时抛出异常
    """
    return asyncio.run(execute())

if __name__ == "__main__":
    # 演示如何调用异步函数
    async def main():
        try:
            data = await execute()
            print(f"获取到 {len(data)} 条知名港股数据:")
            for item in data[:3]:  # 打印前3条数据示例
                print(item)
        except Exception as e:
            print(f"执行出错: {e}")
    
    asyncio.run(main())