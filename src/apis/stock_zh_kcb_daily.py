import asyncio
from typing import Any, Dict, List, Optional
import aiohttp
import akshare as ak
import pandas as pd

async def execute(symbol: str, adjust: str = "") -> List[Dict[str, Any]]:
    """
    异步获取科创板股票历史行情数据
    
    Args:
        symbol: 带市场标识的股票代码, 例如 "sh688008"
        adjust: 复权类型, 可选: 
            ""(默认不复权), "qfq"(前复权), "hfq"(后复权),
            "hfq-factor"(后复权因子), "qfq-factor"(前复权因子)
    
    Returns:
        科创板股票历史行情数据列表, 每个元素为包含单日数据的字典
        
    Raises:
        Exception: 当获取数据失败时抛出异常
    """
    try:
        # 使用akshare同步接口获取数据
        df = ak.stock_zh_kcb_daily(symbol=symbol, adjust=adjust)
        
        # 将DataFrame转换为List[Dict]格式
        if not df.empty:
            # 处理可能的NaN值
            df = df.fillna(0)
            # 转换日期格式为字符串
            if 'date' in df.columns:
                df['date'] = df['date'].astype(str)
            return df.to_dict('records')
        return []
    except Exception as e:
        raise Exception(f"Failed to fetch stock data for {symbol}: {str(e)}")

def test():
    """
    同步测试方法, 用于自动化测试
    
    Raises:
        原样抛出execute方法中的任何异常
    """
    try:
        # 使用示例参数调用execute方法
        result = asyncio.run(execute(symbol="sh688399", adjust="hfq"))
        print(f"Test completed. Got {len(result)} records.")
        return result
    except Exception as e:
        print(f"Test failed: {str(e)}")
        raise

if __name__ == '__main__':
    # 演示如何调用异步函数
    async def main():
        try:
            data = await execute(symbol="sh688008", adjust="qfq")
            print(f"Got {len(data)} records")
            if data:
                print("First record:", data[0])
        except Exception as e:
            print("Error:", str(e))
    
    asyncio.run(main())