import asyncio
from typing import List, Dict, Any
import akshare as ak

async def execute(symbol: str) -> List[Dict[str, Any]]:
    """
    东方财富-股票-财务分析-现金流量表-按单季度
    
    Args:
        symbol: 股票代码，例如 "SH600519"
    
    Returns:
        现金流量表数据的列表，每个元素为一个季度的数据字典
    
    Raises:
        Exception: 当数据获取失败时抛出异常
    """
    try:
        # 调用akshare的同步接口，使用asyncio.to_thread转为异步
        df = await asyncio.to_thread(ak.stock_cash_flow_sheet_by_quarterly_em, symbol=symbol)
        # 将DataFrame转换为List[Dict]格式
        return df.to_dict(orient="records")
    except Exception as e:
        raise Exception(f"获取现金流量表数据失败: {e}")

def test():
    """
    同步测试方法，用于自动化测试
    
    Raises:
        原样抛出execute方法可能抛出的异常
    """
    # 使用示例中的测试参数
    test_symbol = "SH600519"
    # 直接调用异步的execute方法并等待结果
    result = asyncio.run(execute(symbol=test_symbol))
    return result

if __name__ == "__main__":
    # 演示如何调用异步函数
    async def main():
        try:
            data = await execute(symbol="SH600519")
            print(data[:2])  # 打印前两条数据示例
        except Exception as e:
            print(f"Error: {e}")
    
    asyncio.run(main())