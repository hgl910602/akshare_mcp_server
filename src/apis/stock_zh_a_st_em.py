import asyncio
from typing import List, Dict, Any
import akshare as ak
import pandas as pd

async def execute() -> List[Dict[str, Any]]:
    """
    获取东方财富网-行情中心-沪深个股-风险警示板数据
    
    Returns:
        List[Dict[str, Any]]: 返回风险警示板股票数据列表，每个股票为一个字典
    """
    try:
        # 调用akshare接口获取数据
        df = ak.stock_zh_a_st_em()
        
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
                '涨跌幅': 'float64',
                '涨跌额': 'float64',
                '成交量': 'float64',
                '成交额': 'float64',
                '振幅': 'float64',
                '最高': 'float64',
                '最低': 'float64',
                '今开': 'float64',
                '昨收': 'float64',
                '量比': 'float64',
                '换手率': 'float64',
                '市盈率-动态': 'float64',
                '市净率': 'float64'
            })
            return df.to_dict('records')
        return []
    except Exception as e:
        raise Exception(f"获取风险警示板数据失败: {e}")

def test() -> List[Dict[str, Any]]:
    """
    同步测试方法，用于自动化测试
    
    Returns:
        List[Dict[str, Any]]: 返回风险警示板股票数据列表
        
    Raises:
        Exception: 当execute方法执行失败时抛出异常
    """
    try:
        return asyncio.run(execute())
    except Exception as e:
        raise Exception(f"测试执行失败: {e}")

if __name__ == '__main__':
    # 演示如何调用异步函数并打印结果
    async def main():
        try:
            data = await execute()
            print(f"获取到{len(data)}条风险警示板数据:")
            for item in data[:5]:  # 打印前5条数据
                print(item)
        except Exception as e:
            print(f"执行出错: {e}")
    
    asyncio.run(main())