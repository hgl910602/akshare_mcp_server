import asyncio
from typing import List, Dict, Any
import akshare as ak

async def execute() -> List[Dict[str, Any]]:
    """
    异步获取东方财富-财经早餐数据
    
    Returns:
        List[Dict[str, Any]]: 财经早餐数据列表，每个元素包含标题、摘要、发布时间和链接
    """
    try:
        # 调用akshare的同步接口，使用asyncio.to_thread在异步环境中运行
        df = await asyncio.to_thread(ak.stock_info_cjzc_em)
        # 将DataFrame转换为List[Dict]格式
        return df.to_dict("records")
    except Exception as e:
        raise Exception(f"获取财经早餐数据失败: {e}")

def test() -> List[Dict[str, Any]]:
    """
    同步测试函数，用于自动化测试
    
    Returns:
        List[Dict[str, Any]]: 财经早餐数据列表
        
    Raises:
        Exception: 当execute方法执行失败时抛出异常
    """
    return asyncio.run(execute())

if __name__ == "__main__":
    # 演示如何调用异步函数
    async def main():
        try:
            data = await execute()
            print(data[:2])  # 打印前两条数据示例
        except Exception as e:
            print(f"Error: {e}")
    
    asyncio.run(main())