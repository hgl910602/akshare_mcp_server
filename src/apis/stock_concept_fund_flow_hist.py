import asyncio
from typing import List, Dict, Any
import akshare as ak

async def execute(symbol: str) -> List[Dict[str, Any]]:
    """
    异步获取东方财富概念历史资金流数据
    
    Args:
        symbol: 概念名称，如"数据要素"
        
    Returns:
        概念历史资金流数据列表，每个元素为字典格式
        
    Raises:
        Exception: 当akshare接口调用失败时抛出异常
    """
    try:
        # 调用akshare同步接口，使用await在异步环境中执行
        df = await asyncio.get_event_loop().run_in_executor(
            None, 
            ak.stock_concept_fund_flow_hist, 
            symbol
        )
        
        # 将DataFrame转换为List[Dict]格式
        result = df.to_dict(orient='records')
        return result
    except Exception as e:
        raise Exception(f"获取概念历史资金流数据失败: {e}")

def test():
    """
    同步测试方法，用于自动化测试
    
    Raises:
        直接抛出execute方法中出现的异常
    """
    symbol = "数据要素"  # 使用示例中的参数
    return asyncio.run(execute(symbol))

if __name__ == '__main__':
    # 演示如何调用异步函数
    async def main():
        try:
            data = await execute(symbol="数据要素")
            print(data[:2])  # 打印前两条数据
        except Exception as e:
            print(f"Error: {e}")

    asyncio.run(main())