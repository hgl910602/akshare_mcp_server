import asyncio
from typing import List, Dict, Any
import akshare as ak
import pandas as pd

async def execute(date: str) -> List[Dict[str, Any]]:
    """
    异步获取深圳证券交易所融资融券交易明细数据
    
    Args:
        date: 日期, 格式为"YYYYMMDD"
        
    Returns:
        返回融资融券交易明细数据列表, 每个元素为一个字典
        
    Raises:
        Exception: 当获取数据失败时抛出异常
    """
    try:
        # 调用akshare接口获取数据
        df = ak.stock_margin_detail_szse(date=date)
        
        # 将DataFrame转换为List[Dict]格式
        if not df.empty:
            # 处理可能的NaN值
            df = df.fillna(0)
            # 转换数据类型
            df = df.astype({
                '融资买入额': 'int64',
                '融资余额': 'int64',
                '融券卖出量': 'int64',
                '融券余量': 'int64',
                '融券余额': 'int64',
                '融资融券余额': 'int64'
            })
            return df.to_dict('records')
        return []
    except Exception as e:
        raise Exception(f"获取深圳证券交易所融资融券交易明细数据失败: {str(e)}")

def test():
    """
    同步测试方法, 用于自动化测试
    
    Raises:
        当execute方法执行失败时抛出异常
    """
    # 使用示例中的日期参数
    test_date = "20230925"
    try:
        result = asyncio.run(execute(date=test_date))
        print(f"测试成功, 获取到{len(result)}条数据")
        return result
    except Exception as e:
        print(f"测试失败: {str(e)}")
        raise

if __name__ == '__main__':
    # 演示如何调用异步函数
    async def main():
        try:
            # 使用示例中的日期参数
            result = await execute(date="20230925")
            print(f"获取到{len(result)}条数据:")
            for item in result[:5]:  # 打印前5条数据
                print(item)
        except Exception as e:
            print(f"执行失败: {str(e)}")
    
    asyncio.run(main())