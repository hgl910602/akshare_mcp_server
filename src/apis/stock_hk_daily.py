import asyncio
from typing import Any, Dict, List
import akshare as ak

async def execute(symbol: str, adjust: str = "") -> List[Dict[str, Any]]:
    """
    异步获取港股历史行情数据
    
    Args:
        symbol: 港股代码
        adjust: 复权类型，可选值: "", "qfq", "hfq", "qfq-factor", "hfq-factor"
    
    Returns:
        返回包含历史行情数据的字典列表
    
    Raises:
        Exception: 当获取数据失败时抛出异常
    """
    try:
        # 使用akshare同步接口获取数据
        df = ak.stock_hk_daily(symbol=symbol, adjust=adjust)
        
        # 将DataFrame转换为字典列表
        result = df.to_dict(orient="records")
        return result
    except Exception as e:
        raise Exception(f"Failed to fetch HK stock daily data: {str(e)}")

def test():
    """
    同步测试方法，用于验证execute函数
    
    Raises:
        任何execute方法可能抛出的异常
    """
    try:
        # 使用示例参数调用execute方法
        result = asyncio.run(execute(symbol="00700", adjust="hfq-factor"))
        print("Test executed successfully")
        return result
    except Exception as e:
        print(f"Test failed: {str(e)}")
        raise

if __name__ == "__main__":
    # 演示如何调用异步函数
    async def main():
        try:
            data = await execute(symbol="00700", adjust="hfq-factor")
            print(data[:5])  # 打印前5条数据
        except Exception as e:
            print(f"Error occurred: {str(e)}")
    
    asyncio.run(main())