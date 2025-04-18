import asyncio
from typing import List, Dict, Any
import akshare as ak

async def execute(symbol: str, indicator: str) -> List[Dict[str, Any]]:
    """
    异步获取同花顺财务指标-资产负债表数据
    
    Args:
        symbol: 股票代码
        indicator: 报告期类型，可选 {"按报告期", "按年度", "按单季度"}
    
    Returns:
        财务数据列表，每个元素为字典形式的财务指标
    
    Raises:
        Exception: 当获取数据失败时抛出异常
    """
    try:
        # 调用akshare同步接口，使用run_in_executor避免阻塞事件循环
        loop = asyncio.get_running_loop()
        df = await loop.run_in_executor(
            None, 
            ak.stock_financial_debt_ths, 
            symbol, 
            indicator
        )
        # 将DataFrame转换为List[Dict]格式
        return df.to_dict("records")
    except Exception as e:
        raise Exception(f"Failed to fetch financial debt data: {str(e)}")

def test():
    """
    同步测试方法，用于自动化测试
    
    Raises:
        原样抛出execute方法中的异常
    """
    # 使用示例参数调用
    return asyncio.run(execute(symbol="000063", indicator="按年度"))

if __name__ == "__main__":
    # 演示异步调用
    async def main():
        try:
            data = await execute(symbol="000063", indicator="按年度")
            print(data[:2])  # 打印前两条记录示例
        except Exception as e:
            print(f"Error occurred: {e}")
    
    asyncio.run(main())