import asyncio
from typing import List, Dict, Any
import akshare as ak


async def execute(stock: str, symbol: str, indicator: str) -> List[Dict[str, Any]]:
    """
    异步获取美股财务报表数据
    
    Args:
        stock: 股票代码，如 "TSLA"
        symbol: 报表类型，可选 {"资产负债表", "综合损益表", "现金流量表"}
        indicator: 报告类型，可选 {"年报", "单季报", "累计季报"}
    
    Returns:
        返回处理后的字典列表
    
    Raises:
        Exception: 当akshare接口调用失败时抛出异常
    """
    try:
        # 调用akshare接口获取数据
        df = ak.stock_financial_us_report_em(stock=stock, symbol=symbol, indicator=indicator)
        # 将DataFrame转换为字典列表
        result = df.to_dict(orient="records")
        return result
    except Exception as e:
        raise Exception(f"获取美股财务报表数据失败: {e}")


def test():
    """
    同步测试方法，用于验证execute函数
    
    Raises:
        直接抛出execute函数可能产生的异常
    """
    # 使用示例参数调用execute方法
    result = asyncio.run(execute(stock="TSLA", symbol="资产负债表", indicator="年报"))
    print(result)


if __name__ == "__main__":
    # 演示如何调用异步函数
    async def main():
        try:
            data = await execute(stock="TSLA", symbol="资产负债表", indicator="年报")
            print(data)
        except Exception as e:
            print(f"Error: {e}")

    asyncio.run(main())