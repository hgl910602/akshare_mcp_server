import asyncio
from typing import List, Dict, Any
import akshare as ak
import pandas as pd

async def execute(date: str) -> List[Dict[str, Any]]:
    """
    异步获取上海证券交易所融资融券明细数据
    
    Args:
        date: 日期, 格式如 "20210205"
        
    Returns:
        融资融券明细数据列表，每个元素为一个字典
        
    Raises:
        Exception: 当akshare接口调用失败时抛出异常
    """
    try:
        # 调用akshare接口获取数据
        df = ak.stock_margin_detail_sse(date=date)
        
        # 将DataFrame转换为List[Dict]格式
        result = df.to_dict(orient="records")
        
        return result
    except Exception as e:
        raise Exception(f"获取上海证券交易所融资融券明细数据失败: {e}")

def test():
    """
    同步测试方法，用于自动化测试
    
    Raises:
        Exception: 当execute方法调用失败时抛出异常
    """
    # 使用示例中的日期参数
    test_date = "20230922"
    try:
        result = asyncio.run(execute(date=test_date))
        print(f"测试成功，获取到{len(result)}条数据")
    except Exception as e:
        raise Exception(f"测试失败: {e}")

if __name__ == "__main__":
    # 演示如何调用该函数
    async def main():
        try:
            # 使用示例参数调用
            data = await execute(date="20230922")
            print(f"获取到{len(data)}条数据:")
            # 打印前5条数据
            for i, item in enumerate(data[:5], 1):
                print(f"第{i}条: {item}")
        except Exception as e:
            print(f"调用失败: {e}")
    
    asyncio.run(main())