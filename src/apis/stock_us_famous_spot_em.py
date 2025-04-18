import asyncio
from typing import List, Dict, Any
import akshare as ak
import pandas as pd

async def execute(symbol: str = '科技类') -> List[Dict[str, Any]]:
    """
    获取美股-知名美股的实时行情数据
    
    Args:
        symbol: 股票类别, 可选: {'科技类', '金融类', '医药食品类', '媒体类', '汽车能源类', '制造零售类'}
    
    Returns:
        List[Dict[str, Any]]: 返回转换后的字典列表
    
    Raises:
        Exception: 当获取数据失败时抛出异常
    """
    try:
        # 调用akshare接口获取数据
        df = ak.stock_us_famous_spot_em(symbol=symbol)
        
        # 将DataFrame转换为字典列表
        if not df.empty:
            # 处理可能的NaN值
            df = df.fillna(0)
            # 转换数据类型
            df = df.astype({
                '序号': 'int64',
                '名称': 'str',
                '最新价': 'float64',
                '涨跌额': 'float64',
                '涨跌幅': 'float64',
                '开盘价': 'float64',
                '最高价': 'float64',
                '最低价': 'float64',
                '昨收价': 'float64',
                '总市值': 'float64',
                '市盈率': 'float64',
                '代码': 'str'
            })
            return df.to_dict('records')
        return []
    except Exception as e:
        raise Exception(f"获取美股知名股票数据失败: {str(e)}")

def test():
    """
    同步测试方法，用于自动化测试
    
    Raises:
        Exception: 当execute方法执行失败时抛出异常
    """
    try:
        result = asyncio.run(execute(symbol='科技类'))
        print(f"测试成功，获取到{len(result)}条数据")
        return result
    except Exception as e:
        print(f"测试失败: {str(e)}")
        raise

if __name__ == '__main__':
    # 演示如何调用异步函数
    async def main():
        try:
            data = await execute(symbol='科技类')
            print(f"获取到{len(data)}条数据:")
            for item in data[:3]:  # 打印前3条数据
                print(item)
        except Exception as e:
            print(f"执行出错: {str(e)}")
    
    asyncio.run(main())