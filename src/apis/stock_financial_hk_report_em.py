import asyncio
from typing import List, Dict, Any
import akshare as ak

async def execute(stock: str, symbol: str, indicator: str) -> List[Dict[str, Any]]:
    """
    异步获取港股财务报表数据
    
    Args:
        stock: 股票代码，如 "00700"
        symbol: 报表类型，可选 {"资产负债表", "利润表", "现金流量表"}
        indicator: 报告期类型，可选 {"年度", "报告期"}
    
    Returns:
        返回处理后的字典列表
    
    Raises:
        Exception: 当akshare接口调用失败时抛出异常
    """
    try:
        # 调用akshare接口获取数据
        df = ak.stock_financial_hk_report_em(stock=stock, symbol=symbol, indicator=indicator)
        # 将DataFrame转换为字典列表
        result = df.to_dict(orient="records")
        return result
    except Exception as e:
        raise Exception(f"获取港股财务报表数据失败: {str(e)}")

def test():
    """
    同步测试方法，用于自动化测试
    
    Raises:
        直接抛出execute方法可能产生的异常
    """
    # 使用示例参数调用
    result = asyncio.run(execute(stock="00700", symbol="资产负债表", indicator="年度"))
    return result

if __name__ == "__main__":
    # 演示如何调用异步函数
    async def main():
        try:
            data = await execute(stock="00700", symbol="资产负债表", indicator="年度")
            for item in data[:3]:  # 打印前3条记录
                print(item)
        except Exception as e:
            print(f"Error: {e}")
    
    asyncio.run(main())