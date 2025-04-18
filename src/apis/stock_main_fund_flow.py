import asyncio
from typing import List, Dict, Any
import akshare as ak
import pandas as pd

async def execute(symbol: str = "全部股票") -> List[Dict[str, Any]]:
    """
    获取东方财富网-数据中心-资金流向-主力净流入排名数据
    
    Args:
        symbol: 股票类型，可选值: {"全部股票", "沪深A股", "沪市A股", "科创板", "深市A股", "创业板", "沪市B股", "深市B股"}
        
    Returns:
        主力资金流向数据列表，每个元素为一个字典
        
    Raises:
        Exception: 当获取数据失败时抛出异常
    """
    try:
        # 调用akshare同步接口，使用await将同步调用包装为异步
        df = await asyncio.get_event_loop().run_in_executor(
            None, 
            ak.stock_main_fund_flow, 
            symbol
        )
        
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
                '今日排行榜-主力净占比': 'float64',
                '今日排行榜-今日排名': 'float64',
                '今日排行榜-今日涨跌': 'float64',
                '5日排行榜-主力净占比': 'float64',
                '5日排行榜-5日排名': 'int64',
                '5日排行榜-5日涨跌': 'float64',
                '10日排行榜-主力净占比': 'float64',
                '10日排行榜-10日排名': 'int64',
                '10日排行榜-10日涨跌': 'float64',
                '所属板块': 'str'
            })
            return df.to_dict('records')
        return []
    except Exception as e:
        raise Exception(f"获取主力资金流向数据失败: {str(e)}")

def test():
    """
    同步测试方法，用于自动化测试
    
    Raises:
        Exception: 当execute方法执行失败时抛出异常
    """
    try:
        result = asyncio.run(execute(symbol="全部股票"))
        print(f"获取到{len(result)}条主力资金流向数据")
        return result
    except Exception as e:
        raise Exception(f"测试失败: {str(e)}")

if __name__ == '__main__':
    # 演示如何异步调用该函数
    async def main():
        try:
            data = await execute(symbol="全部股票")
            print(f"获取到{len(data)}条数据:")
            for item in data[:3]:  # 打印前3条作为示例
                print(item)
        except Exception as e:
            print(f"发生错误: {str(e)}")
    
    asyncio.run(main())