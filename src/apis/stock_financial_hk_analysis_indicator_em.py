import asyncio
from typing import List, Dict, Any
import akshare as ak

async def execute(symbol: str, indicator: str) -> List[Dict[str, Any]]:
    """
    获取东方财富-港股-财务分析-主要指标数据(异步版本)
    
    Args:
        symbol: 股票代码, 如 "00700"
        indicator: 报告类型, "年度" 或 "报告期"
    
    Returns:
        List[Dict[str, Any]]: 财务指标数据列表
    
    Raises:
        Exception: 当获取数据失败时抛出异常
    """
    try:
        # 调用akshare同步接口获取数据
        df = ak.stock_financial_hk_analysis_indicator_em(symbol=symbol, indicator=indicator)
        # 将DataFrame转换为List[Dict]格式
        return df.to_dict(orient="records")
    except Exception as e:
        raise Exception(f"获取港股财务指标数据失败: {str(e)}")

def test():
    """
    同步测试方法, 用于自动化测试
    
    Returns:
        List[Dict[str, Any]]: 财务指标数据列表
    
    Raises:
        Exception: 当execute方法执行失败时抛出异常
    """
    try:
        # 使用asyncio.run调用异步方法
        return asyncio.run(execute(symbol="00700", indicator="年度"))
    except Exception as e:
        raise Exception(f"测试执行失败: {str(e)}")

if __name__ == "__main__":
    # 演示如何调用异步函数
    async def main():
        try:
            data = await execute(symbol="00700", indicator="年度")
            print(data)
        except Exception as e:
            print(f"Error: {e}")
    
    asyncio.run(main())