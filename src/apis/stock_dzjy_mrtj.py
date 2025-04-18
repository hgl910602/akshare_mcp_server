import asyncio
from typing import List, Dict, Any
import akshare as ak
import pandas as pd

async def execute(start_date: str, end_date: str) -> List[Dict[str, Any]]:
    """
    异步获取大宗交易每日统计数据
    
    Args:
        start_date: 开始日期，格式如'20220105'
        end_date: 结束日期，格式如'20220105'
        
    Returns:
        返回大宗交易每日统计数据的字典列表
        
    Raises:
        Exception: 当akshare接口调用失败时抛出异常
    """
    try:
        # 调用akshare接口获取数据
        df = ak.stock_dzjy_mrtj(start_date=start_date, end_date=end_date)
        
        # 将DataFrame转换为字典列表
        if not df.empty:
            # 处理可能的NaN值
            df = df.fillna(0)
            return df.to_dict('records')
        return []
    except Exception as e:
        raise Exception(f"获取大宗交易每日统计数据失败: {str(e)}")

def test():
    """
    同步测试方法，用于自动化测试
    
    Raises:
        当execute方法调用失败时抛出异常
    """
    try:
        # 使用示例参数调用execute方法
        result = asyncio.run(execute(start_date='20220105', end_date='20220105'))
        print("测试成功，返回数据条数:", len(result))
        return result
    except Exception as e:
        print("测试失败:", str(e))
        raise

if __name__ == '__main__':
    # 演示如何调用该函数
    async def main():
        try:
            data = await execute(start_date='20220105', end_date='20220105')
            print("获取到的数据:")
            for item in data[:5]:  # 只打印前5条记录
                print(item)
        except Exception as e:
            print(f"发生错误: {str(e)}")
    
    asyncio.run(main())