import asyncio
from typing import List, Dict, Any
import akshare as ak

async def execute(symbol: str = "全称变更") -> List[Dict[str, Any]]:
    """
    异步获取深证证券交易所股票名称变更数据
    
    Args:
        symbol: 变更类型，"全称变更" 或 "简称变更"
        
    Returns:
        返回名称变更数据列表，每个元素为一个字典
        
    Raises:
        Exception: 当akshare接口调用失败时抛出异常
    """
    try:
        # 调用akshare同步接口，使用run_in_executor避免阻塞事件循环
        loop = asyncio.get_running_loop()
        df = await loop.run_in_executor(None, ak.stock_info_sz_change_name, symbol)
        return df.to_dict("records")
    except Exception as e:
        raise Exception(f"获取深证股票名称变更数据失败: {e}")

def test() -> List[Dict[str, Any]]:
    """
    同步测试方法，用于自动化测试
    
    Returns:
        返回名称变更数据列表
        
    Raises:
        直接抛出execute方法中的异常
    """
    return asyncio.run(execute(symbol="全称变更"))

if __name__ == "__main__":
    # 演示如何调用异步函数
    async def main():
        try:
            data = await execute(symbol="全称变更")
            print(data[:2])  # 打印前两条数据示例
        except Exception as e:
            print(f"Error: {e}")
    
    asyncio.run(main())