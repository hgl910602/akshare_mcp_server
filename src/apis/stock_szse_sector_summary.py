import asyncio
from typing import Any, Dict, List
import akshare as ak

async def execute(symbol: str = "当月", date: str = "202501") -> List[Dict[str, Any]]:
    """
    异步获取深圳证券交易所-统计资料-股票行业成交数据
    
    Args:
        symbol: 统计周期, "当月" 或 "当年"
        date: 年月格式, 如 "202501"
    
    Returns:
        返回处理后的字典列表
        
    Raises:
        Exception: 当akshare接口调用失败时抛出异常
    """
    try:
        # 调用akshare同步接口
        df = ak.stock_szse_sector_summary(symbol=symbol, date=date)
        
        # 将DataFrame转换为字典列表
        result = df.to_dict(orient="records")
        return result
    except Exception as e:
        raise Exception(f"获取深圳证券交易所股票行业成交数据失败: {e}")

def test() -> List[Dict[str, Any]]:
    """
    同步测试方法, 用于自动化测试
    
    Returns:
        返回execute方法的执行结果
        
    Raises:
        直接抛出execute方法可能产生的异常
    """
    return asyncio.run(execute(symbol="当年", date="202501"))

if __name__ == "__main__":
    # 演示异步调用
    async def main():
        try:
            data = await execute(symbol="当月", date="202501")
            print(data)
        except Exception as e:
            print(f"Error: {e}")
    
    asyncio.run(main())