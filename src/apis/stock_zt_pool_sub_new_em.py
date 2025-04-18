import asyncio
from typing import List, Dict, Any
import akshare as ak
import pandas as pd

async def execute(date: str = '20241231') -> List[Dict[str, Any]]:
    """
    东方财富网-行情中心-涨停板行情-次新股池
    
    Args:
        date: 日期, 格式为'YYYYMMDD'
        
    Returns:
        List[Dict[str, Any]]: 返回次新股池数据列表
        
    Raises:
        Exception: 当获取数据失败时抛出异常
    """
    try:
        # 调用akshare接口获取数据
        df = ak.stock_zt_pool_sub_new_em(date=date)
        
        # 处理NaN值
        df = df.fillna('')
        
        # 转换DataFrame为List[Dict]
        result = df.to_dict('records')
        
        # 转换数据类型
        for item in result:
            for key, value in item.items():
                if pd.isna(value):
                    item[key] = None
                elif isinstance(value, (pd.Timestamp, pd.Timedelta)):
                    item[key] = str(value)
                    
        return result
    except Exception as e:
        raise Exception(f"获取次新股池数据失败: {str(e)}")

def test():
    """
    同步测试方法
    """
    try:
        # 使用示例参数调用execute方法
        result = asyncio.run(execute(date='20241231'))
        print(result)
        return result
    except Exception as e:
        print(f"测试失败: {str(e)}")
        raise

if __name__ == '__main__':
    # 演示如何调用该函数
    async def main():
        try:
            data = await execute(date='20241231'))
            print(data)
        except Exception as e:
            print(f"Error: {str(e)}")
    
    asyncio.run(main())