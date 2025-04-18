import asyncio
from typing import List, Dict, Any
import akshare as ak

async def execute(symbol: str, adjust: str = "") -> List[Dict[str, Any]]:
    """
    异步获取东方财富网-概念板-行情中心-日K-筹码分布数据
    
    Args:
        symbol: 股票代码
        adjust: 复权类型, "qfq": 前复权, "hfq": 后复权, "": 不复权
        
    Returns:
        返回筹码分布数据列表,每个元素为包含字段的字典
        
    Raises:
        Exception: 当获取数据失败时抛出异常
    """
    try:
        # 调用akshare同步接口,使用await包装
        loop = asyncio.get_running_loop()
        df = await loop.run_in_executor(None, ak.stock_cyq_em, symbol, adjust)
        
        # 将DataFrame转换为List[Dict]格式
        result = df.to_dict("records")
        return result
    except Exception as e:
        raise Exception(f"获取筹码分布数据失败: {str(e)}")

def test():
    """
    同步测试方法,用于自动化测试
    
    Returns:
        返回execute方法的执行结果
        
    Raises:
        直接抛出execute方法可能产生的异常
    """
    # 使用示例参数调用
    return asyncio.run(execute(symbol="000001", adjust=""))

if __name__ == "__main__":
    # 演示如何调用异步函数
    async def main():
        try:
            data = await execute(symbol="000001", adjust="")
            print(data)
        except Exception as e:
            print(f"Error: {e}")
    
    asyncio.run(main())