import asyncio
from typing import List, Dict, Any
import akshare as ak
import pandas as pd

async def execute(symbol: str = '债券', start_date: str = '20220104', end_date: str = '20220104') -> List[Dict[str, Any]]:
    """
    异步获取东方财富网-数据中心-大宗交易-每日明细数据
    
    Args:
        symbol: 证券类型, 可选 {'A股', 'B股', '基金', '债券'}
        start_date: 开始日期, 格式: 'YYYYMMDD'
        end_date: 结束日期, 格式: 'YYYYMMDD'
    
    Returns:
        返回大宗交易每日明细数据列表, 每个元素为字典格式
    
    Raises:
        Exception: 当akshare接口调用失败时抛出异常
    """
    try:
        # 调用akshare接口获取数据
        df = ak.stock_dzjy_mrmx(symbol=symbol, start_date=start_date, end_date=end_date)
        
        # 处理返回结果
        if not isinstance(df, pd.DataFrame) or df.empty:
            return []
            
        # 转换DataFrame为List[Dict]
        result = df.to_dict(orient='records')
        return result
    except Exception as e:
        raise Exception(f"获取大宗交易每日明细数据失败: {str(e)}")

def test():
    """
    同步测试方法, 用于自动化测试
    
    Raises:
        直接抛出execute方法中的异常
    """
    try:
        # 使用示例参数调用
        result = asyncio.run(execute(symbol='债券', start_date='20220104', end_date='20220104'))
        print(f"测试成功, 获取到{len(result)}条数据")
        return result
    except Exception as e:
        print(f"测试失败: {str(e)}")
        raise

if __name__ == '__main__':
    # 演示如何调用异步函数
    async def main():
        try:
            data = await execute(symbol='债券', start_date='20220104', end_date='20220104')
            print(f"获取到{len(data)}条数据:")
            for item in data[:3]:  # 打印前3条数据
                print(item)
        except Exception as e:
            print(f"调用失败: {str(e)}")
    
    asyncio.run(main())