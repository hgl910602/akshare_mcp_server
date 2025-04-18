import asyncio
from typing import List, Dict, Any
import akshare as ak
import pandas as pd

async def execute(date: str = '20241009') -> List[Dict[str, Any]]:
    """
    东方财富网-行情中心-涨停板行情-强势股池
    
    Args:
        date: 日期, 格式为'YYYYMMDD'
    
    Returns:
        List[Dict[str, Any]]: 强势股池数据列表
    
    Raises:
        Exception: 当接口调用或数据处理出错时抛出
    """
    try:
        # 调用akshare接口获取数据
        df = ak.stock_zt_pool_strong_em(date=date)
        
        # 处理数据为List[Dict]格式
        if not df.empty:
            # 转换NaN为None
            df = df.where(pd.notnull(df), None)
            # 转换数据类型
            df['序号'] = df['序号'].astype(int) if '序号' in df.columns else None
            return df.to_dict('records')
        return []
    except Exception as e:
        raise Exception(f"获取强势股池数据失败: {e}")

def test():
    """
    同步测试方法
    
    Raises:
        Exception: 当execute方法调用出错时抛出
    """
    try:
        # 使用示例参数调用execute方法
        result = asyncio.run(execute(date='20241231'))
        print(result)
    except Exception as e:
        raise Exception(f"测试失败: {e}")

if __name__ == '__main__':
    # 演示如何调用异步函数
    async def main():
        try:
            data = await execute(date='20241231')
            print(data)
        except Exception as e:
            print(f"Error: {e}")
    
    asyncio.run(main())