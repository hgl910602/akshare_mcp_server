import asyncio
from typing import List, Dict, Any
import akshare as ak

async def execute(symbol: str = "SZ000665") -> List[Dict[str, Any]]:
    """
    东方财富-个股人气榜-最新排名
    
    Args:
        symbol: 股票代码，例如 "SZ000665"
    
    Returns:
        List[Dict[str, Any]]: 返回个股人气榜数据列表
    
    Raises:
        Exception: 当获取数据失败时抛出异常
    """
    try:
        # 调用akshare接口获取数据
        df = ak.stock_hot_rank_latest_em(symbol=symbol)
        # 将DataFrame转换为List[Dict]格式
        return df.to_dict("records")
    except Exception as e:
        raise Exception(f"获取个股人气榜数据失败: {e}")

def test():
    """
    同步测试方法，用于自动化测试
    
    Raises:
        Exception: 当execute方法执行失败时抛出异常
    """
    try:
        # 使用示例参数调用execute方法
        result = asyncio.run(execute(symbol="SZ000665"))
        print(result)
    except Exception as e:
        raise Exception(f"测试执行失败: {e}")

if __name__ == "__main__":
    # 演示如何调用异步函数
    async def main():
        try:
            result = await execute(symbol="SZ000665")
            print(result)
        except Exception as e:
            print(f"执行出错: {e}")
    
    asyncio.run(main())