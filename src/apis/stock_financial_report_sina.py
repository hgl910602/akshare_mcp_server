import asyncio
from typing import Any, Dict, List, Optional
import akshare as ak


async def execute(stock: str, symbol: str) -> List[Dict[str, Any]]:
    """
    异步获取新浪财经-财务报表-三大报表数据
    
    Args:
        stock: 带市场标识的股票代码, 例如 "sh600600"
        symbol: 报表类型, 可选 {"资产负债表", "利润表", "现金流量表"}
    
    Returns:
        返回处理后的财务报表数据列表
    
    Raises:
        Exception: 当获取数据失败时抛出异常
    """
    try:
        # 调用akshare同步接口，使用await让出控制权
        df = await asyncio.get_event_loop().run_in_executor(
            None, 
            lambda: ak.stock_financial_report_sina(stock=stock, symbol=symbol)
        )
        # 将DataFrame转换为List[Dict]格式
        return df.to_dict("records")
    except Exception as e:
        raise Exception(f"获取财务报表数据失败: {e}")


def test():
    """
    同步测试方法，用于自动化测试
    
    Raises:
        直接抛出execute方法可能产生的异常
    """
    # 使用示例参数调用
    result = asyncio.run(execute(stock="sh600600", symbol="资产负债表"))
    print(result)


if __name__ == "__main__":
    # 演示如何调用异步函数
    async def main():
        try:
            data = await execute(stock="sh600600", symbol="利润表")
            print(data)
        except Exception as e:
            print(f"Error: {e}")
    
    asyncio.run(main())