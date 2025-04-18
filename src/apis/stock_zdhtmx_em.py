import asyncio
from typing import List, Dict, Any
import akshare as ak
import pandas as pd

async def execute(start_date: str, end_date: str) -> List[Dict[str, Any]]:
    """
    异步获取东方财富网-数据中心-重大合同-重大合同明细数据
    
    Args:
        start_date: 开始日期，格式为"YYYYMMDD"
        end_date: 结束日期，格式为"YYYYMMDD"
    
    Returns:
        重大合同明细数据列表，每个元素为一个字典
    
    Raises:
        Exception: 当获取数据失败时抛出异常
    """
    try:
        # 调用akshare的同步接口，使用await包装
        df = await asyncio.get_event_loop().run_in_executor(
            None, 
            lambda: ak.stock_zdhtmx_em(start_date=start_date, end_date=end_date)
        )
        
        # 将DataFrame转换为List[Dict]格式
        if not df.empty:
            # 处理可能的NaN值
            df = df.fillna('')
            return df.to_dict('records')
        return []
    except Exception as e:
        raise Exception(f"获取重大合同明细数据失败: {str(e)}")

def test():
    """
    同步测试方法，用于自动化测试
    
    Returns:
        重大合同明细数据列表
        
    Raises:
        原样抛出execute方法中的异常
    """
    # 使用示例中的参数
    start_date = "20220819"
    end_date = "20230819"
    return asyncio.run(execute(start_date=start_date, end_date=end_date))

if __name__ == '__main__':
    # 演示如何调用异步函数
    async def main():
        try:
            data = await execute(start_date="20220819", end_date="20230819")
            print(f"获取到{len(data)}条数据")
            if data:
                print("第一条数据示例:")
                print(data[0])
        except Exception as e:
            print(f"发生错误: {e}")
    
    asyncio.run(main())