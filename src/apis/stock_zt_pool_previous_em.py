import asyncio
from typing import List, Dict, Any
import akshare as ak
import pandas as pd

async def execute(date: str = '20240415') -> List[Dict[str, Any]]:
    """
    获取东方财富网-行情中心-涨停板行情-昨日涨停股池数据
    
    Args:
        date: 日期, 格式为'YYYYMMDD'
        
    Returns:
        List[Dict[str, Any]]: 昨日涨停股池数据列表
        
    Raises:
        Exception: 当获取数据失败时抛出异常
    """
    try:
        # 调用akshare同步接口获取数据
        df = ak.stock_zt_pool_previous_em(date=date)
        
        # 将DataFrame转换为List[Dict]格式
        result = df.to_dict('records')
        
        # 处理可能的NaN值
        for item in result:
            for key, value in item.items():
                if pd.isna(value):
                    item[key] = None
        
        return result
    except Exception as e:
        raise Exception(f"获取昨日涨停股池数据失败: {str(e)}")

def test():
    """
    同步测试方法，用于自动化测试
    
    Raises:
        Exception: 当execute方法执行失败时抛出异常
    """
    try:
        # 使用示例参数调用execute方法
        result = asyncio.run(execute(date='20240415'))
        print(f"获取到{len(result)}条昨日涨停股池数据")
        return result
    except Exception as e:
        raise Exception(f"测试失败: {str(e)}")

if __name__ == '__main__':
    # 演示如何调用异步函数
    async def main():
        try:
            data = await execute(date='20240415')
            print(f"获取到{len(data)}条数据:")
            for item in data[:3]:  # 打印前3条数据
                print(item)
        except Exception as e:
            print(f"发生错误: {e}")
    
    asyncio.run(main())