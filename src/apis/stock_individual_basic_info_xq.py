import asyncio
from typing import List, Dict, Any
import akshare as ak

async def execute(symbol: str, token: str = None, timeout: float = None) -> List[Dict[str, Any]]:
    """
    异步获取雪球财经个股公司简介信息
    
    Args:
        symbol: 股票代码，如 "SH601127"
        token: 可选token参数
        timeout: 可选超时时间
        
    Returns:
        返回包含公司简介信息的字典列表
        
    Raises:
        Exception: 当接口调用失败时抛出异常
    """
    try:
        # 调用akshare的同步接口，使用await asyncio.to_thread在异步环境中运行
        result = await asyncio.to_thread(
            ak.stock_individual_basic_info_xq,
            symbol=symbol,
            token=token,
            timeout=timeout
        )
        # 将结果转换为List[Dict]格式
        return result.to_dict(orient='records')
    except Exception as e:
        raise Exception(f"Failed to fetch stock basic info: {str(e)}")

def test():
    """
    同步测试方法，用于自动化测试
    
    Raises:
        原样抛出execute方法中的异常
    """
    # 使用示例参数调用execute方法
    result = asyncio.run(execute(symbol="SH601127"))
    return result

if __name__ == '__main__':
    # 演示如何调用异步函数
    async def main():
        try:
            data = await execute(symbol="SH601127")
            print(data)
        except Exception as e:
            print(f"Error occurred: {e}")
    
    asyncio.run(main())