import asyncio
from typing import List, Dict, Any
import akshare as ak

async def execute(market: str = "北向", indicator: str = "今日排行") -> List[Dict[str, Any]]:
    """
    获取东方财富网-数据中心-沪深港通持股-个股排行数据
    
    Args:
        market: 市场类型，可选值: "北向", "沪股通", "深股通"
        indicator: 排行类型，可选值: "今日排行", "3日排行", "5日排行", "10日排行", "月排行", "季排行", "年排行"
    
    Returns:
        沪深港通持股个股排行数据列表
    
    Raises:
        Exception: 当获取数据失败时抛出异常
    """
    try:
        # 调用akshare的同步接口，使用asyncio.to_thread在异步环境中运行
        df = await asyncio.to_thread(
            ak.stock_hsgt_hold_stock_em,
            market=market,
            indicator=indicator
        )
        # 将DataFrame转换为List[Dict]格式
        return df.to_dict("records")
    except Exception as e:
        raise Exception(f"获取沪深港通持股个股排行数据失败: {str(e)}")

def test() -> List[Dict[str, Any]]:
    """
    同步测试方法，用于自动化测试
    
    Returns:
        沪深港通持股个股排行数据列表
    
    Raises:
        Exception: 当获取数据失败时抛出异常
    """
    try:
        # 使用asyncio.run运行异步方法
        return asyncio.run(execute(market="北向", indicator="今日排行"))
    except Exception as e:
        raise e

if __name__ == "__main__":
    # 演示如何调用异步函数
    async def main():
        try:
            data = await execute(market="沪股通", indicator="5日排行")
            print(data[:2])  # 打印前两条数据
        except Exception as e:
            print(f"Error: {e}")
    
    asyncio.run(main())