import asyncio
from typing import Any, Dict, List, Optional
import aiohttp
import akshare as ak

async def execute(symbol: str, indicator: str = "按报告期") -> List[Dict[str, Any]]:
    """
    异步获取同花顺财务指标-利润表数据
    
    Args:
        symbol: 股票代码
        indicator: 报告期类型，可选 ["按报告期", "按年度", "按单季度"]
    
    Returns:
        财务指标数据列表，每个元素为字典格式
        
    Raises:
        Exception: 当数据获取失败时抛出异常
    """
    try:
        # 使用akshare同步接口，在异步环境中使用run_in_executor
        loop = asyncio.get_running_loop()
        result = await loop.run_in_executor(
            None, 
            ak.stock_financial_benefit_ths, 
            symbol, 
            indicator
        )
        # 将DataFrame转换为List[Dict]格式
        if result is not None:
            return result.to_dict("records")
        return []
    except Exception as e:
        raise Exception(f"Failed to fetch financial benefit data: {str(e)}")

def test():
    """
    同步测试方法，用于自动化测试
    
    Raises:
        Exception: 当execute方法执行失败时抛出异常
    """
    try:
        # 使用示例参数调用execute方法
        result = asyncio.run(execute(symbol="000063", indicator="按报告期"))
        print(f"Test executed successfully. Got {len(result)} records.")
        return result
    except Exception as e:
        print(f"Test failed: {str(e)}")
        raise

if __name__ == "__main__":
    # 演示如何调用异步函数
    async def main():
        try:
            data = await execute(symbol="000063", indicator="按报告期")
            print(f"Fetched {len(data)} records")
            if data:
                print("Sample record:", data[0])
        except Exception as e:
            print("Error:", str(e))
    
    asyncio.run(main())