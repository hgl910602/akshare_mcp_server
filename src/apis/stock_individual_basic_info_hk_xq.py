import asyncio
from typing import Any, Dict, List, Optional
import akshare as ak

async def execute(symbol: str, token: Optional[str] = None, timeout: Optional[float] = None) -> List[Dict[str, Any]]:
    """
    异步获取港股个股基本信息(雪球)
    
    Args:
        symbol: 股票代码, 如 "02097"
        token: 可选token
        timeout: 超时时间(秒)
    
    Returns:
        包含个股基本信息的字典列表
        
    Raises:
        Exception: 当接口调用失败时抛出异常
    """
    try:
        # 调用akshare接口获取数据
        df = ak.stock_individual_basic_info_hk_xq(symbol=symbol, token=token, timeout=timeout)
        
        # 将DataFrame转换为字典列表
        result = df.to_dict(orient='records')
        return result
    except Exception as e:
        raise Exception(f"获取港股个股基本信息失败: {str(e)}")

def test():
    """
    同步测试方法，用于自动化测试
    
    Raises:
        任何execute方法可能抛出的异常
    """
    # 使用示例参数调用execute方法
    result = asyncio.run(execute(symbol="02097"))
    return result

if __name__ == '__main__':
    # 演示如何调用该函数
    async def main():
        try:
            data = await execute(symbol="02097")
            print(data)
        except Exception as e:
            print(f"Error: {e}")
    
    asyncio.run(main())