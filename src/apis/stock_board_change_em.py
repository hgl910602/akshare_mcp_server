import asyncio
from typing import List, Dict, Any
import akshare as ak
import pandas as pd

async def execute() -> List[Dict[str, Any]]:
    """
    东方财富-行情中心-当日板块异动详情
    返回板块异动数据列表
    
    Returns:
        List[Dict[str, Any]]: 板块异动数据列表，每个元素为一个板块的异动信息字典
    """
    try:
        # 调用akshare接口获取数据
        df = ak.stock_board_change_em()
        
        # 将DataFrame转换为字典列表
        result = []
        if not df.empty:
            # 替换NaN为None
            df = df.where(pd.notnull(df), None)
            # 转换每一行为字典
            result = df.to_dict(orient='records')
        return result
    except Exception as e:
        raise Exception(f"获取板块异动数据失败: {e}")

def test() -> List[Dict[str, Any]]:
    """
    同步测试方法，用于自动化测试
    
    Returns:
        List[Dict[str, Any]]: 板块异动数据列表
        
    Raises:
        Exception: 当execute方法执行出错时抛出异常
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
            print("板块异动数据:")
            for item in data:
                print(item)
        except Exception as e:
            print(f"发生错误: {e}")
    
    asyncio.run(main())