import asyncio
from typing import List, Dict, Any
import akshare as ak
import pandas as pd

async def execute(date: str) -> List[Dict[str, Any]]:
    """
    异步获取巨潮资讯-股东人数及持股集中度数据
    
    Args:
        date: 报告日期，格式为"YYYY0331", "YYYY0630", "YYYY0930"或"YYYY1231"
    
    Returns:
        股东人数及持股集中度数据列表，每个元素为一个字典
    
    Raises:
        Exception: 当akshare接口调用失败时抛出异常
    """
    try:
        # 调用akshare接口获取数据
        df = ak.stock_hold_num_cninfo(date=date)
        
        # 将DataFrame转换为List[Dict]格式
        if not df.empty:
            # 处理可能的NaN值
            df = df.fillna(0)
            # 转换数据类型
            df = df.astype({
                "本期股东人数": int,
                "上期股东人数": float,
                "股东人数增幅": float,
                "本期人均持股数量": int,
                "上期人均持股数量": float,
                "人均持股数量增幅": float
            })
            return df.to_dict("records")
        return []
    except Exception as e:
        raise Exception(f"获取股东人数数据失败: {str(e)}")

def test():
    """
    同步测试方法，用于自动化测试
    
    Returns:
        股东人数及持股集中度数据列表
    
    Raises:
        原样抛出execute方法可能抛出的异常
    """
    # 使用示例中的参数进行测试
    test_date = "20210630"
    return asyncio.run(execute(date=test_date))

if __name__ == "__main__":
    # 演示如何调用异步函数
    async def main():
        try:
            # 使用示例参数调用
            data = await execute(date="20210630")
            # 打印前5条结果
            for item in data[:5]:
                print(item)
        except Exception as e:
            print(f"Error: {e}")
    
    asyncio.run(main())