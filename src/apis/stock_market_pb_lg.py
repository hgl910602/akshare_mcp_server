import asyncio
from typing import List, Dict, Any
import akshare as ak
import pandas as pd

async def execute(symbol: str = "上证") -> List[Dict[str, Any]]:
    """
    异步获取乐咕乐股-主板市净率数据
    
    Args:
        symbol: 股票市场标识，可选: "上证", "深证", "创业板", "科创版"
        
    Returns:
        返回处理后的数据列表，每个元素为包含字段的字典
        
    Raises:
        Exception: 当akshare接口调用失败或数据处理出错时抛出异常
    """
    try:
        # 调用akshare同步接口
        df = ak.stock_market_pb_lg(symbol=symbol)
        
        # 处理数据为List[Dict]格式
        result = []
        for _, row in df.iterrows():
            item = {
                "日期": str(row["日期"]),
                "指数": float(row["指数"]),
                "市净率": float(row["市净率"]),
                "等权市净率": float(row["等权市净率"]),
                "市净率中位数": float(row["市净率中位数"])
            }
            result.append(item)
            
        return result
    except Exception as e:
        raise Exception(f"获取主板市净率数据失败: {str(e)}")


def test():
    """
    同步测试方法，用于自动化测试
    
    Returns:
        返回execute方法的执行结果
        
    Raises:
        直接抛出execute方法可能产生的异常
    """
    try:
        # 使用asyncio.run调用异步方法
        result = asyncio.run(execute(symbol="上证"))
        return result
    except Exception as e:
        raise e


if __name__ == "__main__":
    # 演示如何调用异步函数
    async def main():
        try:
            data = await execute(symbol="上证")
            for item in data:
                print(item)
        except Exception as e:
            print(f"Error: {e}")
    
    asyncio.run(main())