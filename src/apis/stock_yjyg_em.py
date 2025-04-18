import asyncio
from typing import List, Dict, Any
import akshare as ak
import pandas as pd

async def execute(date: str) -> List[Dict[str, Any]]:
    """
    异步获取东方财富-数据中心-年报季报-业绩预告数据
    
    Args:
        date: 报告日期，格式为"YYYY0331", "YYYY0630", "YYYY0930", "YYYY1231"
        
    Returns:
        业绩预告数据列表，每个元素为一个字典
        
    Raises:
        ValueError: 当输入参数格式不正确时
        Exception: 当获取数据失败时
    """
    if not isinstance(date, str) or len(date) != 8 or not date.isdigit():
        raise ValueError("date参数格式不正确，应为8位数字字符串，如'20200331'")
    
    try:
        # 调用akshare同步接口，使用await在异步环境中运行
        loop = asyncio.get_running_loop()
        df = await loop.run_in_executor(None, ak.stock_yjyg_em, date)
        
        # 将DataFrame转换为List[Dict]格式
        if not df.empty:
            # 处理可能的NaN值
            df = df.where(pd.notnull(df), None)
            return df.to_dict("records")
        return []
    except Exception as e:
        raise Exception(f"获取业绩预告数据失败: {str(e)}")

def test() -> List[Dict[str, Any]]:
    """
    同步测试方法，用于自动化测试
    
    Returns:
        业绩预告数据列表
        
    Raises:
        原样抛出execute方法中的异常
    """
    # 使用示例中的参数
    date = "20190331"
    return asyncio.run(execute(date))

if __name__ == "__main__":
    # 演示如何调用异步函数
    async def main():
        try:
            data = await execute(date="20200331")
            print(f"获取到{len(data)}条业绩预告数据")
            if data:
                print("第一条数据示例:")
                print(data[0])
        except Exception as e:
            print(f"发生错误: {e}")
    
    asyncio.run(main())