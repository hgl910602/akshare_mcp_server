import asyncio
from typing import List, Dict, Any
import akshare as ak
import pandas as pd

async def execute(symbol: str = "全部") -> List[Dict[str, Any]]:
    """
    异步获取东方财富网-数据中心-特色数据-高管持股数据
    
    Args:
        symbol: 选择类型, 可选 {"全部", "股东增持", "股东减持"}
    
    Returns:
        List[Dict[str, Any]]: 高管持股数据列表
    
    Raises:
        Exception: 当获取数据失败时抛出异常
    """
    try:
        # 调用akshare同步接口，使用run_in_executor避免阻塞事件循环
        loop = asyncio.get_running_loop()
        df = await loop.run_in_executor(None, ak.stock_ggcg_em, symbol)
        
        # 将DataFrame转换为List[Dict]格式
        if not df.empty:
            return df.to_dict("records")
        return []
    except Exception as e:
        raise Exception(f"获取高管持股数据失败: {e}")

def test():
    """
    同步测试方法，用于自动化测试
    
    Returns:
        List[Dict[str, Any]]: 高管持股数据列表
    
    Raises:
        Exception: 当execute方法执行失败时抛出异常
    """
    try:
        # 使用asyncio.run运行异步方法
        return asyncio.run(execute(symbol="全部"))
    except Exception as e:
        raise Exception(f"测试执行失败: {e}")

if __name__ == "__main__":
    # 演示如何调用异步函数
    async def main():
        try:
            data = await execute(symbol="全部")
            print(f"获取到{len(data)}条高管持股数据")
            if data:
                print("第一条数据示例:")
                print(data[0])
        except Exception as e:
            print(f"发生错误: {e}")
    
    asyncio.run(main())