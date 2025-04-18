import asyncio
from typing import List, Dict, Any
import akshare as ak

async def execute(symbol: str) -> List[Dict[str, Any]]:
    """
    获取东方财富-已退市股票利润表数据(按报告期)
    
    Args:
        symbol: 带市场标识的已退市股票代码, 如 "SZ000013"
    
    Returns:
        利润表数据列表, 每个元素为一条记录(字典格式)
    
    Raises:
        Exception: 当接口调用失败时抛出异常
    """
    try:
        # 调用akshare接口获取数据
        df = ak.stock_profit_sheet_by_report_delisted_em(symbol=symbol)
        # 将DataFrame转换为List[Dict]格式
        return df.to_dict(orient="records")
    except Exception as e:
        raise Exception(f"获取已退市股票利润表数据失败: {e}")

def test():
    """
    同步测试方法, 用于自动化测试
    
    Raises:
        直接抛出execute方法中的异常
    """
    # 使用示例中的参数进行测试
    symbol = "SZ000013"
    try:
        result = asyncio.run(execute(symbol=symbol))
        print(f"测试成功, 获取到{len(result)}条数据")
        return result
    except Exception as e:
        print(f"测试失败: {e}")
        raise

if __name__ == "__main__":
    # 演示如何调用异步函数
    async def main():
        try:
            # 使用示例参数调用
            data = await execute(symbol="SZ000013")
            print(f"获取到{len(data)}条数据")
            if len(data) > 0:
                print("第一条数据示例:")
                print(data[0])
        except Exception as e:
            print(f"调用失败: {e}")
    
    asyncio.run(main())