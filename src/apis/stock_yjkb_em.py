import asyncio
from typing import List, Dict, Any
import akshare as ak
import pandas as pd

async def execute(date: str) -> List[Dict[str, Any]]:
    """
    异步获取东方财富-数据中心-年报季报-业绩快报数据
    
    Args:
        date: 报告日期，格式为"XXXX0331", "XXXX0630", "XXXX0930", "XXXX1231"之一
        
    Returns:
        业绩快报数据列表，每个元素为一个字典
        
    Raises:
        ValueError: 当输入参数不合法时
        Exception: 当获取数据失败时
    """
    if not date or len(date) != 8 or not date.isdigit():
        raise ValueError("date参数格式不正确，应为'XXXX0331'等8位数字格式")
    
    try:
        # 调用akshare同步接口，使用await在异步环境中运行
        df = await asyncio.get_event_loop().run_in_executor(
            None, ak.stock_yjkb_em, date
        )
        
        # 将DataFrame转换为List[Dict]格式
        if not df.empty:
            return df.to_dict("records")
        return []
    except Exception as e:
        raise Exception(f"获取业绩快报数据失败: {str(e)}")

def test():
    """
    同步测试方法，用于自动化测试
    
    Returns:
        业绩快报数据列表
        
    Raises:
        原样抛出execute方法可能抛出的异常
    """
    # 使用示例中的参数进行测试
    test_date = "20200331"
    return asyncio.run(execute(test_date))

if __name__ == "__main__":
    # 演示如何调用异步函数
    async def main():
        try:
            data = await execute("20200331")
            print(f"获取到{len(data)}条数据")
            if data:
                print("第一条数据示例:")
                print(data[0])
        except Exception as e:
            print(f"发生错误: {e}")
    
    asyncio.run(main())