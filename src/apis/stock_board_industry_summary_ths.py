import asyncio
from typing import List, Dict, Any
import akshare as ak
import pandas as pd

async def execute() -> List[Dict[str, Any]]:
    """
    异步获取同花顺行业一览表数据
    
    Returns:
        List[Dict[str, Any]]: 行业板块数据列表，每个元素为一个字典表示一行数据
        
    Raises:
        Exception: 当数据获取失败时抛出异常
    """
    try:
        # 调用akshare接口获取数据
        df = ak.stock_board_industry_summary_ths()
        
        # 将DataFrame转换为List[Dict]格式
        result = df.to_dict(orient='records')
        
        return result
    except Exception as e:
        raise Exception(f"获取同花顺行业一览表数据失败: {e}")

def test() -> List[Dict[str, Any]]:
    """
    同步测试方法，用于自动化测试
    
    Returns:
        List[Dict[str, Any]]: 行业板块数据列表
        
    Raises:
        原样抛出execute方法中的异常
    """
    return asyncio.run(execute())

if __name__ == '__main__':
    # 演示如何调用异步函数
    async def main():
        try:
            data = await execute()
            print(f"获取到{len(data)}条行业数据:")
            for item in data[:3]:  # 打印前3条数据作为示例
                print(item)
        except Exception as e:
            print(f"发生错误: {e}")
    
    asyncio.run(main())