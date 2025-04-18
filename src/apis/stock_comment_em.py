import asyncio
from typing import List, Dict, Any
import akshare as ak
import pandas as pd

async def execute() -> List[Dict[str, Any]]:
    """
    异步获取东方财富网千股千评数据
    
    Returns:
        List[Dict[str, Any]]: 转换后的股票评论数据列表
    """
    try:
        # 调用akshare接口获取数据
        df = ak.stock_comment_em()
        
        # 将DataFrame转换为List[Dict]格式
        if not df.empty:
            # 处理可能的NaN值
            df = df.fillna(0)
            # 转换数据类型
            df = df.astype({
                '序号': int,
                '代码': str,
                '名称': str,
                '最新价': float,
                '涨跌幅': float,
                '换手率': float,
                '市盈率': float,
                '主力成本': float,
                '机构参与度': float,
                '综合得分': float,
                '上升': int,
                '目前排名': int,
                '关注指数': float,
                '交易日': float
            })
            return df.to_dict('records')
        return []
    except Exception as e:
        raise Exception(f"获取千股千评数据失败: {str(e)}")

def test() -> List[Dict[str, Any]]:
    """
    同步测试方法，用于自动化测试
    
    Returns:
        List[Dict[str, Any]]: 股票评论数据
        
    Raises:
        Exception: 当execute方法执行出错时抛出
    """
    try:
        return asyncio.run(execute())
    except Exception as e:
        raise Exception(f"测试执行失败: {str(e)}")

if __name__ == '__main__':
    # 演示异步调用
    async def main():
        try:
            data = await execute()
            print(f"获取到{len(data)}条股票评论数据")
            if data:
                print("第一条数据示例:")
                print(data[0])
        except Exception as e:
            print(f"执行出错: {e}")
    
    asyncio.run(main())