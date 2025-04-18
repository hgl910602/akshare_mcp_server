import asyncio
from typing import List, Dict, Any
import akshare as ak
import pandas as pd

async def execute() -> List[Dict[str, Any]]:
    """
    获取东方财富网-行情中心-港股市场-港股通成份股数据
    
    Returns:
        List[Dict[str, Any]]: 港股通成份股数据列表，每个元素为一个字典表示一条股票数据
        
    Raises:
        Exception: 当获取数据失败时抛出异常
    """
    try:
        # 调用akshare接口获取数据
        df = ak.stock_hk_ggt_components_em()
        
        # 将DataFrame转换为List[Dict]格式
        if not df.empty:
            # 处理可能的NaN值
            df = df.fillna(0)
            # 转换数据类型
            df = df.astype({
                '序号': 'int64',
                '代码': 'str',
                '名称': 'str',
                '最新价': 'float64',
                '涨跌额': 'float64',
                '涨跌幅': 'float64',
                '今开': 'float64',
                '最高': 'float64',
                '最低': 'float64',
                '昨收': 'float64',
                '成交量': 'float64',
                '成交额': 'float64'
            })
            return df.to_dict('records')
        return []
    except Exception as e:
        raise Exception(f"获取港股通成份股数据失败: {str(e)}")

def test() -> List[Dict[str, Any]]:
    """
    同步测试方法，用于自动化测试
    
    Returns:
        List[Dict[str, Any]]: 港股通成份股数据列表
        
    Raises:
        Exception: 当execute方法执行失败时抛出异常
    """
    try:
        return asyncio.run(execute())
    except Exception as e:
        raise Exception(f"测试执行失败: {str(e)}")

if __name__ == '__main__':
    # 演示如何异步调用该函数
    async def main():
        try:
            data = await execute()
            print(f"获取到{len(data)}条港股通成份股数据:")
            for item in data[:3]:  # 打印前3条数据作为示例
                print(item)
        except Exception as e:
            print(f"执行出错: {str(e)}")
    
    asyncio.run(main())