import asyncio
from typing import List, Dict, Any
import akshare as ak

async def execute(symbol: str) -> List[Dict[str, Any]]:
    """
    异步获取东方财富股票资产负债表数据(按报告期)
    
    Args:
        symbol: 股票代码，如 "SH600519"
        
    Returns:
        资产负债表数据列表，每个元素为字典形式的行数据
        
    Raises:
        Exception: 当接口调用失败时抛出异常
    """
    try:
        # 调用akshare同步接口，使用run_in_executor避免阻塞事件循环
        loop = asyncio.get_running_loop()
        df = await loop.run_in_executor(
            None, 
            ak.stock_balance_sheet_by_report_em, 
            symbol
        )
        # 将DataFrame转换为List[Dict]格式
        return df.to_dict("records")
    except Exception as e:
        raise Exception(f"获取资产负债表数据失败: {str(e)}")

def test():
    """
    同步测试方法，用于自动化测试
    
    Raises:
        直接抛出execute方法中的异常
    """
    try:
        # 使用示例中的测试股票代码
        result = asyncio.run(execute(symbol="SH600519"))
        print(f"获取到{len(result)}条资产负债表数据")
        return result
    except Exception as e:
        print(f"测试失败: {str(e)}")
        raise

if __name__ == "__main__":
    # 演示如何调用异步函数
    async def main():
        try:
            data = await execute(symbol="SH600519")
            print(f"获取到{len(data)}条数据")
            if data:
                print("首条数据示例:")
                print(data[0])
        except Exception as e:
            print(f"调用失败: {str(e)}")
    
    asyncio.run(main())