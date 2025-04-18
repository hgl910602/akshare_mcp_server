import asyncio
from typing import List, Dict, Any
import akshare as ak
import pandas as pd

async def execute(symbol: str = "001308") -> List[Dict[str, Any]]:
    """
    深圳证券交易所-信息披露-监管信息公开-董监高人员股份变动
    
    Args:
        symbol: 股票代码或"全部"
    
    Returns:
        List[Dict[str, Any]]: 董监高人员股份变动数据列表
    
    Raises:
        Exception: 当接口调用失败时抛出异常
    """
    try:
        # 调用akshare接口获取数据
        df = ak.stock_share_hold_change_szse(symbol=symbol)
        
        # 将DataFrame转换为List[Dict]格式
        if not df.empty:
            # 处理可能的NaN值
            df = df.fillna("")
            return df.to_dict("records")
        return []
    except Exception as e:
        raise Exception(f"获取董监高人员股份变动数据失败: {str(e)}")

def test():
    """
    同步测试方法，用于自动化测试
    
    Returns:
        List[Dict[str, Any]]: 测试结果
    
    Raises:
        Exception: 当测试失败时抛出异常
    """
    try:
        # 使用示例参数进行测试
        result = asyncio.run(execute(symbol="001308"))
        return result
    except Exception as e:
        raise Exception(f"测试失败: {str(e)}")

if __name__ == "__main__":
    # 演示如何调用异步函数
    async def main():
        try:
            data = await execute(symbol="001308")
            for item in data:
                print(item)
        except Exception as e:
            print(f"Error: {e}")
    
    asyncio.run(main())