import asyncio
from typing import List, Dict, Any
import akshare as ak
import pandas as pd

async def execute(symbol: str) -> List[Dict[str, Any]]:
    """
    异步获取东方财富网-数据中心-特色数据-千股千评-市场热度-用户关注指数
    
    Args:
        symbol: 股票代码, 如 "600000"
        
    Returns:
        List[Dict[str, Any]]: 包含用户关注指数的数据列表
        
    Raises:
        Exception: 当获取数据失败时抛出异常
    """
    try:
        # 调用akshare接口获取数据
        df = ak.stock_comment_detail_scrd_focus_em(symbol=symbol)
        
        # 将DataFrame转换为List[Dict]格式
        if not df.empty:
            # 确保列名正确
            df.columns = ["交易日", "用户关注指数"]
            return df.to_dict("records")
        return []
    except Exception as e:
        raise Exception(f"获取股票{symbol}的市场热度数据失败: {str(e)}")

def test():
    """
    同步测试方法，用于验证execute函数
    
    Raises:
        Exception: 当execute执行失败时抛出异常
    """
    # 使用示例中的参数进行测试
    symbol = "600000"
    try:
        result = asyncio.run(execute(symbol=symbol))
        print(f"测试成功，获取到{len(result)}条数据")
        return result
    except Exception as e:
        print(f"测试失败: {str(e)}")
        raise

if __name__ == "__main__":
    # 演示如何调用异步函数
    async def main():
        try:
            data = await execute(symbol="600000")
            print(data)
        except Exception as e:
            print(f"调用失败: {str(e)}")
    
    asyncio.run(main())