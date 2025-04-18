import asyncio
from typing import List, Dict, Any
import akshare as ak
import pandas as pd

async def execute(stock: str) -> List[Dict[str, Any]]:
    """
    获取东方财富网-沪深港通持股-具体股票数据(异步版本)
    
    Args:
        stock: 股票代码, 如 "002008"
        
    Returns:
        沪深港通持股数据列表, 每个元素为包含字段的字典
        
    Raises:
        Exception: 当获取数据失败时抛出异常
    """
    try:
        # 调用akshare同步接口获取数据
        df = ak.stock_hsgt_individual_em(stock=stock)
        
        # 将DataFrame转换为List[Dict]格式
        result = df.to_dict(orient="records")
        
        # 处理可能的NaN值
        for item in result:
            for key, value in item.items():
                if pd.isna(value):
                    item[key] = None
        
        return result
    except Exception as e:
        raise Exception(f"获取沪深港通个股持股数据失败: {e}")

def test():
    """
    同步测试方法, 用于自动化测试
    
    Returns:
        沪深港通持股数据列表
        
    Raises:
        原样抛出execute方法可能抛出的异常
    """
    # 使用示例参数调用
    return asyncio.run(execute(stock="002008"))

if __name__ == "__main__":
    # 演示如何调用异步函数
    async def main():
        try:
            data = await execute(stock="002008")
            print(data)
        except Exception as e:
            print(f"Error: {e}")
    
    asyncio.run(main())