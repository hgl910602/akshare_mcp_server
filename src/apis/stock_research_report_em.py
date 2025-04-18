import asyncio
from typing import List, Dict, Any
import akshare as ak
import pandas as pd

async def execute(symbol: str) -> List[Dict[str, Any]]:
    """
    异步获取东方财富网个股研报数据
    
    Args:
        symbol: 股票代码, 如 "000001"
        
    Returns:
        个股研报数据列表, 每个元素为字典格式
        
    Raises:
        Exception: 当接口调用失败时抛出异常
    """
    try:
        # 调用akshare接口获取数据
        df = ak.stock_research_report_em(symbol=symbol)
        
        # 处理空数据情况
        if df.empty:
            return []
            
        # 转换DataFrame为List[Dict]格式
        result = df.to_dict("records")
        
        # 处理可能的NaN值
        for item in result:
            for key, value in item.items():
                if pd.isna(value):
                    item[key] = None
                    
        return result
    except Exception as e:
        raise Exception(f"获取个股研报数据失败: {str(e)}")

def test():
    """
    同步测试方法, 用于自动化测试
    
    Returns:
        个股研报数据列表
        
    Raises:
        异常上抛, 不捕获
    """
    # 使用示例参数调用
    return asyncio.run(execute(symbol="000001"))

if __name__ == "__main__":
    # 演示异步调用
    async def main():
        try:
            data = await execute(symbol="000001")
            print(data)
        except Exception as e:
            print(f"Error: {e}")
    
    asyncio.run(main())