import asyncio
from typing import List, Dict, Any
import akshare as ak
import pandas as pd

async def execute(symbol: str = '近3日') -> List[Dict[str, Any]]:
    """
    东方财富网-数据中心-大宗交易-活跃营业部统计
    
    Args:
        symbol: choice of {'当前交易日', '近3日', '近5日', '近10日', '近30日'}
    
    Returns:
        List[Dict[str, Any]]: 返回活跃营业部统计数据的字典列表
    
    Raises:
        Exception: 当获取数据失败时抛出异常
    """
    try:
        # 调用akshare接口获取数据
        df = ak.stock_dzjy_hyyybtj(symbol=symbol)
        
        # 将DataFrame转换为字典列表
        result = df.to_dict('records')
        
        # 转换数据类型
        for item in result:
            item['序号'] = int(item['序号'])
            item['次数总计-买入'] = float(item['次数总计-买入'])
            item['次数总计-卖出'] = float(item['次数总计-卖出'])
            item['成交金额统计-买入'] = float(item['成交金额统计-买入'])
            item['成交金额统计-卖出'] = float(item['成交金额统计-卖出'])
            item['成交金额统计-净买入额'] = float(item['成交金额统计-净买入额'])
        
        return result
    except Exception as e:
        raise Exception(f"获取活跃营业部统计数据失败: {str(e)}")

def test():
    """
    同步测试方法，用于自动化测试
    
    Returns:
        List[Dict[str, Any]]: 返回活跃营业部统计数据的字典列表
    
    Raises:
        Exception: 当获取数据失败时抛出异常
    """
    try:
        # 使用asyncio.run调用异步方法
        result = asyncio.run(execute(symbol='近3日'))
        return result
    except Exception as e:
        raise Exception(f"测试失败: {str(e)}")

if __name__ == '__main__':
    # 演示如何调用异步函数
    async def main():
        try:
            data = await execute(symbol='近3日')
            print(data)
        except Exception as e:
            print(f"Error: {e}")
    
    asyncio.run(main())