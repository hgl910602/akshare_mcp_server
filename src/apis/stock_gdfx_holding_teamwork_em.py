import asyncio
from typing import List, Dict, Any
import akshare as ak

async def execute(symbol: str = "社保") -> List[Dict[str, Any]]:
    """
    东方财富网-数据中心-股东分析-股东协同-十大股东
    
    Args:
        symbol: 股东类型, choice of {"全部", "个人", "基金", "QFII", "社保", "券商", "信托"}
    
    Returns:
        List[Dict[str, Any]]: 返回股东协同数据
        
    Raises:
        Exception: 当获取数据失败时抛出异常
    """
    try:
        # 调用akshare接口获取数据
        df = ak.stock_gdfx_holding_teamwork_em(symbol=symbol)
        
        # 将DataFrame转换为List[Dict]格式
        result = df.to_dict("records")
        return result
    except Exception as e:
        raise Exception(f"获取股东协同数据失败: {e}")

def test():
    """
    同步测试方法，用于自动化测试
    
    Raises:
        Exception: 当execute方法执行失败时抛出异常
    """
    try:
        # 使用asyncio.run调用异步方法
        result = asyncio.run(execute(symbol="社保"))
        print("测试成功，返回数据条数:", len(result))
        return result
    except Exception as e:
        raise Exception(f"测试失败: {e}")

if __name__ == "__main__":
    # 演示如何调用该函数
    async def main():
        try:
            data = await execute(symbol="社保")
            print("获取数据成功:")
            for item in data[:3]:  # 打印前3条数据
                print(item)
        except Exception as e:
            print(f"发生错误: {e}")
    
    asyncio.run(main())