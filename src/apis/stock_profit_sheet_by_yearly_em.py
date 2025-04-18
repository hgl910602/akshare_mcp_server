import asyncio
from typing import List, Dict, Any
import akshare as ak

async def execute(symbol: str) -> List[Dict[str, Any]]:
    """
    异步获取东方财富股票年度利润表数据
    
    Args:
        symbol: 股票代码，例如 "SH600519"
        
    Returns:
        返回利润表数据的字典列表
        
    Raises:
        Exception: 当数据获取失败时抛出异常
    """
    try:
        # 调用akshare的同步接口，使用await在异步环境中运行
        loop = asyncio.get_running_loop()
        df = await loop.run_in_executor(None, ak.stock_profit_sheet_by_yearly_em, symbol)
        # 将DataFrame转换为字典列表
        return df.to_dict('records')
    except Exception as e:
        raise Exception(f"Failed to fetch profit sheet data: {str(e)}")

def test():
    """
    同步测试方法，用于自动化测试
    
    Raises:
        当execute方法执行失败时会上抛异常
    """
    # 使用示例中的测试参数
    symbol = "SH600519"
    # 使用asyncio.run运行异步方法
    result = asyncio.run(execute(symbol))
    return result

if __name__ == '__main__':
    # 演示如何调用异步函数
    async def main():
        try:
            data = await execute("SH600519")
            print(data[:2])  # 打印前两条数据示例
        except Exception as e:
            print(f"Error occurred: {e}")
    
    asyncio.run(main())