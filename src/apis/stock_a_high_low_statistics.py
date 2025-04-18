import asyncio
from typing import List, Dict, Any
import akshare as ak

async def execute(symbol: str = "all") -> List[Dict[str, Any]]:
    """
    获取不同市场的创新高和新低的股票数量
    
    Args:
        symbol: 市场类型，可选值为 "all"(全部A股), "sz50"(上证50), "hs300"(沪深300), "zz500"(中证500)
    
    Returns:
        创新高和新低的股票数量数据列表，每个元素为一个字典
        
    Raises:
        Exception: 当获取数据失败时抛出异常
    """
    try:
        # 调用akshare接口获取数据
        df = ak.stock_a_high_low_statistics(symbol=symbol)
        
        # 将DataFrame转换为List[Dict]格式
        result = df.to_dict(orient="records")
        return result
    except Exception as e:
        raise Exception(f"获取创新高和新低股票数量数据失败: {str(e)}")

def test():
    """
    同步测试方法，用于自动化测试
    
    Returns:
        创新高和新低的股票数量数据列表
        
    Raises:
        直接抛出execute方法可能产生的异常
    """
    # 使用默认参数调用execute方法
    return asyncio.run(execute(symbol="all"))

if __name__ == "__main__":
    # 演示如何调用异步函数并打印结果
    async def main():
        try:
            data = await execute(symbol="all")
            print("创新高和新低股票数量数据:")
            for item in data:
                print(item)
        except Exception as e:
            print(f"发生错误: {e}")
    
    asyncio.run(main())