import asyncio
from typing import List, Dict, Any
import akshare as ak
import pandas as pd

async def execute(
    symbol: str = "000001",
    start_time: str = "09:00:00",
    end_time: str = "15:40:00",
) -> List[Dict[str, Any]]:
    """
    获取东方财富-股票行情-盘前数据 (异步版本)
    
    Args:
        symbol: 股票代码
        start_time: 开始时间
        end_time: 结束时间
    
    Returns:
        返回包含行情数据的字典列表
    
    Raises:
        Exception: 当获取数据失败时抛出异常
    """
    try:
        # 调用akshare同步接口
        df = ak.stock_zh_a_hist_pre_min_em(
            symbol=symbol,
            start_time=start_time,
            end_time=end_time
        )
        
        # 将DataFrame转换为字典列表
        if not df.empty:
            # 处理可能的NaN值
            df = df.fillna(0)
            return df.to_dict("records")
        return []
    except Exception as e:
        raise Exception(f"获取股票盘前数据失败: {e}")

def test():
    """
    同步测试方法，用于自动化测试
    
    Raises:
        原样抛出execute方法中的异常
    """
    try:
        result = asyncio.run(execute(
            symbol="000001",
            start_time="09:00:00",
            end_time="15:40:00"
        ))
        print("测试成功，返回数据条数:", len(result))
        return result
    except Exception as e:
        print("测试失败:", str(e))
        raise

if __name__ == "__main__":
    # 演示如何异步调用该函数
    async def main():
        try:
            data = await execute(
                symbol="000001",
                start_time="09:00:00",
                end_time="15:40:00"
            )
            print("获取到的数据:")
            for item in data[:5]:  # 打印前5条记录
                print(item)
        except Exception as e:
            print(f"发生错误: {e}")
    
    asyncio.run(main())