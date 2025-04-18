import asyncio
from typing import List, Dict, Any
import akshare as ak
import pandas as pd

async def execute(
    symbol: str, 
    start_year: str = "2000", 
    end_year: str = "2019", 
    adjust: str = ""
) -> List[Dict[str, Any]]:
    """
    异步获取A+H股历史行情数据
    
    Args:
        symbol: 港股股票代码
        start_year: 开始年份
        end_year: 结束年份
        adjust: 复权类型，默认为空不复权; 'qfq': 前复权, 'hfq': 后复权
        
    Returns:
        List[Dict[str, Any]]: 包含历史行情数据的字典列表
        
    Raises:
        Exception: 当获取数据失败时抛出异常
    """
    try:
        # 调用akshare同步接口获取数据
        df = ak.stock_zh_ah_daily(
            symbol=symbol,
            start_year=start_year,
            end_year=end_year,
            adjust=adjust
        )
        
        # 将DataFrame转换为字典列表
        if not df.empty:
            # 确保日期列是字符串格式
            df["日期"] = df["日期"].astype(str)
            return df.to_dict("records")
        return []
    except Exception as e:
        raise Exception(f"Failed to fetch A+H stock data: {str(e)}")

def test():
    """
    同步测试方法，用于自动化测试
    
    Returns:
        List[Dict[str, Any]]: 包含历史行情数据的字典列表
        
    Raises:
        Exception: 当获取数据失败时抛出异常
    """
    # 使用示例参数调用execute方法
    return asyncio.run(execute(
        symbol="02318",
        start_year="2022",
        end_year="2024",
        adjust=""
    ))

if __name__ == "__main__":
    # 演示如何调用异步函数并打印结果
    async def main():
        try:
            data = await execute(
                symbol="02318",
                start_year="2022",
                end_year="2024",
                adjust=""
            )
            print(data[:5])  # 打印前5条数据
        except Exception as e:
            print(f"Error occurred: {e}")
    
    asyncio.run(main())