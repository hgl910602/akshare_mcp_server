import asyncio
from typing import List, Dict, Any
import akshare as ak

async def execute(symbol: str, indicator: str) -> List[Dict[str, Any]]:
    """
    异步获取同花顺财务指标-现金流量表数据
    
    Args:
        symbol: 股票代码
        indicator: 报告期类型，可选 {"按报告期", "按年度", "按单季度"}
        
    Returns:
        现金流量表数据列表，每个元素为字典形式的行数据
        
    Raises:
        Exception: 当akshare接口调用失败时抛出
    """
    try:
        # 调用akshare接口获取数据
        df = ak.stock_financial_cash_ths(symbol=symbol, indicator=indicator)
        # 将DataFrame转换为List[Dict]格式
        return df.to_dict("records")
    except Exception as e:
        raise Exception(f"Failed to fetch cash flow data: {str(e)}")

def test():
    """
    同步测试方法，用于自动化测试
    
    Raises:
        Exception: 当execute方法调用失败时抛出
    """
    # 使用示例参数调用execute方法
    result = asyncio.run(execute(symbol="000063", indicator="按单季度"))
    print(result)

if __name__ == "__main__":
    # 演示如何调用异步函数
    async def main():
        try:
            data = await execute(symbol="000063", indicator="按单季度")
            print(data)
        except Exception as e:
            print(f"Error occurred: {e}")
    
    asyncio.run(main())