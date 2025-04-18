import asyncio
from typing import List, Dict, Any
import akshare as ak

async def execute(symbol: str, indicator: str) -> List[Dict[str, Any]]:
    """
    异步获取美股财务分析主要指标数据
    
    Args:
        symbol: 股票代码，如 "TSLA"
        indicator: 报表类型，可选 "年报", "单季报", "累计季报"
    
    Returns:
        财务指标数据列表，每个元素为一个字典表示的指标数据
    
    Raises:
        Exception: 当akshare接口调用失败时抛出异常
    """
    try:
        # 调用akshare同步接口，使用await包装
        loop = asyncio.get_running_loop()
        df = await loop.run_in_executor(
            None, 
            ak.stock_financial_us_analysis_indicator_em,
            symbol=symbol,
            indicator=indicator
        )
        # 将DataFrame转换为List[Dict]格式
        return df.to_dict("records")
    except Exception as e:
        raise Exception(f"Failed to fetch US stock financial indicators: {str(e)}")

def test():
    """
    同步测试方法，用于自动化测试
    
    Raises:
        Exception: 当execute方法调用失败时抛出异常
    """
    try:
        result = asyncio.run(execute(symbol="TSLA", indicator="年报"))
        print(f"Test executed successfully, got {len(result)} records")
        return result
    except Exception as e:
        raise Exception(f"Test failed: {str(e)}")

if __name__ == "__main__":
    # 演示如何调用异步函数
    async def main():
        try:
            data = await execute(symbol="TSLA", indicator="年报")
            print(f"Got {len(data)} records")
            if data:
                print("Sample data:", data[0])
        except Exception as e:
            print(f"Error: {str(e)}")
    
    asyncio.run(main())