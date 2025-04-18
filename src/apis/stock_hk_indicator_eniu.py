import asyncio
from typing import List, Dict, Any
import akshare as ak

async def execute(symbol: str, indicator: str) -> List[Dict[str, Any]]:
    """
    异步获取港股个股指标数据
    
    Args:
        symbol: 股票代码，如 "hk01093"
        indicator: 指标类型，可选 {"港股", "市盈率", "市净率", "股息率", "ROE", "市值"}
    
    Returns:
        返回包含指标数据的字典列表
    
    Raises:
        Exception: 当akshare接口调用失败时抛出异常
    """
    try:
        # 调用akshare同步接口，使用run_in_executor避免阻塞事件循环
        loop = asyncio.get_running_loop()
        df = await loop.run_in_executor(
            None, 
            ak.stock_hk_indicator_eniu, 
            symbol=symbol, 
            indicator=indicator
        )
        # 将DataFrame转换为List[Dict]格式
        return df.to_dict("records")
    except Exception as e:
        raise Exception(f"Failed to fetch stock indicator data: {str(e)}")

def test():
    """
    同步测试方法，用于验证execute函数
    
    Raises:
        直接抛出execute方法可能产生的异常
    """
    # 使用示例参数进行测试
    result = asyncio.run(execute(symbol="hk01093", indicator="市净率"))
    print(result)

if __name__ == "__main__":
    # 演示如何异步调用该函数
    async def main():
        try:
            data = await execute(symbol="hk01093", indicator="ROE")
            print(data)
        except Exception as e:
            print(f"Error occurred: {e}")
    
    asyncio.run(main())