import asyncio
from typing import List, Dict, Any
import akshare as ak
import pandas as pd

async def execute(symbol: str, date: str) -> List[Dict[str, Any]]:
    """
    异步获取东方财富网个股限售解禁-解禁股东数据
    
    Args:
        symbol: 股票代码，如 "600000"
        date: 解禁日期，如 "20200904"
        
    Returns:
        返回解禁股东数据的字典列表
        
    Raises:
        Exception: 当获取数据失败时抛出异常
    """
    try:
        # 调用akshare接口获取数据
        df = ak.stock_restricted_release_stockholder_em(symbol=symbol, date=date)
        
        # 将DataFrame转换为字典列表
        if not df.empty:
            # 处理可能的NaN值
            df = df.fillna(0)
            # 转换数据类型
            df = df.astype({
                '序号': 'int64',
                '解禁数量': 'int64',
                '实际解禁数量': 'int64',
                '解禁市值': 'float64',
                '锁定期': 'int64',
                '剩余未解禁数量': 'int64'
            })
            return df.to_dict('records')
        return []
    except Exception as e:
        raise Exception(f"获取限售解禁股东数据失败: {e}")

def test():
    """
    同步测试方法，用于自动化测试
    
    Returns:
        返回解禁股东数据的字典列表
        
    Raises:
        异常上抛不捕获
    """
    # 使用示例参数调用
    symbol = "600000"
    date = "20200904"
    return asyncio.run(execute(symbol=symbol, date=date))

if __name__ == '__main__':
    # 演示如何调用异步函数
    async def main():
        try:
            data = await execute(symbol="600000", date="20200904")
            print(data)
        except Exception as e:
            print(f"Error: {e}")
    
    asyncio.run(main())