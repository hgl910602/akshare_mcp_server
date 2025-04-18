import asyncio
from typing import List, Dict, Any
import akshare as ak
import pandas as pd

async def execute(date: str) -> List[Dict[str, Any]]:
    """
    异步获取东方财富-数据中心-年报季报-资产负债表数据
    
    Args:
        date: 财报日期，格式为"YYYY0331", "YYYY0630", "YYYY0930"或"YYYY1231"
    
    Returns:
        返回处理后的资产负债表数据列表，每个元素为一个字典
        
    Raises:
        ValueError: 当输入参数不符合要求时
        Exception: 当获取数据失败时
    """
    if not date or len(date) != 8 or not date.isdigit():
        raise ValueError("date参数格式不正确，应为8位数字如'20240331'")
    
    try:
        # 调用akshare同步接口获取数据
        df = ak.stock_zcfz_em(date=date)
        
        # 处理NaN值为None
        df = df.where(pd.notnull(df), None)
        
        # 转换为List[Dict]格式
        result = df.to_dict(orient='records')
        return result
    except Exception as e:
        raise Exception(f"获取资产负债表数据失败: {str(e)}")

def test():
    """
    同步测试方法，用于自动化测试
    
    Returns:
        返回execute方法的执行结果
        
    Raises:
        直接抛出execute方法可能产生的异常
    """
    # 使用示例参数调用
    date = "20240331"
    return asyncio.run(execute(date))

if __name__ == '__main__':
    # 演示如何调用异步函数
    async def main():
        try:
            data = await execute(date="20240331")
            print(f"获取到{len(data)}条资产负债表数据")
            if data:
                print("第一条数据示例:")
                print(data[0])
        except Exception as e:
            print(f"发生错误: {e}")
    
    asyncio.run(main())