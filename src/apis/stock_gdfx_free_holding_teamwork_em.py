import asyncio
from typing import List, Dict, Any
import akshare as ak

async def execute(symbol: str = "社保") -> List[Dict[str, Any]]:
    """
    东方财富网-数据中心-股东分析-股东协同-十大流通股东
    
    Parameters
    ----------
    symbol : str, optional
        股东类型, by default "社保"
        choice of {"全部", "个人", "基金", "QFII", "社保", "券商", "信托"}
    
    Returns
    -------
    List[Dict[str, Any]]
        十大流通股东协同数据
    
    Raises
    ------
    Exception
        当获取数据失败时抛出异常
    """
    try:
        # 调用akshare接口获取数据
        df = ak.stock_gdfx_free_holding_teamwork_em(symbol=symbol)
        # 将DataFrame转换为List[Dict]格式
        return df.to_dict("records")
    except Exception as e:
        raise Exception(f"获取股东协同数据失败: {e}")

def test():
    """
    同步测试方法，用于自动化测试
    
    Raises
    ------
    Exception
        当execute方法执行失败时抛出异常
    """
    try:
        # 使用asyncio.run运行异步方法
        result = asyncio.run(execute(symbol="社保"))
        print(result)
    except Exception as e:
        raise Exception(f"测试执行失败: {e}")

if __name__ == "__main__":
    # 演示如何调用异步函数并打印结果
    async def main():
        try:
            data = await execute(symbol="社保")
            print(data)
        except Exception as e:
            print(f"Error: {e}")
    
    asyncio.run(main())