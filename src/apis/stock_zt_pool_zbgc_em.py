import asyncio
from typing import List, Dict, Any
import akshare as ak
import pandas as pd

async def execute(date: str = '20241011') -> List[Dict[str, Any]]:
    """
    异步获取东方财富网-行情中心-涨停板行情-炸板股池数据
    
    Args:
        date: 日期, 格式为'YYYYMMDD'
        
    Returns:
        炸板股池数据列表, 每个元素为包含字段的字典
        
    Raises:
        Exception: 当akshare接口调用失败时抛出
    """
    try:
        # 调用akshare同步接口获取数据
        df = ak.stock_zt_pool_zbgc_em(date=date)
        
        # 将DataFrame转换为List[Dict]格式
        if not df.empty:
            # 处理可能的NaN值
            df = df.fillna('')
            return df.to_dict('records')
        return []
    except Exception as e:
        raise Exception(f"获取炸板股池数据失败: {str(e)}")

def test():
    """
    同步测试方法, 用于自动化测试
    
    Returns:
        炸板股池数据列表
        
    Raises:
        原样抛出execute方法中的异常
    """
    # 使用示例参数调用
    return asyncio.run(execute(date='20241011'))

if __name__ == '__main__':
    # 演示异步调用
    async def main():
        try:
            data = await execute(date='20241011')
            print(f"获取到{len(data)}条炸板股数据:")
            for item in data[:3]:  # 打印前3条作为示例
                print(item)
        except Exception as e:
            print(f"调用失败: {e}")
    
    asyncio.run(main())