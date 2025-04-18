import asyncio
from typing import List, Dict, Any
import akshare as ak
import pandas as pd

async def execute(symbol: str) -> List[Dict[str, Any]]:
    """
    异步获取巨潮资讯个股上市相关信息
    
    Args:
        symbol: 股票代码，如 "600030"
        
    Returns:
        上市相关信息的字典列表
        
    Raises:
        Exception: 当akshare接口调用失败时抛出
    """
    try:
        # 调用akshare接口获取数据
        df = ak.stock_ipo_summary_cninfo(symbol=symbol)
        
        # 将DataFrame转换为字典列表
        if not df.empty:
            # 处理可能的NaN值
            df = df.fillna("")
            return df.to_dict("records")
        return []
    except Exception as e:
        raise Exception(f"获取股票{symbol}上市信息失败: {str(e)}")

def test():
    """
    同步测试方法，用于自动化测试
    
    Raises:
        直接抛出execute方法中的异常
    """
    # 使用示例中的参数进行测试
    symbol = "600030"
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
            data = await execute(symbol="600030")
            print("获取到的上市信息:")
            for item in data:
                print(item)
        except Exception as e:
            print(f"主程序出错: {str(e)}")
    
    asyncio.run(main())