import asyncio
from typing import List, Dict, Any
import akshare as ak
import pandas as pd

async def execute() -> List[Dict[str, Any]]:
    """
    异步获取同花顺-数据中心-技术选股-持续缩量数据
    
    Returns:
        List[Dict[str, Any]]: 持续缩量股票数据列表
    """
    try:
        # 调用akshare接口获取数据
        df = ak.stock_rank_cxsl_ths()
        
        # 将DataFrame转换为List[Dict]格式
        if not df.empty:
            return df.to_dict("records")
        return []
    except Exception as e:
        raise RuntimeError(f"获取持续缩量数据失败: {e}")

def test() -> List[Dict[str, Any]]:
    """
    同步测试方法，用于自动化测试
    
    Returns:
        List[Dict[str, Any]]: 持续缩量股票数据列表
        
    Raises:
        Exception: 当execute方法执行失败时抛出异常
    """
    return asyncio.run(execute())

if __name__ == "__main__":
    # 演示如何调用异步函数
    async def main():
        try:
            data = await execute()
            print(f"获取到 {len(data)} 条持续缩量数据")
            for item in data[:3]:  # 打印前3条数据
                print(item)
        except Exception as e:
            print(f"发生错误: {e}")
    
    asyncio.run(main())