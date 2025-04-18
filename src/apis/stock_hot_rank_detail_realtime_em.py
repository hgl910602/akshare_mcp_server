import asyncio
from typing import List, Dict, Any
import akshare as ak

async def execute(symbol: str = "SZ000665") -> List[Dict[str, Any]]:
    """
    东方财富网-个股人气榜-实时变动
    
    Args:
        symbol: 股票代码，例如 "SZ000665"
    
    Returns:
        List[Dict[str, Any]]: 包含时间、排名等信息的字典列表
        
    Raises:
        Exception: 当接口调用失败时抛出异常
    """
    try:
        # 调用akshare接口获取数据
        df = ak.stock_hot_rank_detail_realtime_em(symbol=symbol)
        # 将DataFrame转换为List[Dict]格式
        return df.to_dict("records")
    except Exception as e:
        raise Exception(f"获取股票实时人气榜失败: {str(e)}")

def test():
    """
    同步测试方法，用于自动化测试
    
    Raises:
        Exception: 当execute方法调用失败时抛出异常
    """
    try:
        result = asyncio.run(execute(symbol="SZ000665"))
        print(result)
    except Exception as e:
        raise Exception(f"测试失败: {str(e)}")

if __name__ == "__main__":
    # 演示如何调用异步函数
    async def main():
        try:
            result = await execute(symbol="SZ000665")
            print(result)
        except Exception as e:
            print(f"Error: {str(e)}")
    
    asyncio.run(main())