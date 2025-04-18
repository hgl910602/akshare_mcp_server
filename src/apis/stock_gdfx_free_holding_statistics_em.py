import asyncio
from typing import List, Dict, Any
import akshare as ak
import pandas as pd

async def execute(date: str) -> List[Dict[str, Any]]:
    """
    异步获取东方财富网-数据中心-股东分析-股东持股统计-十大股东数据
    
    Args:
        date: 财报发布季度最后日，格式如"20210930"
        
    Returns:
        十大股东数据列表，每个股东信息以字典形式存储
        
    Raises:
        Exception: 当接口调用失败时抛出异常
    """
    try:
        # 调用akshare接口获取数据
        df = ak.stock_gdfx_free_holding_statistics_em(date=date)
        
        # 将DataFrame转换为List[Dict]格式
        if not df.empty:
            # 处理可能的NaN值
            df = df.where(pd.notnull(df), None)
            return df.to_dict("records")
        return []
    except Exception as e:
        raise Exception(f"获取股东持股统计数据失败: {str(e)}")

def test():
    """
    同步测试方法，用于自动化测试
    
    Returns:
        十大股东数据列表
        
    Raises:
        原样抛出execute方法中的异常
    """
    # 使用示例中的参数进行测试
    test_date = "20210930"
    return asyncio.run(execute(date=test_date))

if __name__ == "__main__":
    # 演示如何调用异步函数
    async def main():
        try:
            data = await execute(date="20210930")
            print(data)
        except Exception as e:
            print(f"Error: {e}")
    
    asyncio.run(main())