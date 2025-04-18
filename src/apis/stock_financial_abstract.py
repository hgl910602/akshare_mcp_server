import asyncio
from typing import List, Dict, Any
import akshare as ak

async def execute(symbol: str) -> List[Dict[str, Any]]:
    """
    异步获取新浪财经-财务报表-关键指标数据
    
    Args:
        symbol: 股票代码, 例如 "600004"
        
    Returns:
        返回处理后的关键指标数据列表
        
    Raises:
        Exception: 当数据获取或处理失败时抛出异常
    """
    try:
        # 调用akshare同步接口获取数据
        df = ak.stock_financial_abstract(symbol=symbol)
        # 将DataFrame转换为List[Dict]格式
        result = df.to_dict(orient="records")
        return result
    except Exception as e:
        raise Exception(f"获取股票{symbol}财务摘要数据失败: {str(e)}")

def test():
    """
    同步测试方法，用于自动化测试
    
    Raises:
        原样抛出execute方法中的异常
    """
    # 使用示例中的参数进行测试
    symbol = "600004"
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
            symbol = "600004"
            data = await execute(symbol)
            print(f"获取到股票{symbol}的财务摘要数据:")
            for item in data:
                print(item)
        except Exception as e:
            print(f"主程序出错: {str(e)}")
    
    asyncio.run(main())