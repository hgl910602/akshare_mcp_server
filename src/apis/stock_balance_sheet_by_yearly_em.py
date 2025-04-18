import asyncio
from typing import List, Dict, Any
import akshare as ak

async def execute(symbol: str) -> List[Dict[str, Any]]:
    """
    异步获取东方财富-股票-财务分析-资产负债表-按年度数据
    
    Args:
        symbol: 股票代码，例如 "SH600519"
        
    Returns:
        资产负债表数据的字典列表
        
    Raises:
        Exception: 当数据获取失败时抛出异常
    """
    try:
        # 调用akshare的同步接口，使用await包装
        loop = asyncio.get_event_loop()
        df = await loop.run_in_executor(
            None, 
            ak.stock_balance_sheet_by_yearly_em, 
            symbol
        )
        # 将DataFrame转换为字典列表
        return df.to_dict("records")
    except Exception as e:
        raise Exception(f"获取资产负债表数据失败: {str(e)}")

def test():
    """
    同步测试方法，用于自动化测试
    
    Raises:
        原样抛出execute方法中的异常
    """
    # 使用示例中的参数进行测试
    symbol = "SH600519"
    try:
        result = asyncio.run(execute(symbol))
        print(f"测试成功，获取到{len(result)}条数据")
        return result
    except Exception as e:
        print(f"测试失败: {str(e)}")
        raise

if __name__ == "__main__":
    # 演示如何调用异步函数
    async def main():
        try:
            data = await execute("SH600519")
            print(f"获取到{len(data)}条资产负债表数据")
            if len(data) > 0:
                print("第一条数据示例:", data[0])
        except Exception as e:
            print(f"调用失败: {str(e)}")
    
    asyncio.run(main())