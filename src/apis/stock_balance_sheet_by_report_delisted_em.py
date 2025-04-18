import asyncio
from typing import List, Dict, Any
import akshare as ak

async def execute(symbol: str) -> List[Dict[str, Any]]:
    """
    异步获取东方财富已退市股票资产负债表数据
    
    Args:
        symbol: 带市场标识的已退市股票代码，如"SZ000013"
        
    Returns:
        资产负债表数据列表，每个元素为一个报告期的数据字典
        
    Raises:
        Exception: 当akshare接口调用失败时抛出
    """
    try:
        # 调用akshare同步接口，使用await在异步环境中运行
        loop = asyncio.get_event_loop()
        df = await loop.run_in_executor(
            None, 
            ak.stock_balance_sheet_by_report_delisted_em, 
            symbol
        )
        # 将DataFrame转换为List[Dict]格式
        return df.to_dict("records")
    except Exception as e:
        raise Exception(f"Failed to fetch balance sheet data: {str(e)}")

def test():
    """
    同步测试方法，用于自动化测试
    
    Raises:
        Exception: 当execute方法调用失败时抛出
    """
    try:
        # 使用示例中的测试参数
        symbol = "SZ000013"
        # 运行异步execute方法
        result = asyncio.run(execute(symbol))
        return result
    except Exception as e:
        raise Exception(f"Test failed: {str(e)}")

if __name__ == "__main__":
    # 演示如何调用异步函数
    async def main():
        try:
            # 使用示例参数调用
            data = await execute(symbol="SZ000013")
            # 打印结果
            print(data[:2])  # 只打印前两条记录演示
        except Exception as e:
            print(f"Error: {str(e)}")
    
    asyncio.run(main())