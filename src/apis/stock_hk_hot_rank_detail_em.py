import asyncio
from typing import List, Dict, Any
import akshare as ak
import pandas as pd

async def execute(symbol: str) -> List[Dict[str, Any]]:
    """
    获取东方财富网-股票热度-历史趋势数据 (异步版本)
    
    Args:
        symbol: 股票代码，例如 "00700"
        
    Returns:
        返回处理后的数据列表，每个元素为包含时间、排名、证券代码的字典
        
    Raises:
        Exception: 当获取数据或处理数据过程中出现错误时抛出
    """
    try:
        # 调用akshare接口获取数据
        df = ak.stock_hk_hot_rank_detail_em(symbol=symbol)
        
        # 处理数据为List[Dict]格式
        result = []
        for _, row in df.iterrows():
            item = {
                "时间": str(row["时间"]),
                "排名": int(row["排名"]),
                "证券代码": str(row["证券代码"])
            }
            result.append(item)
            
        return result
    except Exception as e:
        raise Exception(f"获取股票热度数据失败: {str(e)}")

def test():
    """
    同步测试方法，用于自动化测试
    
    Raises:
        原样抛出execute方法可能抛出的异常
    """
    # 使用示例中的参数进行测试
    symbol = "00700"
    try:
        result = asyncio.run(execute(symbol))
        print(result)
        return result
    except Exception as e:
        print(f"测试失败: {str(e)}")
        raise

if __name__ == "__main__":
    # 演示如何调用异步函数
    async def main():
        try:
            data = await execute(symbol="00700")
            print(data)
        except Exception as e:
            print(f"执行出错: {e}")
    
    asyncio.run(main())