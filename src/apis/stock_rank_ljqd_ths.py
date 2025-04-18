import asyncio
from typing import List, Dict, Any
import akshare as ak
import pandas as pd

async def execute() -> List[Dict[str, Any]]:
    """
    异步获取同花顺-数据中心-技术选股-量价齐跌数据
    
    Returns:
        List[Dict[str, Any]]: 量价齐跌股票数据列表
    """
    try:
        # 调用akshare接口获取数据
        df = ak.stock_rank_ljqd_ths()
        
        # 将DataFrame转换为List[Dict]格式
        result = []
        if not df.empty:
            # 处理可能的NaN值
            df = df.fillna('')
            result = df.to_dict('records')
        return result
    except Exception as e:
        raise Exception(f"获取量价齐跌数据失败: {str(e)}")

def test() -> List[Dict[str, Any]]:
    """
    同步测试方法，用于自动化测试
    
    Returns:
        List[Dict[str, Any]]: 量价齐跌股票数据列表
        
    Raises:
        Exception: 当execute方法执行失败时抛出
    """
    try:
        return asyncio.run(execute())
    except Exception as e:
        raise Exception(f"测试执行失败: {str(e)}")

if __name__ == '__main__':
    # 演示如何调用异步函数
    async def main():
        try:
            data = await execute()
            print(f"获取到{len(data)}条量价齐跌数据:")
            for item in data[:5]:  # 打印前5条数据
                print(item)
        except Exception as e:
            print(f"执行出错: {e}")
    
    asyncio.run(main())