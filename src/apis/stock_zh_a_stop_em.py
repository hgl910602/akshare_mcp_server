import asyncio
from typing import List, Dict, Any
import akshare as ak
import pandas as pd

async def execute() -> List[Dict[str, Any]]:
    """
    异步获取东方财富网-行情中心-沪深个股-两网及退市数据
    
    Returns:
        List[Dict[str, Any]]: 返回处理后的数据列表，每个元素为包含字段的字典
        
    Raises:
        Exception: 当数据获取或处理失败时抛出异常
    """
    try:
        # 调用akshare同步接口获取数据
        df = ak.stock_zh_a_stop_em()
        
        # 将DataFrame转换为List[Dict]格式
        result = df.to_dict(orient='records')
        
        # 处理可能的NaN值，替换为None
        for item in result:
            for key, value in item.items():
                if pd.isna(value):
                    item[key] = None
                    
        return result
    except Exception as e:
        raise Exception(f"获取两网及退市数据失败: {str(e)}")

def test() -> List[Dict[str, Any]]:
    """
    同步测试方法，用于自动化测试
    
    Returns:
        List[Dict[str, Any]]: 返回处理后的数据列表
        
    Raises:
        Exception: 当execute方法执行失败时抛出异常
    """
    return asyncio.run(execute())

if __name__ == '__main__':
    # 演示如何调用异步函数并打印结果
    async def main():
        try:
            data = await execute()
            print(f"获取到{len(data)}条数据")
            if len(data) > 0:
                print("第一条数据示例:")
                print(data[0])
        except Exception as e:
            print(f"执行出错: {e}")
    
    asyncio.run(main())