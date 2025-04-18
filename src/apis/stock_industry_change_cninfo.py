import asyncio
from typing import List, Dict, Any
import akshare as ak

async def execute(symbol: str, start_date: str, end_date: str) -> List[Dict[str, Any]]:
    """
    异步获取上市公司行业归属变动情况
    
    Args:
        symbol: 股票代码
        start_date: 开始日期，格式为YYYYMMDD
        end_date: 结束日期，格式为YYYYMMDD
    
    Returns:
        行业变动信息的字典列表
        
    Raises:
        Exception: 当akshare接口调用失败时抛出
    """
    try:
        # 调用akshare同步接口，使用run_in_executor避免阻塞事件循环
        loop = asyncio.get_running_loop()
        df = await loop.run_in_executor(
            None, 
            ak.stock_industry_change_cninfo, 
            symbol=symbol, 
            start_date=start_date, 
            end_date=end_date
        )
        # 将DataFrame转换为字典列表
        return df.to_dict("records")
    except Exception as e:
        raise Exception(f"Failed to fetch industry change data: {str(e)}")

def test():
    """
    同步测试方法，用于自动化测试
    
    Raises:
        Exception: 当execute方法调用失败时抛出
    """
    try:
        result = asyncio.run(execute(symbol="002594", start_date="20091227", end_date="20220708"))
        print(result)
    except Exception as e:
        raise Exception(f"Test failed: {str(e)}")

if __name__ == "__main__":
    # 演示如何调用异步函数
    async def main():
        try:
            data = await execute(symbol="002594", start_date="20091227", end_date="20220708")
            print(data)
        except Exception as e:
            print(f"Error occurred: {e}")
    
    asyncio.run(main())