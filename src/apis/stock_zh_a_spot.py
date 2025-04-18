import asyncio
from typing import List, Dict, Any
import akshare as ak
import pandas as pd

async def execute() -> List[Dict[str, Any]]:
    """
    获取新浪财经-沪深京 A 股实时行情数据(异步版本)
    
    返回:
        List[Dict[str, Any]]: 包含所有股票实时数据的字典列表
        
    异常:
        Exception: 获取数据时可能出现的各种异常
    """
    try:
        # 调用akshare同步接口获取数据
        df = ak.stock_zh_a_spot()
        
        # 将DataFrame转换为字典列表并返回
        return df.to_dict('records')
    except Exception as e:
        raise Exception(f"获取A股实时行情数据失败: {str(e)}")

def test() -> List[Dict[str, Any]]:
    """
    同步测试方法，用于自动化测试
    
    返回:
        List[Dict[str, Any]]: 包含所有股票实时数据的字典列表
        
    异常:
        会原样抛出execute方法中的异常
    """
    return asyncio.run(execute())

if __name__ == '__main__':
    # 演示如何调用异步函数
    async def main():
        try:
            data = await execute()
            print(f"获取到{len(data)}条A股实时数据")
            if len(data) > 0:
                print("第一条数据示例:")
                print(data[0])
        except Exception as e:
            print(f"发生错误: {e}")
    
    asyncio.run(main())