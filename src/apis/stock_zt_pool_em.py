import asyncio
from typing import List, Dict, Any
import akshare as ak
import pandas as pd

async def execute(date: str = '20241008') -> List[Dict[str, Any]]:
    """
    获取东方财富网涨停股池数据
    
    Args:
        date: 日期，格式如'20241008'
    
    Returns:
        涨停股池数据列表，每个元素为包含股票信息的字典
    
    Raises:
        Exception: 当获取数据失败时抛出异常
    """
    try:
        # 调用akshare同步接口获取数据
        df = ak.stock_zt_pool_em(date=date)
        
        # 处理可能的空数据
        if df.empty:
            return []
            
        # 转换DataFrame为List[Dict]
        result = df.to_dict('records')
        
        # 处理可能的NaN值
        for item in result:
            for key, value in item.items():
                if pd.isna(value):
                    item[key] = None
        
        return result
    except Exception as e:
        raise Exception(f"获取涨停股池数据失败: {str(e)}")

def test():
    """
    同步测试方法，用于自动化测试
    
    Raises:
        直接抛出execute方法可能产生的异常
    """
    try:
        # 使用示例参数调用
        result = asyncio.run(execute(date='20241008'))
        return result
    except Exception as e:
        raise e

if __name__ == '__main__':
    # 演示如何调用异步函数
    async def main():
        try:
            data = await execute(date='20241008')
            print(data[:2])  # 打印前两条数据示例
        except Exception as e:
            print(f"Error: {e}")
    
    asyncio.run(main())