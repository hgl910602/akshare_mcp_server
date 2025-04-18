import asyncio
from typing import List, Dict, Any
import akshare as ak
import pandas as pd
from datetime import datetime

async def execute() -> List[Dict[str, Any]]:
    """
    获取所有港股的实时行情数据(15分钟延时)
    
    Returns:
        List[Dict[str, Any]]: 港股实时行情数据列表，每个元素为一个字典代表一只股票的数据
        
    Raises:
        Exception: 当获取数据失败时抛出异常
    """
    try:
        # 调用akshare接口获取数据
        df = ak.stock_hk_spot()
        
        # 将DataFrame转换为List[Dict]格式
        result = []
        for _, row in df.iterrows():
            record = {
                "symbol": row["symbol"],
                "name": row["name"],
                "engname": row["engname"],
                "tradetype": row["tradetype"],
                "lasttrade": row["lasttrade"],
                "prevclose": row["prevclose"],
                "open": row["open"],
                "high": row["high"],
                "low": row["low"],
                "volume": row["volume"],
                "amount": row["amount"],
                "ticktime": row["ticktime"],
                "buy": row["buy"],
                "sell": row["sell"],
                "pricechange": row["pricechange"],
                "changepercent": row["changepercent"]
            }
            result.append(record)
            
        return result
    except Exception as e:
        raise Exception(f"获取港股实时行情数据失败: {str(e)}")

def test() -> List[Dict[str, Any]]:
    """
    同步测试方法，用于自动化测试
    
    Returns:
        List[Dict[str, Any]]: 港股实时行情数据列表
        
    Raises:
        Exception: 当execute方法执行失败时抛出异常
    """
    try:
        return asyncio.run(execute())
    except Exception as e:
        raise Exception(f"测试获取港股实时行情数据失败: {str(e)}")

if __name__ == "__main__":
    # 演示如何调用异步函数
    async def main():
        try:
            data = await execute()
            print(f"获取到 {len(data)} 条港股实时行情数据")
            if data:
                print("第一条数据示例:")
                print(data[0])
        except Exception as e:
            print(f"执行出错: {str(e)}")
    
    asyncio.run(main())