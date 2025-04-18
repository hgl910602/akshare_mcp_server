import asyncio
from typing import List, Dict, Any
import akshare as ak

async def execute(symbol: str, token: float = None, timeout: float = None) -> List[Dict[str, Any]]:
    """
    雪球-行情中心-个股实时行情数据
    
    Args:
        symbol: 证券代码，可以是 A 股个股代码，A 股场内基金代码，A 股指数，美股代码, 美股指数
        token: 默认不设置token
        timeout: 默认不设置超时参数
        
    Returns:
        List[Dict[str, Any]]: 返回处理后的行情数据列表
        
    Raises:
        Exception: 当获取数据失败时抛出异常
    """
    try:
        # 调用akshare接口获取数据
        df = ak.stock_individual_spot_xq(symbol=symbol, token=token, timeout=timeout)
        # 将DataFrame转换为List[Dict]格式
        result = df.to_dict(orient='records')
        return result
    except Exception as e:
        raise Exception(f"Failed to fetch stock individual spot data from xueqiu: {str(e)}")

def test():
    """
    同步测试方法，用于自动化测试
    
    Raises:
        Exception: 当execute方法执行失败时抛出异常
    """
    try:
        # 使用示例参数调用execute方法
        result = asyncio.run(execute(symbol="SH600000"))
        print("Test executed successfully")
        return result
    except Exception as e:
        print(f"Test failed: {str(e)}")
        raise

if __name__ == '__main__':
    # 演示如何调用异步函数并打印结果
    async def main():
        try:
            data = await execute(symbol="SH600000")
            print(data)
        except Exception as e:
            print(f"Error: {str(e)}")
    
    asyncio.run(main())