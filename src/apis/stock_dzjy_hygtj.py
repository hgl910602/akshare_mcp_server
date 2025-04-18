import asyncio
from typing import List, Dict, Any
import akshare as ak
import pandas as pd

async def execute(symbol: str = '近三月') -> List[Dict[str, Any]]:
    """
    异步获取东方财富网-数据中心-大宗交易-活跃 A 股统计数据
    
    Args:
        symbol: 统计周期, 可选: '近一月', '近三月', '近六月', '近一年'
        
    Returns:
        返回处理后的字典列表
        
    Raises:
        Exception: 当akshare接口调用失败时抛出异常
    """
    try:
        # 调用akshare接口获取数据
        df = ak.stock_dzjy_hygtj(symbol=symbol)
        
        # 处理数据为字典列表
        if not df.empty:
            # 处理可能的NaN值
            df = df.fillna(0)
            # 转换数据类型
            df = df.astype({
                '序号': 'int64',
                '证券代码': 'str',
                '证券简称': 'str',
                '最新价': 'float64',
                '涨跌幅': 'float64',
                '最近上榜日': 'str',
                '上榜次数-总计': 'int64',
                '上榜次数-溢价': 'int64',
                '上榜次数-折价': 'int64',
                '总成交额': 'float64',
                '折溢率': 'float64',
                '成交总额/流通市值': 'float64',
                '上榜日后平均涨跌幅-1日': 'float64',
                '上榜日后平均涨跌幅-5日': 'float64',
                '上榜日后平均涨跌幅-10日': 'float64',
                '上榜日后平均涨跌幅-20日': 'float64'
            })
            return df.to_dict('records')
        return []
    except Exception as e:
        raise Exception(f"获取大宗交易活跃A股统计数据失败: {e}")

def test():
    """
    同步测试方法，用于自动化测试
    
    Raises:
        直接抛出execute方法中的异常
    """
    try:
        result = asyncio.run(execute(symbol='近三月'))
        print(result)
        return result
    except Exception as e:
        print(f"测试失败: {e}")
        raise

if __name__ == '__main__':
    # 演示如何调用异步函数
    async def main():
        try:
            data = await execute(symbol='近三月')
            print(data)
        except Exception as e:
            print(f"调用失败: {e}")
    
    asyncio.run(main())