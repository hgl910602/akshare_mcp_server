import asyncio
from typing import List, Dict, Any
import akshare as ak

async def execute(symbol: str = "500日均线") -> List[Dict[str, Any]]:
    """
    异步获取同花顺-数据中心-技术选股-向下突破数据
    
    Args:
        symbol: 均线类型, 可选值: {"5日均线", "10日均线", "20日均线", "30日均线", 
                              "60日均线", "90日均线", "250日均线", "500日均线"}
    
    Returns:
        List[Dict[str, Any]]: 返回向下突破股票数据列表
    
    Raises:
        Exception: 当akshare接口调用失败时抛出异常
    """
    try:
        # 调用akshare同步接口，使用await在异步环境中执行
        df = await asyncio.get_event_loop().run_in_executor(
            None, 
            ak.stock_rank_xxtp_ths, 
            symbol
        )
        # 将DataFrame转换为List[Dict]格式
        return df.to_dict("records")
    except Exception as e:
        raise Exception(f"获取向下突破数据失败: {str(e)}")

def test():
    """
    同步测试方法，用于自动化测试
    
    Returns:
        List[Dict[str, Any]]: 返回向下突破股票数据列表
    
    Raises:
        Exception: 当execute方法调用失败时抛出异常
    """
    try:
        # 使用asyncio.run运行异步方法
        result = asyncio.run(execute(symbol="500日均线"))
        return result
    except Exception as e:
        raise Exception(f"测试执行失败: {str(e)}")

if __name__ == "__main__":
    # 演示如何调用异步函数
    async def main():
        try:
            data = await execute(symbol="500日均线")
            print(data[:5])  # 打印前5条数据
        except Exception as e:
            print(f"Error: {str(e)}")
    
    asyncio.run(main())