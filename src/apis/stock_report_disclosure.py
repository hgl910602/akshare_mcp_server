import asyncio
from typing import Any, Dict, List
import akshare as ak

async def execute(market: str = "沪深京", period: str = "2021年报") -> List[Dict[str, Any]]:
    """
    异步获取巨潮资讯-数据-预约披露的数据
    
    Args:
        market: 市场类型，可选值: {"沪深京", "深市", "深主板", "创业板", "沪市", "沪主板", "科创板", "北交所"}
        period: 报告期，可选值: {"2021一季", "2021半年报", "2021三季", "2021年报"}等近四期的财务报告
    
    Returns:
        返回预约披露数据列表，每个元素为包含字段的字典
    
    Raises:
        Exception: 当akshare接口调用失败时抛出异常
    """
    try:
        # 调用akshare同步接口，使用await在异步环境中执行
        df = await asyncio.get_event_loop().run_in_executor(
            None, 
            lambda: ak.stock_report_disclosure(market=market, period=period)
        )
        # 将DataFrame转换为List[Dict]格式
        return df.to_dict(orient="records")
    except Exception as e:
        raise Exception(f"Failed to fetch stock report disclosure data: {str(e)}")

def test() -> List[Dict[str, Any]]:
    """
    同步测试方法，用于自动化测试
    
    Returns:
        返回预约披露数据列表
    
    Raises:
        异常上抛不捕获
    """
    return asyncio.run(execute(market="沪深京", period="2022年报"))

if __name__ == "__main__":
    # 演示如何调用异步函数
    async def main():
        try:
            data = await execute(market="沪深京", period="2022年报")
            print(data[:2])  # 打印前两条数据示例
        except Exception as e:
            print(f"Error occurred: {e}")
    
    asyncio.run(main())