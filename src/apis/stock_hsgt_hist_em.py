import asyncio
from typing import List, Dict, Any
import akshare as ak
import pandas as pd

async def execute(symbol: str = "北向资金") -> List[Dict[str, Any]]:
    """
    异步获取沪深港通历史数据
    
    Args:
        symbol: 数据类别, 可选: "北向资金", "沪股通", "深股通", "南向资金", "港股通沪", "港股通深"
    
    Returns:
        沪深港通历史数据列表, 每个元素为包含字段的字典
    
    Raises:
        Exception: 当获取数据失败时抛出异常
    """
    try:
        # 调用akshare同步接口, 在异步函数中使用run_in_executor避免阻塞事件循环
        loop = asyncio.get_running_loop()
        df = await loop.run_in_executor(None, ak.stock_hsgt_hist_em, symbol)
        
        # 将DataFrame转换为List[Dict]格式
        if not df.empty:
            return df.to_dict("records")
        return []
    except Exception as e:
        raise Exception(f"获取沪深港通历史数据失败: {e}")

def test():
    """
    同步测试方法, 用于自动化测试
    
    Raises:
        Exception: 当execute执行失败时抛出异常
    """
    try:
        # 使用asyncio.run运行异步函数
        result = asyncio.run(execute(symbol="港股通沪"))
        print(f"测试成功, 获取到{len(result)}条数据")
        return result
    except Exception as e:
        print(f"测试失败: {e}")
        raise

if __name__ == "__main__":
    # 演示如何调用异步函数
    async def main():
        try:
            data = await execute(symbol="港股通沪")
            print(f"获取到{len(data)}条数据")
            if data:
                print("第一条数据示例:")
                print(data[0])
        except Exception as e:
            print(f"调用失败: {e}")
    
    asyncio.run(main())