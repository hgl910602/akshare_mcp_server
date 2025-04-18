import asyncio
from typing import List, Dict, Any
import akshare as ak
import pandas as pd

async def execute(date: str) -> List[Dict[str, Any]]:
    """
    异步获取东方财富-数据中心-年报季报-业绩快报-现金流量表数据
    
    Args:
        date: 财报日期，格式为"YYYY0331", "YYYY0630", "YYYY0930"或"YYYY1231"
        
    Returns:
        返回处理后的现金流量表数据列表，每个元素为包含字段的字典
        
    Raises:
        Exception: 当akshare接口调用失败或数据处理出错时抛出异常
    """
    try:
        # 调用akshare接口获取数据
        df = await asyncio.to_thread(ak.stock_xjll_em, date=date)
        
        # 处理数据为List[Dict]格式
        if not df.empty:
            # 替换NaN为None，方便JSON序列化
            df = df.where(pd.notnull(df), None)
            return df.to_dict(orient='records')
        return []
    except Exception as e:
        raise Exception(f"获取现金流量表数据失败: {str(e)}")

def test():
    """
    同步测试方法，用于自动化测试
    
    Returns:
        返回execute方法的执行结果
        
    Raises:
        直接抛出execute方法可能产生的异常
    """
    # 使用示例参数调用
    return asyncio.run(execute(date="20240331"))

if __name__ == '__main__':
    # 演示如何调用异步函数
    async def main():
        try:
            data = await execute(date="20240331")
            print(f"获取到{len(data)}条数据")
            if data:
                print("第一条数据示例:")
                print(data[0])
        except Exception as e:
            print(f"调用失败: {e}")
    
    asyncio.run(main())