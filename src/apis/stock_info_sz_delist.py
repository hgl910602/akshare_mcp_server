import asyncio
from typing import List, Dict, Any
import akshare as ak

async def execute(symbol: str = "终止上市公司") -> List[Dict[str, Any]]:
    """
    获取深证证券交易所终止/暂停上市股票信息
    
    Args:
        symbol: 股票类型，"暂停上市公司" 或 "终止上市公司"
    
    Returns:
        List[Dict[str, Any]]: 返回股票信息列表，每个元素为包含股票信息的字典
    
    Raises:
        Exception: 当获取数据失败时抛出异常
    """
    try:
        # 调用akshare接口获取数据
        df = ak.stock_info_sz_delist(symbol=symbol)
        # 将DataFrame转换为List[Dict]格式
        return df.to_dict(orient='records')
    except Exception as e:
        raise Exception(f"获取深证终止/暂停上市股票信息失败: {e}")

def test() -> List[Dict[str, Any]]:
    """
    同步测试方法，用于自动化测试
    
    Returns:
        List[Dict[str, Any]]: 返回股票信息列表
    
    Raises:
        Exception: 当execute方法执行失败时抛出异常
    """
    try:
        # 使用asyncio.run调用异步方法
        result = asyncio.run(execute(symbol="终止上市公司"))
        return result
    except Exception as e:
        raise Exception(f"测试失败: {e}")

if __name__ == '__main__':
    # 演示如何调用异步函数
    async def main():
        try:
            data = await execute(symbol="终止上市公司"))
            print(data)
        except Exception as e:
            print(f"Error: {e}")
    
    asyncio.run(main())