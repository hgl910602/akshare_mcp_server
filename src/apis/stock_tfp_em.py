import asyncio
from typing import List, Dict, Any
import akshare as ak
import pandas as pd

async def execute(date: str) -> List[Dict[str, Any]]:
    """
    异步获取东方财富网-数据中心-特色数据-停复牌信息
    
    Args:
        date: 日期, 格式为"YYYYMMDD"
        
    Returns:
        停复牌信息列表, 每个元素为包含详细信息的字典
        
    Raises:
        Exception: 当获取数据失败时抛出异常
    """
    try:
        # 调用akshare同步接口获取数据
        df = ak.stock_tfp_em(date=date)
        
        # 将DataFrame转换为List[Dict]格式
        if not df.empty:
            # 处理可能的NaN值
            df = df.where(pd.notna(df), None)
            return df.to_dict(orient="records")
        return []
    except Exception as e:
        raise Exception(f"获取停复牌信息失败: {e}")

def test():
    """
    同步测试方法, 用于自动化测试
    
    Returns:
        停复牌信息列表
        
    Raises:
        原样抛出execute方法中的异常
    """
    # 使用示例中的参数
    date = "20240426"
    return asyncio.run(execute(date))

if __name__ == "__main__":
    # 演示如何调用异步函数
    async def main():
        try:
            date = "20240426"
            result = await execute(date)
            print(f"获取到{len(result)}条停复牌信息:")
            for item in result:
                print(item)
        except Exception as e:
            print(f"发生错误: {e}")
    
    asyncio.run(main())