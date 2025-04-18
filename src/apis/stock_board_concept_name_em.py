import asyncio
from typing import List, Dict, Any
import akshare as ak
import pandas as pd

async def execute() -> List[Dict[str, Any]]:
    """
    获取东方财富网-行情中心-沪深京板块-概念板块数据
    
    Returns:
        List[Dict[str, Any]]: 返回概念板块数据列表，每个板块信息以字典形式存储
        
    Raises:
        Exception: 当获取数据失败时抛出异常
    """
    try:
        # 调用akshare接口获取数据
        df = ak.stock_board_concept_name_em()
        
        # 将DataFrame转换为List[Dict]格式
        result = df.to_dict(orient='records')
        return result
    except Exception as e:
        raise Exception(f"获取概念板块数据失败: {e}")

def test() -> List[Dict[str, Any]]:
    """
    同步测试方法，用于自动化测试
    
    Returns:
        List[Dict[str, Any]]: 返回概念板块数据列表
        
    Raises:
        Exception: 当execute方法执行失败时抛出异常
    """
    try:
        return asyncio.run(execute())
    except Exception as e:
        raise e

if __name__ == '__main__':
    # 异步调用示例
    async def main():
        try:
            data = await execute()
            print(f"获取到{len(data)}条概念板块数据")
            for i, item in enumerate(data[:3], 1):  # 打印前3条数据
                print(f"\n第{i}条数据:")
                for k, v in item.items():
                    print(f"{k}: {v}")
        except Exception as e:
            print(f"执行出错: {e}")
    
    asyncio.run(main())