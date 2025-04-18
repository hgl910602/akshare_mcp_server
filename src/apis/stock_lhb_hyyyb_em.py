import asyncio
from typing import List, Dict, Any
import akshare as ak
import pandas as pd

async def execute(start_date: str, end_date: str) -> List[Dict[str, Any]]:
    """
    获取东方财富网-数据中心-龙虎榜单-每日活跃营业部数据
    
    Args:
        start_date: 开始日期, 格式为YYYYMMDD
        end_date: 结束日期, 格式为YYYYMMDD
        
    Returns:
        List[Dict[str, Any]]: 转换后的营业部数据列表
        
    Raises:
        Exception: 当akshare接口调用失败时抛出
    """
    try:
        # 调用akshare接口获取数据
        df = ak.stock_lhb_hyyyb_em(start_date=start_date, end_date=end_date)
        
        # 将DataFrame转换为List[Dict]格式
        result = []
        if not df.empty:
            # 处理可能的NaN值
            df = df.fillna('')
            # 转换数据类型
            df['序号'] = df['序号'].astype(int)
            result = df.to_dict('records')
            
        return result
    except Exception as e:
        raise Exception(f"获取龙虎榜活跃营业部数据失败: {str(e)}")


def test():
    """
    同步测试方法，用于自动化测试
    
    Returns:
        List[Dict[str, Any]]: 营业部数据列表
        
    Raises:
        Exception: 当execute方法调用失败时抛出
    """
    try:
        # 使用示例参数调用execute方法
        return asyncio.run(execute(start_date="20220324", end_date="20220324"))
    except Exception as e:
        raise Exception(f"测试失败: {str(e)}")


if __name__ == '__main__':
    # 演示如何调用异步函数
    async def main():
        try:
            data = await execute(start_date="20220324", end_date="20220324")
            print(data)
        except Exception as e:
            print(f"Error: {str(e)}")
    
    asyncio.run(main())