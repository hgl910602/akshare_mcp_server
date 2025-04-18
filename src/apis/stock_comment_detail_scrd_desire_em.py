import asyncio
from typing import List, Dict, Any
import akshare as ak
import pandas as pd

async def execute(symbol: str) -> List[Dict[str, Any]]:
    """
    异步获取东方财富网-数据中心-特色数据-千股千评-市场热度-市场参与意愿数据
    
    Args:
        symbol: 股票代码, 如 "600000"
        
    Returns:
        返回处理后的字典列表数据
        
    Raises:
        Exception: 当接口调用或数据处理出错时抛出
    """
    try:
        # 调用akshare接口获取数据
        df = ak.stock_comment_detail_scrd_desire_em(symbol=symbol)
        
        # 处理数据为字典列表
        if not df.empty:
            # 转换日期时间为字符串格式
            df['日期时间'] = df['日期时间'].astype(str)
            return df.to_dict('records')
        return []
    except Exception as e:
        raise Exception(f"获取股票市场热度数据失败: {e}")

def test():
    """
    同步测试方法，用于自动化测试
    
    Returns:
        返回execute方法的执行结果
        
    Raises:
        直接抛出execute方法中的异常
    """
    return asyncio.run(execute(symbol="600000"))

if __name__ == '__main__':
    # 演示如何调用异步函数
    async def main():
        try:
            data = await execute(symbol="600000")
            print(data)
        except Exception as e:
            print(f"Error: {e}")
    
    asyncio.run(main())