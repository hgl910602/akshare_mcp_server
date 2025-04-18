import asyncio
from typing import List, Dict, Any
import akshare as ak

async def execute(symbol: str) -> List[Dict[str, Any]]:
    """
    东方财富-股票-财务分析-利润表-报告期
    
    Args:
        symbol: 股票代码, 如 "SH600519"
    
    Returns:
        利润表数据列表, 每个元素为字典形式的行数据
    
    Raises:
        Exception: 当接口调用失败时抛出异常
    """
    try:
        # 调用akshare同步接口
        df = ak.stock_profit_sheet_by_report_em(symbol=symbol)
        # 将DataFrame转换为List[Dict]格式
        return df.to_dict("records")
    except Exception as e:
        raise Exception(f"获取利润表数据失败: {str(e)}")

def test():
    """
    同步测试方法, 用于自动化测试
    
    Raises:
        直接抛出execute方法中的异常
    """
    # 使用示例中的测试参数
    symbol = "SH600519"
    # 异步调用execute方法
    result = asyncio.run(execute(symbol))
    return result

if __name__ == "__main__":
    # 演示如何调用异步函数
    async def main():
        try:
            data = await execute("SH600519")
            print(data[:2])  # 打印前两行数据示例
        except Exception as e:
            print(f"Error: {e}")
    
    asyncio.run(main())