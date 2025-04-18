import asyncio
from typing import List, Dict, Any
import akshare as ak

async def execute() -> List[Dict[str, Any]]:
    """
    异步获取东方财富-全球财经快讯数据
    
    Returns:
        List[Dict[str, Any]]: 全球财经快讯数据列表，每个条目包含标题、摘要、发布时间和链接
    """
    try:
        # 调用akshare的同步接口，使用run_in_executor避免阻塞事件循环
        loop = asyncio.get_running_loop()
        df = await loop.run_in_executor(None, ak.stock_info_global_em)
        
        # 将DataFrame转换为List[Dict]格式
        result = df.to_dict(orient='records')
        return result
    except Exception as e:
        raise Exception(f"获取全球财经快讯数据失败: {e}")

def test() -> List[Dict[str, Any]]:
    """
    同步测试方法，用于自动化测试
    
    Returns:
        List[Dict[str, Any]]: 全球财经快讯数据
        
    Raises:
        Exception: 当execute方法执行失败时抛出异常
    """
    try:
        return asyncio.run(execute())
    except Exception as e:
        raise Exception(f"测试执行失败: {e}")

if __name__ == '__main__':
    # 演示如何异步调用该函数
    async def main():
        try:
            data = await execute()
            for item in data[:3]:  # 打印前3条数据
                print(item)
        except Exception as e:
            print(f"Error: {e}")
    
    asyncio.run(main())