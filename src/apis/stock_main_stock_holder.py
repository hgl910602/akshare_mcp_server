import asyncio
from typing import List, Dict, Any
import akshare as ak
import pandas as pd

async def execute(stock: str) -> List[Dict[str, Any]]:
    """
    异步获取股票主要股东信息
    
    Args:
        stock: 股票代码, 如 "600004"
        
    Returns:
        主要股东信息列表, 每个股东信息为字典格式
        
    Raises:
        Exception: 当akshare接口调用失败时抛出异常
    """
    try:
        # 调用akshare同步接口
        df = ak.stock_main_stock_holder(stock=stock)
        
        # 将DataFrame转换为List[Dict]格式
        if not df.empty:
            # 处理可能的NaN值
            df = df.fillna('')
            # 转换数据类型
            df['持股数量'] = df['持股数量'].astype(float)
            df['持股比例'] = df['持股比例'].astype(float)
            df['股东总数'] = df['股东总数'].astype(float)
            df['平均持股数'] = df['平均持股数'].astype(float)
            
            return df.to_dict('records')
        return []
    except Exception as e:
        raise Exception(f"获取股票{stock}主要股东信息失败: {str(e)}")

def test():
    """
    同步测试方法, 用于自动化测试
    
    Raises:
        Exception: 当execute方法调用失败时抛出异常
    """
    try:
        # 使用示例参数调用
        result = asyncio.run(execute(stock="600004"))
        print(result)
    except Exception as e:
        raise Exception(f"测试失败: {str(e)}")

if __name__ == '__main__':
    # 演示如何调用异步函数
    async def main():
        try:
            result = await execute(stock="600004")
            print(result)
        except Exception as e:
            print(f"Error: {str(e)}")
    
    asyncio.run(main())