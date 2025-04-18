import asyncio
from typing import List, Dict, Any
import akshare as ak
import pandas as pd

async def execute(symbol: str = "科创版") -> List[Dict[str, Any]]:
    """
    异步获取乐咕乐股-主板市盈率数据
    
    Args:
        symbol: 股票市场类型，可选值: "上证", "深证", "创业板", "科创版"
    
    Returns:
        主板市盈率数据列表，每个元素为包含日期、总市值和市盈率的字典
        
    Raises:
        Exception: 当获取数据失败时抛出异常
    """
    try:
        # 调用akshare同步接口获取数据
        df = ak.stock_market_pe_lg(symbol=symbol)
        
        # 转换DataFrame为List[Dict]格式
        result = []
        if not df.empty:
            # 确保列名正确
            df.columns = ["日期", "总市值", "市盈率"]
            result = df.to_dict("records")
        return result
    except Exception as e:
        raise Exception(f"获取{symbol}市盈率数据失败: {str(e)}")

def test():
    """
    同步测试方法，用于自动化测试
    
    Returns:
        主板市盈率数据列表
        
    Raises:
        直接抛出execute方法可能产生的异常
    """
    # 使用示例参数调用异步方法
    return asyncio.run(execute(symbol="科创版"))

if __name__ == "__main__":
    # 演示如何调用异步函数
    async def main():
        try:
            data = await execute(symbol="科创版")
            print(f"获取到{len(data)}条数据:")
            for item in data[:5]:  # 打印前5条数据
                print(item)
        except Exception as e:
            print(f"发生错误: {e}")
    
    asyncio.run(main())