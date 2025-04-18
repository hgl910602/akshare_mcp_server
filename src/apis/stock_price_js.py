import asyncio
from typing import Any, Dict, List
import akshare as ak
import pandas as pd

async def execute(symbol: str = "us") -> List[Dict[str, Any]]:
    """
    异步获取美港电讯-美港目标价数据
    
    Args:
        symbol: 市场类型, "us"表示美股, "hk"表示港股
        
    Returns:
        返回处理后的目标价数据列表, 每个元素为包含目标价信息的字典
        
    Raises:
        Exception: 当akshare接口调用失败或数据处理出错时抛出异常
    """
    try:
        # 调用akshare接口获取数据
        df = await asyncio.to_thread(ak.stock_price_js, symbol=symbol)
        
        # 处理数据为List[Dict]格式
        result = []
        if not df.empty:
            # 替换NaN为None, 确保JSON序列化
            df = df.where(pd.notnull(df), None)
            result = df.to_dict(orient="records")
        return result
    except Exception as e:
        raise Exception(f"Failed to fetch stock price js data: {str(e)}")

def test():
    """
    同步测试方法, 用于自动化测试
    
    Raises:
        Exception: 当execute方法执行失败时抛出异常
    """
    try:
        # 使用示例参数调用execute方法
        data = asyncio.run(execute(symbol="us"))
        print(f"Test executed successfully, got {len(data)} records")
        return data
    except Exception as e:
        print(f"Test failed: {str(e)}")
        raise

if __name__ == "__main__":
    # 演示如何调用异步函数
    async def main():
        try:
            data = await execute(symbol="us")
            print(f"Got {len(data)} records")
            if data:
                print("Sample record:", data[0])
        except Exception as e:
            print(f"Error: {str(e)}")
    
    asyncio.run(main())