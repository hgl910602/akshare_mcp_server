import asyncio
from typing import List, Dict, Any
import akshare as ak
import pandas as pd

async def execute(symbol: str = "600000") -> List[Dict[str, Any]]:
    """
    异步获取上海证券交易所-披露-监管信息公开-公司监管-董监高人员股份变动数据
    
    Args:
        symbol: 股票代码或"全部"
    
    Returns:
        List[Dict[str, Any]]: 转换后的数据列表
    
    Raises:
        Exception: 当akshare接口调用失败时抛出
    """
    try:
        # 调用akshare同步接口
        df = ak.stock_share_hold_change_sse(symbol=symbol)
        
        # 将DataFrame转换为List[Dict]格式
        if not df.empty:
            # 处理可能的NaN值
            df = df.fillna("")
            return df.to_dict("records")
        return []
    except Exception as e:
        raise Exception(f"获取董监高股份变动数据失败: {str(e)}")

def test():
    """
    同步测试方法，用于自动化测试
    
    Raises:
        Exception: 当execute调用失败时抛出
    """
    try:
        # 使用示例参数调用异步方法
        result = asyncio.run(execute(symbol="600000"))
        return result
    except Exception as e:
        raise Exception(f"测试失败: {str(e)}")

if __name__ == "__main__":
    # 演示如何调用异步函数
    async def main():
        try:
            data = await execute(symbol="600000")
            print(f"获取到{len(data)}条记录")
            if data:
                print("第一条记录:", data[0])
        except Exception as e:
            print(f"调用失败: {str(e)}")
    
    asyncio.run(main())