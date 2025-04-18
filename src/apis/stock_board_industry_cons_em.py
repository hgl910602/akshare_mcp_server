import asyncio
from typing import List, Dict, Any
import akshare as ak
import pandas as pd

async def execute(symbol: str = "小金属") -> List[Dict[str, Any]]:
    """
    异步获取东方财富-沪深板块-行业板块-板块成份数据
    
    Args:
        symbol: 板块名称或代码，例如:"小金属"或"BK1027"
    
    Returns:
        返回板块成份股数据列表，每个成份股为字典格式
    
    Raises:
        Exception: 当数据获取失败时抛出异常
    """
    try:
        # 调用akshare同步接口获取数据
        df = ak.stock_board_industry_cons_em(symbol=symbol)
        
        # 将DataFrame转换为List[Dict]格式
        result = df.to_dict(orient="records")
        
        return result
    except Exception as e:
        raise Exception(f"获取行业板块成份股数据失败: {str(e)}")

def test():
    """
    同步测试方法，用于自动化测试
    
    Raises:
        当execute方法执行失败时抛出异常
    """
    try:
        # 使用示例参数调用异步方法
        result = asyncio.run(execute(symbol="小金属"))
        print(f"测试成功，获取到{len(result)}条数据")
        return result
    except Exception as e:
        print(f"测试失败: {str(e)}")
        raise

if __name__ == "__main__":
    # 演示如何调用异步函数
    async def main():
        try:
            data = await execute(symbol="小金属")
            print(f"获取到{len(data)}条数据:")
            for item in data[:3]:  # 打印前3条数据
                print(item)
        except Exception as e:
            print(f"执行出错: {str(e)}")
    
    asyncio.run(main())