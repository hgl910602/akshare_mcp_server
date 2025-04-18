import asyncio
from typing import List, Dict, Any
import akshare as ak
import pandas as pd

async def execute(
    symbol: str,
    market: str = "沪深京",
    keyword: str = "",
    category: str = "",
    start_date: str = "",
    end_date: str = "",
) -> List[Dict[str, Any]]:
    """
    异步获取巨潮资讯-沪深京股票信息披露公告
    
    Args:
        symbol: 股票代码
        market: 市场类型，默认为"沪深京"
        keyword: 关键词，默认为空
        category: 公告类别，默认为空
        start_date: 开始日期，格式为YYYYMMDD
        end_date: 结束日期，格式为YYYYMMDD
    
    Returns:
        公告信息列表，每个公告为字典形式
    
    Raises:
        Exception: 当akshare接口调用失败时抛出异常
    """
    try:
        # 调用akshare接口获取数据
        df = ak.stock_zh_a_disclosure_report_cninfo(
            symbol=symbol,
            market=market,
            keyword=keyword,
            category=category,
            start_date=start_date,
            end_date=end_date,
        )
        
        # 将DataFrame转换为List[Dict]格式
        if not df.empty:
            return df.to_dict(orient="records")
        return []
    except Exception as e:
        raise Exception(f"Failed to fetch disclosure report: {str(e)}")

def test() -> List[Dict[str, Any]]:
    """
    同步测试方法，用于自动化测试
    
    Returns:
        公告信息列表
    
    Raises:
        Exception: 当execute方法调用失败时抛出异常
    """
    try:
        return asyncio.run(
            execute(
                symbol="000001",
                market="沪深京",
                category="公司治理",
                start_date="20230619",
                end_date="20231220",
            )
        )
    except Exception as e:
        raise Exception(f"Test failed: {str(e)}")

if __name__ == "__main__":
    # 演示如何调用异步函数
    async def main():
        try:
            result = await execute(
                symbol="000001",
                market="沪深京",
                category="公司治理",
                start_date="20230619",
                end_date="20231220",
            )
            print(result)
        except Exception as e:
            print(f"Error: {str(e)}")
    
    asyncio.run(main())