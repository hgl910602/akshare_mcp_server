import asyncio
from typing import List, Dict, Any
import akshare as ak
import pandas as pd

async def execute(date: str = "20240331") -> List[Dict[str, Any]]:
    """
    东方财富-数据中心-年报季报-业绩快报-利润表(异步实现)
    
    Args:
        date: 财报日期,格式为"YYYY0331", "YYYY0630", "YYYY0930", "YYYY1231"之一,从20120331开始
    
    Returns:
        List[Dict[str, Any]]: 利润表数据列表,每个元素为一条记录
        
    Raises:
        ValueError: 当输入参数不合法时抛出
        Exception: 当接口调用失败时抛出
    """
    try:
        # 验证日期格式
        if len(date) != 8 or not date.isdigit():
            raise ValueError("日期格式应为YYYY0331/0630/0930/1231")
        
        # 调用akshare接口获取数据
        df = ak.stock_lrb_em(date=date)
        
        # 将DataFrame转换为List[Dict]
        result = df.to_dict("records")
        
        return result
    except Exception as e:
        raise Exception(f"获取利润表数据失败: {str(e)}")

def test():
    """
    同步测试方法,用于自动化测试
    
    Returns:
        List[Dict[str, Any]]: 利润表数据列表
        
    Raises:
        原样抛出execute方法可能抛出的异常
    """
    # 使用示例参数调用
    return asyncio.run(execute(date="20240331"))

if __name__ == "__main__":
    # 演示如何调用异步函数
    async def main():
        try:
            data = await execute(date="20240331")
            for item in data[:3]:  # 打印前3条记录
                print(item)
        except Exception as e:
            print(f"Error: {e}")
    
    asyncio.run(main())