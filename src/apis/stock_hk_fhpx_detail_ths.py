import asyncio
from typing import List, Dict, Any
import akshare as ak

async def execute(symbol: str) -> List[Dict[str, Any]]:
    """
    异步获取港股分红派息详情数据
    
    Args:
        symbol: 港股代码，例如 "0700"
        
    Returns:
        返回分红派息详情数据列表，每个条目为字典形式
        
    Raises:
        Exception: 当数据获取失败时抛出异常
    """
    try:
        # 调用akshare同步接口，使用await在异步环境中运行
        df = await asyncio.get_event_loop().run_in_executor(
            None, 
            ak.stock_hk_fhpx_detail_ths, 
            symbol
        )
        # 将DataFrame转换为List[Dict]格式
        return df.to_dict("records")
    except Exception as e:
        raise Exception(f"Failed to fetch stock hk fhpx detail: {str(e)}")

def test():
    """
    同步测试方法，用于自动化测试
    
    Returns:
        返回execute方法的执行结果
        
    Raises:
        原样抛出execute方法中的异常
    """
    # 使用示例参数调用execute方法
    return asyncio.run(execute(symbol="0700"))

if __name__ == "__main__":
    # 演示如何调用异步函数并打印结果
    async def main():
        try:
            data = await execute(symbol="0700")
            print(data)
        except Exception as e:
            print(f"Error occurred: {e}")
    
    asyncio.run(main())