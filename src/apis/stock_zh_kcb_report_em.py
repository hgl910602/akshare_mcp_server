import asyncio
from typing import List, Dict, Any
import akshare as ak
import pandas as pd

async def execute(from_page: int = 1, to_page: int = 100) -> List[Dict[str, Any]]:
    """
    异步获取东方财富-科创板报告数据
    
    Args:
        from_page: 起始页码，默认为1
        to_page: 结束页码，默认为100
        
    Returns:
        List[Dict[str, Any]]: 科创板公告数据列表
        
    Raises:
        Exception: 当数据获取失败时抛出异常
    """
    try:
        # 调用akshare同步接口，使用run_in_executor避免阻塞事件循环
        loop = asyncio.get_event_loop()
        df = await loop.run_in_executor(
            None, 
            lambda: ak.stock_zh_kcb_report_em(from_page=from_page, to_page=to_page)
        )
        
        # 将DataFrame转换为List[Dict]格式
        if not df.empty:
            return df.to_dict("records")
        return []
    except Exception as e:
        raise Exception(f"获取科创板报告数据失败: {e}")

def test():
    """
    同步测试方法，用于自动化测试
    
    Returns:
        List[Dict[str, Any]]: 科创板公告数据列表
        
    Raises:
        Exception: 当数据获取失败时抛出异常
    """
    try:
        return asyncio.run(execute(from_page=1, to_page=2))
    except Exception as e:
        raise e

if __name__ == "__main__":
    # 示例调用
    async def main():
        try:
            data = await execute(from_page=1, to_page=2)
            for item in data:
                print(item)
        except Exception as e:
            print(f"Error: {e}")
    
    asyncio.run(main())