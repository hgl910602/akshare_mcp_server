import asyncio
from typing import List, Dict, Any
import akshare as ak

async def execute(
    symbol: str = "000001",
    market: str = "沪深京",
    start_date: str = "20230618",
    end_date: str = "20231219",
) -> List[Dict[str, Any]]:
    """
    异步获取巨潮资讯-信息披露调研数据
    
    Args:
        symbol: 股票代码
        market: 市场类型，可选 {"沪深京", "港股", "三板", "基金", "债券", "监管", "预披露"}
        start_date: 开始日期，格式为YYYYMMDD
        end_date: 结束日期，格式为YYYYMMDD
    
    Returns:
        返回信息披露调研数据列表，每个元素为字典形式
    
    Raises:
        Exception: 当akshare接口调用失败时抛出异常
    """
    try:
        # 调用akshare接口获取数据
        df = ak.stock_zh_a_disclosure_relation_cninfo(
            symbol=symbol,
            market=market,
            start_date=start_date,
            end_date=end_date
        )
        # 将DataFrame转换为List[Dict]格式
        return df.to_dict("records")
    except Exception as e:
        raise Exception(f"获取信息披露调研数据失败: {e}")

def test():
    """
    同步测试方法，用于自动化测试
    
    Raises:
        原样抛出execute方法中的异常
    """
    # 使用示例参数调用execute方法
    result = asyncio.run(execute(
        symbol="000001",
        market="沪深京",
        start_date="20230619",
        end_date="20231220"
    ))
    return result

if __name__ == "__main__":
    # 演示如何调用异步函数并打印结果
    async def main():
        try:
            data = await execute(
                symbol="000001",
                market="沪深京",
                start_date="20230619",
                end_date="20231220"
            )
            print(data)
        except Exception as e:
            print(f"Error: {e}")
    
    asyncio.run(main())