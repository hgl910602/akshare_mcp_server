import asyncio
from typing import List, Dict, Any
import akshare as ak

async def execute(symbol: str) -> List[Dict[str, Any]]:
    """
    东方财富-股票-财务分析-利润表-按单季度
    
    Args:
        symbol: 股票代码，例如 "SH600519"
    
    Returns:
        利润表数据的字典列表
    
    Raises:
        Exception: 当接口调用失败时抛出异常
    """
    try:
        # 调用akshare接口获取数据
        df = ak.stock_profit_sheet_by_quarterly_em(symbol=symbol)
        # 将DataFrame转换为字典列表
        return df.to_dict("records")
    except Exception as e:
        raise Exception(f"获取股票季度利润表数据失败: {e}")

def test():
    """
    同步测试方法，用于自动化测试
    
    Raises:
        原样抛出execute方法中的异常
    """
    # 使用示例中的测试参数
    symbol = "SH600519"
    try:
        result = asyncio.run(execute(symbol))
        print(f"测试成功，获取到{len(result)}条数据")
        return result
    except Exception as e:
        print(f"测试失败: {e}")
        raise

if __name__ == "__main__":
    # 演示如何调用异步函数
    async def main():
        try:
            # 使用示例中的测试参数
            data = await execute(symbol="SH600519")
            print(f"获取到{len(data)}条数据")
            # 打印前5条数据
            for i, item in enumerate(data[:5], 1):
                print(f"\n第{i}条记录:")
                for k, v in item.items():
                    print(f"{k}: {v}")
        except Exception as e:
            print(f"调用失败: {e}")
    
    asyncio.run(main())