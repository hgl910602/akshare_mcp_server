import asyncio
from typing import List, Dict, Any
import akshare as ak
import pandas as pd

async def execute(symbol: str, indicator: str) -> List[Dict[str, Any]]:
    """
    异步获取港股盈利预测数据
    
    Args:
        symbol: 股票代码，如 "09999"
        indicator: 指标类型，可选 {"评级总览", "去年度业绩表现", "综合盈利预测", "盈利预测概览"}
    
    Returns:
        返回处理后的数据列表，每个元素为字典格式
        
    Raises:
        Exception: 当akshare接口调用失败或数据处理出错时抛出
    """
    try:
        # 调用akshare接口获取数据
        df = ak.stock_hk_profit_forecast_et(symbol=symbol, indicator=indicator)
        
        # 处理空数据情况
        if df.empty:
            return []
            
        # 转换DataFrame为List[Dict]格式
        result = df.to_dict(orient='records')
        return result
    except Exception as e:
        raise Exception(f"获取港股盈利预测数据失败: {str(e)}")

def test():
    """
    同步测试方法，用于自动化测试
    
    Raises:
        直接抛出execute方法可能产生的异常
    """
    # 使用示例参数调用
    result = asyncio.run(execute(symbol="09999", indicator="盈利预测概览"))
    return result

if __name__ == '__main__':
    # 演示如何调用异步函数
    async def main():
        try:
            data = await execute(symbol="09999", indicator="盈利预测概览")
            for item in data:
                print(item)
        except Exception as e:
            print(f"Error: {e}")
    
    asyncio.run(main())