import asyncio
from typing import List, Dict, Any
import akshare as ak

async def execute(symbol: str = "阿里巴巴概念") -> List[Dict[str, Any]]:
    """
    异步获取同花顺概念板块简介信息
    
    Args:
        symbol: 概念板块名称，可通过 ak.stock_board_concept_name_ths() 获取所有概念名称
    
    Returns:
        返回包含概念板块简介信息的字典列表
        
    Raises:
        Exception: 当获取数据失败时抛出异常
    """
    try:
        # 调用akshare同步接口，使用await asyncio.to_thread在异步环境中运行同步代码
        df = await asyncio.to_thread(ak.stock_board_concept_info_ths, symbol=symbol)
        # 将DataFrame转换为List[Dict]格式
        return df.to_dict("records")
    except Exception as e:
        raise Exception(f"Failed to fetch stock board concept info: {str(e)}")

def test():
    """
    同步测试方法，用于自动化测试
    
    Raises:
        原样抛出execute方法中出现的异常
    """
    # 使用asyncio.run运行异步方法
    try:
        result = asyncio.run(execute(symbol="阿里巴巴概念"))
        print("Test executed successfully")
        return result
    except Exception as e:
        print(f"Test failed: {str(e)}")
        raise

if __name__ == "__main__":
    # 演示如何调用异步函数
    async def main():
        try:
            data = await execute(symbol="阿里巴巴概念"))
            print(data)
        except Exception as e:
            print(f"Error: {str(e)}")
    
    asyncio.run(main())