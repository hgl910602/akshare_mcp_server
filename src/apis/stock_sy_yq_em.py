import asyncio
from typing import List, Dict, Any
import akshare as ak
import pandas as pd

async def execute(date: str = "20221231") -> List[Dict[str, Any]]:
    """
    东方财富网-数据中心-特色数据-商誉-商誉减值预期明细
    :param date: 报告期, 如 "20221231"
    :return: 商誉减值预期明细数据
    :raises: Exception 当获取数据失败时抛出异常
    """
    try:
        # 调用akshare接口获取数据
        df = ak.stock_sy_yq_em(date=date)
        
        # 处理可能的空数据情况
        if df.empty:
            return []
            
        # 转换DataFrame为List[Dict]格式
        result = df.replace({pd.NA: None}).to_dict("records")
        return result
    except Exception as e:
        raise Exception(f"获取商誉减值预期明细数据失败: {str(e)}")

def test():
    """
    同步测试方法，用于自动化测试
    :return: 商誉减值预期明细数据
    :raises: Exception 当execute方法执行失败时抛出异常
    """
    try:
        # 使用示例参数调用execute方法
        return asyncio.run(execute(date="20221231"))
    except Exception as e:
        raise Exception(f"测试失败: {str(e)}")

if __name__ == "__main__":
    # 演示如何调用异步函数
    async def main():
        try:
            data = await execute(date="20221231")
            print(f"获取到{len(data)}条数据")
            if data:
                print("第一条数据示例:")
                print(data[0])
        except Exception as e:
            print(f"执行出错: {e}")
    
    asyncio.run(main())