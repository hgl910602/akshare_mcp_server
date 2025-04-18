import asyncio
from typing import List, Dict, Any
import akshare as ak

async def execute(
    symbol: str,
    start_date: str = "19000101",
    end_date: str = "20500101",
    adjust: str = "",
    timeout: float = None,
) -> List[Dict[str, Any]]:
    """
    异步获取腾讯证券A股历史行情数据
    
    Args:
        symbol: 带市场标识的股票代码，如'sz000001'
        start_date: 开始日期，格式'YYYYMMDD'
        end_date: 结束日期，格式'YYYYMMDD'
        adjust: 复权类型，''(不复权), 'qfq'(前复权), 'hfq'(后复权)
        timeout: 超时时间(秒)
        
    Returns:
        List[Dict[str, Any]]: 历史行情数据列表
        
    Raises:
        Exception: 当akshare接口调用失败时抛出
    """
    try:
        # 调用akshare同步接口，使用await在异步环境中执行
        df = await asyncio.get_event_loop().run_in_executor(
            None,
            lambda: ak.stock_zh_a_hist_tx(
                symbol=symbol,
                start_date=start_date,
                end_date=end_date,
                adjust=adjust,
                timeout=timeout,
            ),
        )
        # 将DataFrame转换为List[Dict]格式
        return df.to_dict("records")
    except Exception as e:
        raise Exception(f"Failed to fetch stock history data: {str(e)}")

def test():
    """
    同步测试方法，用于自动化测试
    
    Returns:
        List[Dict[str, Any]]: 历史行情数据列表
        
    Raises:
        Exception: 当execute方法调用失败时抛出
    """
    try:
        # 使用asyncio.run调用异步方法
        return asyncio.run(
            execute(
                symbol="sz000001",
                start_date="20200101",
                end_date="20231027",
                adjust="hfq",
            )
        )
    except Exception as e:
        raise Exception(f"Test failed: {str(e)}")

if __name__ == "__main__":
    # 演示如何调用异步函数
    async def main():
        try:
            data = await execute(
                symbol="sz000001",
                start_date="20200101",
                end_date="20231027",
                adjust="hfq",
            )
            print(data[:5])  # 打印前5条数据
        except Exception as e:
            print(f"Error: {str(e)}")
    
    asyncio.run(main())