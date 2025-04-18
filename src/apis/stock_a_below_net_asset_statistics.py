import asyncio
from typing import List, Dict, Any
import akshare as ak

async def execute(symbol: str = "全部A股") -> List[Dict[str, Any]]:
    """
    异步获取A股破净股统计数据
    
    Args:
        symbol: 股票类型, 可选: "全部A股", "沪深300", "上证50", "中证500"
        
    Returns:
        List[Dict[str, Any]]: 破净股统计数据列表
        
    Raises:
        Exception: 当获取数据失败时抛出异常
    """
    try:
        # 调用akshare同步接口，使用asyncio.to_thread在异步环境中运行同步代码
        df = await asyncio.to_thread(ak.stock_a_below_net_asset_statistics, symbol=symbol)
        return df.to_dict("records")
    except Exception as e:
        raise Exception(f"获取破净股统计数据失败: {e}")

def test():
    """
    同步测试方法，用于自动化测试
    
    Returns:
        List[Dict[str, Any]]: 破净股统计数据列表
        
    Raises:
        Exception: 当获取数据失败时抛出异常
    """
    try:
        # 模拟调用示例中的参数
        return asyncio.run(execute(symbol="沪深300"))
    except Exception as e:
        raise Exception(f"测试失败: {e}")

if __name__ == "__main__":
    # 演示如何调用异步函数
    async def main():
        try:
            data = await execute(symbol="沪深300")
            print(data)
        except Exception as e:
            print(f"Error: {e}")
    
    asyncio.run(main())