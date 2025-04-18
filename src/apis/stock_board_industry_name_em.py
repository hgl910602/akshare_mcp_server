import asyncio
from typing import List, Dict, Any
import akshare as ak
import pandas as pd

async def execute() -> List[Dict[str, Any]]:
    """
    异步获取东方财富-沪深京板块-行业板块数据
    
    Returns:
        List[Dict[str, Any]]: 行业板块数据列表，每个元素为一个板块的字典数据
        
    Raises:
        Exception: 当获取数据失败时抛出异常
    """
    try:
        # 调用akshare的同步接口，使用await在异步环境中执行
        df = await asyncio.get_event_loop().run_in_executor(
            None, 
            ak.stock_board_industry_name_em
        )
        
        # 将DataFrame转换为List[Dict]格式
        if not df.empty:
            return df.to_dict(orient='records')
        return []
    except Exception as e:
        raise Exception(f"获取行业板块数据失败: {str(e)}")

def test() -> List[Dict[str, Any]]:
    """
    同步测试方法，用于自动化测试
    
    Returns:
        List[Dict[str, Any]]: 行业板块数据列表
        
    Raises:
        Exception: 当execute方法执行失败时抛出异常
    """
    return asyncio.run(execute())

if __name__ == '__main__':
    # 演示如何调用异步函数
    async def main():
        try:
            data = await execute()
            print(f"获取到{len(data)}条行业板块数据")
            if data:
                print("第一条数据示例:")
                print(data[0])
        except Exception as e:
            print(f"执行出错: {e}")
    
    asyncio.run(main())