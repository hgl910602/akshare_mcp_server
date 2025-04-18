import asyncio
from typing import List, Dict, Any
import akshare as ak
import pandas as pd

async def execute(
    symbol: str = "全部股票",
    start_date: str = "20221101",
    end_date: str = "20221209",
) -> List[Dict[str, Any]]:
    """
    东方财富网-数据中心-特色数据-限售股解禁
    
    Args:
        symbol: 股票市场类型，可选值: "全部股票", "沪市A股", "科创板", "深市A股", "创业板", "京市A股"
        start_date: 开始日期，格式: "YYYYMMDD"
        end_date: 结束日期，格式: "YYYYMMDD"
    
    Returns:
        限售解禁数据列表，每个元素为一个字典，包含解禁信息
    
    Raises:
        Exception: 当获取数据失败时抛出异常
    """
    try:
        # 调用akshare接口获取数据
        df = ak.stock_restricted_release_summary_em(
            symbol=symbol,
            start_date=start_date,
            end_date=end_date,
        )
        
        # 将DataFrame转换为List[Dict]格式
        if not df.empty:
            # 处理可能的NaN值
            df = df.fillna(0)
            return df.to_dict("records")
        return []
    except Exception as e:
        raise Exception(f"获取限售解禁数据失败: {e}")

def test():
    """
    同步测试方法，用于自动化测试
    
    Raises:
        Exception: 当execute方法执行失败时抛出异常
    """
    try:
        # 使用示例参数调用execute方法
        result = asyncio.run(execute(
            symbol="全部股票",
            start_date="20221108",
            end_date="20221209",
        ))
        print("测试成功，获取数据条数:", len(result))
        return result
    except Exception as e:
        print("测试失败:", str(e))
        raise

if __name__ == "__main__":
    # 演示如何调用异步函数并打印结果
    async def main():
        try:
            data = await execute(
                symbol="全部股票",
                start_date="20221108",
                end_date="20221209",
            )
            print("获取到的限售解禁数据:")
            for item in data[:5]:  # 只打印前5条记录
                print(item)
        except Exception as e:
            print(f"发生错误: {e}")

    asyncio.run(main())