import asyncio
from typing import List, Dict, Any
import akshare as ak
import pandas as pd

async def execute(symbol: str = "全部") -> List[Dict[str, Any]]:
    """
    异步获取巨潮资讯-数据中心-专题统计-股东股本-股本变动数据
    
    Args:
        symbol: 股票市场类型，可选 {"深市主板", "沪市", "创业板", "科创板", "北交所", "全部"}
        
    Returns:
        股本变动数据列表，每个元素为一个字典
        
    Raises:
        Exception: 当akshare接口调用失败时抛出异常
    """
    try:
        # 调用akshare接口获取数据
        df = ak.stock_hold_change_cninfo(symbol=symbol)
        
        # 将DataFrame转换为List[Dict]格式
        if not df.empty:
            # 处理可能的NaN值
            df = df.fillna("")
            return df.to_dict("records")
        return []
    except Exception as e:
        raise Exception(f"获取股本变动数据失败: {str(e)}")

def test():
    """
    同步测试方法，用于自动化测试
    
    Returns:
        股本变动数据列表
        
    Raises:
        直接抛出execute方法中的异常
    """
    try:
        # 使用示例参数调用异步方法
        result = asyncio.run(execute(symbol="全部"))
        return result
    except Exception as e:
        raise

if __name__ == "__main__":
    # 演示如何调用异步函数
    async def main():
        try:
            data = await execute(symbol="全部"))
            print(f"获取到{len(data)}条股本变动数据")
            if data:
                print("示例数据:")
                print(data[0])
        except Exception as e:
            print(f"发生错误: {e}")
    
    asyncio.run(main())