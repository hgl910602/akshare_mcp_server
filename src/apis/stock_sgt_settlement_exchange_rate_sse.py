import asyncio
from typing import List, Dict, Any
import akshare as ak

async def execute() -> List[Dict[str, Any]]:
    """
    获取沪港通-港股通信息披露-结算汇兑数据
    
    Returns:
        List[Dict[str, Any]]: 结算汇兑数据列表，每个字典代表一条记录
        
    Raises:
        Exception: 当获取数据失败时抛出异常
    """
    try:
        # 调用akshare接口获取数据
        df = ak.stock_sgt_settlement_exchange_rate_sse()
        
        # 将DataFrame转换为List[Dict]格式
        result = df.to_dict(orient="records")
        return result
    except Exception as e:
        raise Exception(f"获取沪港通结算汇兑数据失败: {e}")


def test() -> List[Dict[str, Any]]:
    """
    同步测试方法，用于自动化测试
    
    Returns:
        List[Dict[str, Any]]: 结算汇兑数据列表
        
    Raises:
        原样抛出execute方法中的异常
    """
    return asyncio.run(execute())


if __name__ == "__main__":
    # 演示如何调用异步函数
    async def main():
        try:
            data = await execute()
            print(data)
        except Exception as e:
            print(f"Error: {e}")
    
    asyncio.run(main())