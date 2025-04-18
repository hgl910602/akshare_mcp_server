import asyncio
from typing import List, Dict, Any
import akshare as ak
import pandas as pd

async def execute(symbol: str, name: str) -> List[Dict[str, Any]]:
    """
    东方财富网-数据中心-特色数据-高管持股-人员增减持股变动明细
    
    Args:
        symbol: 股票代码
        name: 高管名称
    
    Returns:
        List[Dict[str, Any]]: 高管持股变动明细数据
        
    Raises:
        Exception: 当获取数据失败时抛出异常
    """
    try:
        # 调用akshare同步接口获取数据
        df = ak.stock_hold_management_person_em(symbol=symbol, name=name)
        
        # 将DataFrame转换为List[Dict]格式
        if not df.empty:
            return df.to_dict(orient='records')
        return []
    except Exception as e:
        raise Exception(f"获取高管持股数据失败: {str(e)}")

def test():
    """
    同步测试方法，用于自动化测试
    
    Raises:
        Exception: 当execute方法执行失败时抛出异常
    """
    try:
        # 使用示例参数调用execute方法
        result = asyncio.run(execute(symbol="001308", name="孙建华"))
        print(result)
    except Exception as e:
        raise Exception(f"测试失败: {str(e)}")

if __name__ == '__main__':
    # 演示如何调用异步函数并打印结果
    async def main():
        try:
            data = await execute(symbol="001308", name="孙建华")
            print(data)
        except Exception as e:
            print(f"Error: {str(e)}")
    
    asyncio.run(main())