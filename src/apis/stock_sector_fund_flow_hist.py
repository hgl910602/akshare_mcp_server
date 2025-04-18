import asyncio
from typing import List, Dict, Any
import akshare as ak

async def execute(symbol: str) -> List[Dict[str, Any]]:
    """
    获取东方财富网-数据中心-资金流向-行业资金流-行业历史资金流
    
    Args:
        symbol: 行业名称，如"汽车服务"
    
    Returns:
        List[Dict[str, Any]]: 行业历史资金流数据
        
    Raises:
        Exception: 当获取数据失败时抛出异常
    """
    try:
        # 调用akshare接口获取数据
        df = ak.stock_sector_fund_flow_hist(symbol=symbol)
        
        # 将DataFrame转换为List[Dict]格式
        result = df.to_dict(orient="records")
        return result
    except Exception as e:
        raise Exception(f"获取行业历史资金流数据失败: {e}")

def test():
    """
    同步测试方法，用于自动化测试
    
    Returns:
        List[Dict[str, Any]]: 行业历史资金流数据
        
    Raises:
        Exception: 当获取数据失败时抛出异常
    """
    try:
        # 使用示例参数调用execute方法
        result = asyncio.run(execute(symbol="汽车服务"))
        return result
    except Exception as e:
        raise e

if __name__ == "__main__":
    # 演示如何调用异步函数
    async def main():
        try:
            data = await execute(symbol="汽车服务")
            print(data)
        except Exception as e:
            print(f"Error: {e}")
    
    asyncio.run(main())