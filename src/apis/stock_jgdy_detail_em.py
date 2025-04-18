import asyncio
from typing import List, Dict, Any
import akshare as ak
import pandas as pd

async def execute(date: str) -> List[Dict[str, Any]]:
    """
    异步获取东方财富网-机构调研详细数据
    
    Args:
        date: 查询日期，格式为"YYYYMMDD"
    
    Returns:
        机构调研详细数据列表，每个元素为一个字典
        
    Raises:
        Exception: 当akshare接口调用失败时抛出异常
    """
    try:
        # 调用akshare同步接口
        df = ak.stock_jgdy_detail_em(date=date)
        
        # 处理可能的空数据
        if df.empty:
            return []
            
        # 转换DataFrame为List[Dict]
        result = df.to_dict(orient='records')
        
        # 处理可能的NaN值
        for item in result:
            for key, value in item.items():
                if pd.isna(value):
                    item[key] = None
        
        return result
    except Exception as e:
        raise Exception(f"获取机构调研详细数据失败: {str(e)}")

def test():
    """
    同步测试方法，用于自动化测试
    
    Raises:
        直接抛出execute方法可能产生的异常
    """
    # 使用示例参数调用
    date = "20241211"
    result = asyncio.run(execute(date=date))
    print(f"获取到{len(result)}条机构调研数据")

if __name__ == "__main__":
    # 演示如何调用异步函数
    async def main():
        try:
            date = "20241211"
            data = await execute(date=date)
            print(f"获取到{len(data)}条数据:")
            for item in data[:3]:  # 打印前3条作为示例
                print(item)
        except Exception as e:
            print(f"发生错误: {e}")
    
    asyncio.run(main())