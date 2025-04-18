import asyncio
from typing import List, Dict, Any
import akshare as ak

async def execute(
    symbol: str,
    start_date: str = "",
    end_date: str = "",
    adjust: str = "",
) -> List[Dict[str, Any]]:
    """
    异步获取B股历史行情数据
    
    Args:
        symbol: 股票代码，例如'sh900901'
        start_date: 开始日期，格式'YYYYMMDD'
        end_date: 结束日期，格式'YYYYMMDD'
        adjust: 复权类型，可选'qfq'/'hfq'/'hfq-factor'/'qfq-factor'
    
    Returns:
        历史行情数据列表，每个元素为包含当日数据的字典
    
    Raises:
        Exception: 当akshare接口调用失败时抛出
    """
    try:
        # 调用akshare同步接口，使用await在异步环境中执行
        df = await asyncio.get_event_loop().run_in_executor(
            None,
            ak.stock_zh_b_daily,
            symbol,
            start_date,
            end_date,
            adjust
        )
        # 将DataFrame转换为List[Dict]格式
        return df.reset_index().to_dict("records")
    except Exception as e:
        raise Exception(f"Failed to fetch B stock data: {str(e)}")

def test():
    """
    同步测试方法，用于自动化测试
    
    Raises:
        Exception: 当execute方法调用失败时抛出
    """
    try:
        # 使用示例参数调用execute方法
        result = asyncio.run(execute(
            symbol="sh900901",
            adjust="hfq-factor"
        ))
        print("Test executed successfully")
        return result
    except Exception as e:
        print(f"Test failed: {str(e)}")
        raise

if __name__ == "__main__":
    # 演示如何调用异步函数
    async def main():
        try:
            data = await execute(
                symbol="sh900901",
                start_date="20201103",
                end_date="20201116",
                adjust="hfq"
            )
            print(data[:5])  # 打印前5条数据
        except Exception as e:
            print(f"Error: {str(e)}")
    
    asyncio.run(main())