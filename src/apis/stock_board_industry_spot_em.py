import asyncio
from typing import List, Dict, Any
import akshare as ak
import pandas as pd

async def execute(symbol: str = "小金属") -> List[Dict[str, Any]]:
    """
    异步获取东方财富网-沪深板块-行业板块-实时行情数据
    
    Args:
        symbol: 行业板块名称，默认为"小金属"
        
    Returns:
        返回包含行业板块实时行情数据的字典列表
        
    Raises:
        Exception: 当获取数据失败时抛出异常
    """
    try:
        # 调用akshare同步接口
        df = ak.stock_board_industry_spot_em(symbol=symbol)
        
        # 将DataFrame转换为字典列表
        if not df.empty:
            return df.to_dict("records")
        return []
    except Exception as e:
        raise Exception(f"获取行业板块实时行情数据失败: {e}")

def test():
    """
    同步测试方法，用于自动化测试
    
    Returns:
        返回execute方法的执行结果
        
    Raises:
        直接上抛execute方法可能抛出的异常
    """
    # 使用asyncio.run运行异步方法
    return asyncio.run(execute(symbol="小金属"))

if __name__ == "__main__":
    # 演示如何调用异步函数
    async def main():
        try:
            data = await execute(symbol="小金属")
            print(data)
        except Exception as e:
            print(f"Error: {e}")
    
    # 运行主函数
    asyncio.run(main())