import asyncio
from typing import List, Dict, Any
import akshare as ak
import pandas as pd

async def execute(symbol: str = "20230930") -> List[Dict[str, Any]]:
    """
    异步获取东方财富网-股东户数数据
    
    Args:
        symbol: 查询日期，格式为"YYYYMMDD"或"最新"
        
    Returns:
        股东户数数据列表，每个元素为字典形式
        
    Raises:
        Exception: 当akshare接口调用失败时抛出异常
    """
    try:
        # 调用akshare同步接口获取数据
        df = ak.stock_zh_a_gdhs(symbol=symbol)
        
        # 将DataFrame转换为List[Dict]格式
        if not df.empty:
            # 处理可能的NaN值
            df = df.fillna(0)
            return df.to_dict("records")
        return []
    except Exception as e:
        raise Exception(f"获取股东户数数据失败: {str(e)}")

def test():
    """
    同步测试方法，用于自动化测试
    
    Returns:
        股东户数数据列表
        
    Raises:
        原样抛出execute方法中的异常
    """
    try:
        # 使用示例参数调用异步方法
        return asyncio.run(execute(symbol="20230930"))
    except Exception as e:
        raise e

if __name__ == "__main__":
    # 演示如何调用异步函数
    async def main():
        try:
            data = await execute(symbol="20230930")
            for item in data[:3]:  # 打印前3条数据
                print(item)
        except Exception as e:
            print(f"Error: {e}")
    
    asyncio.run(main())