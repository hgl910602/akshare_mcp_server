import asyncio
from typing import List, Dict, Any
import akshare as ak
import pandas as pd

async def execute(date: str) -> List[Dict[str, Any]]:
    """
    异步获取东方财富网-数据中心-股东分析-股东持股明细-十大流通股东数据
    
    Args:
        date: 财报发布季度最后日, 例如 "20210930"
    
    Returns:
        十大流通股东数据列表, 每个股东信息以字典形式存储
        
    Raises:
        Exception: 当akshare接口调用失败时抛出异常
    """
    try:
        # 调用akshare同步接口获取数据
        df = ak.stock_gdfx_free_holding_detail_em(date=date)
        
        # 将DataFrame转换为List[Dict]格式
        if not df.empty:
            # 处理可能的NaN值
            df = df.fillna(0)
            return df.to_dict("records")
        return []
    except Exception as e:
        raise Exception(f"获取十大流通股东数据失败: {str(e)}")

def test():
    """
    同步测试方法, 用于自动化测试
    
    Returns:
        十大流通股东数据列表
        
    Raises:
        原样抛出execute方法可能产生的异常
    """
    # 使用示例参数调用
    return asyncio.run(execute(date="20210930"))

if __name__ == "__main__":
    # 演示如何调用异步函数
    async def main():
        try:
            data = await execute(date="20210930")
            print(data[:2])  # 打印前两条数据
        except Exception as e:
            print(f"Error: {e}")
    
    asyncio.run(main())