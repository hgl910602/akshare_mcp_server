import asyncio
from typing import List, Dict, Any
import akshare as ak
import pandas as pd

async def execute() -> List[Dict[str, Any]]:
    """
    获取东方财富网-数据中心-新股申购-打新收益率数据
    
    Returns:
        List[Dict[str, Any]]: 打新收益率数据列表，每个元素为一个字典代表一行数据
        
    Raises:
        Exception: 当获取数据失败时抛出异常
    """
    try:
        # 调用akshare同步接口获取数据
        df = ak.stock_dxsyl_em()
        
        # 将DataFrame转换为List[Dict]格式
        if not df.empty:
            # 处理可能的NaN值
            df = df.fillna(0)
            # 转换数据类型
            for col in df.columns:
                if df[col].dtype == 'float64':
                    df[col] = df[col].astype(float)
                elif df[col].dtype == 'int64':
                    df[col] = df[col].astype(int)
            return df.to_dict('records')
        return []
    except Exception as e:
        raise Exception(f"获取打新收益率数据失败: {e}")

def test() -> List[Dict[str, Any]]:
    """
    同步测试方法，用于测试execute函数
    
    Returns:
        List[Dict[str, Any]]: 打新收益率数据列表
        
    Raises:
        Exception: 当execute执行失败时抛出异常
    """
    try:
        return asyncio.run(execute())
    except Exception as e:
        raise Exception(f"测试execute方法失败: {e}")

if __name__ == '__main__':
    # 演示如何调用异步函数
    async def main():
        try:
            data = await execute()
            print(f"获取到{len(data)}条打新收益率数据")
            if data:
                print("第一条数据示例:")
                print(data[0])
        except Exception as e:
            print(f"执行出错: {e}")
    
    asyncio.run(main())