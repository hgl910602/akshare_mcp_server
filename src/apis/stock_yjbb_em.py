import asyncio
from typing import List, Dict, Any
import akshare as ak
import pandas as pd

async def execute(date: str) -> List[Dict[str, Any]]:
    """
    异步获取东方财富-数据中心-年报季报-业绩报表数据
    
    Args:
        date: 财报日期，格式为"YYYY0331", "YYYY0630", "YYYY0930"或"YYYY1231"
    
    Returns:
        返回业绩报表数据列表，每个元素为包含各字段的字典
    
    Raises:
        ValueError: 当输入参数不合法时抛出
        Exception: 当获取数据失败时抛出
    """
    if not date or len(date) != 8 or not date.isdigit():
        raise ValueError("date参数格式不正确，应为8位数字如'20200331'")
    
    try:
        # 调用akshare同步接口获取数据
        df = ak.stock_yjbb_em(date=date)
        
        # 处理可能的空数据
        if df.empty:
            return []
            
        # 转换DataFrame为List[Dict]格式
        result = df.to_dict(orient='records')
        return result
    except Exception as e:
        raise Exception(f"获取业绩报表数据失败: {str(e)}")

def test():
    """
    同步测试方法，用于自动化测试
    
    Returns:
        返回业绩报表数据列表
    
    Raises:
        直接抛出execute方法中的异常
    """
    # 使用示例中的参数进行测试
    test_date = "20220331"
    return asyncio.run(execute(date=test_date))

if __name__ == '__main__':
    # 演示如何调用异步函数
    async def main():
        try:
            data = await execute(date="20220331")
            print(f"获取到{len(data)}条数据")
            if data:
                print("第一条数据示例:")
                print(data[0])
        except Exception as e:
            print(f"发生错误: {str(e)}")
    
    asyncio.run(main())