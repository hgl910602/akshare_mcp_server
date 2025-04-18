import asyncio
from typing import List, Dict, Any
import akshare as ak

async def execute() -> List[Dict[str, Any]]:
    """
    异步获取同花顺-数据中心-技术选股-险资举牌数据
    
    Returns:
        List[Dict[str, Any]]: 险资举牌数据列表，每个元素是一个字典代表一行数据
        
    Raises:
        Exception: 当akshare接口调用失败时抛出异常
    """
    try:
        # 调用akshare同步接口，使用asyncio.to_thread转为异步
        df = await asyncio.to_thread(ak.stock_rank_xzjp_ths)
        # 将DataFrame转换为List[Dict]格式
        return df.to_dict("records")
    except Exception as e:
        raise Exception(f"获取险资举牌数据失败: {e}")

def test() -> List[Dict[str, Any]]:
    """
    同步测试函数，用于自动化测试
    
    Returns:
        List[Dict[str, Any]]: 险资举牌数据
        
    Raises:
        Exception: 当execute方法调用失败时抛出异常
    """
    return asyncio.run(execute())

if __name__ == "__main__":
    # 演示如何调用异步函数
    async def main():
        try:
            data = await execute()
            print(data[:2])  # 打印前两条数据
        except Exception as e:
            print(f"Error: {e}")
    
    asyncio.run(main())