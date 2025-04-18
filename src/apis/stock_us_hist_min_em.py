import asyncio
from typing import List, Dict, Any
import akshare as ak

async def execute(symbol: str, start_date: str = "1979-09-01 09:32:00", end_date: str = "2222-01-01 09:32:00") -> List[Dict[str, Any]]:
    """
    获取东方财富网美股分时行情数据
    
    Args:
        symbol: 美股代码，例如 "105.ATER"
        start_date: 开始日期时间，格式 "YYYY-MM-DD HH:MM:SS"
        end_date: 结束日期时间，格式 "YYYY-MM-DD HH:MM:SS"
    
    Returns:
        包含分时行情数据的字典列表
    
    Raises:
        Exception: 当获取数据失败时抛出异常
    """
    try:
        # 调用akshare同步接口获取数据
        df = ak.stock_us_hist_min_em(symbol=symbol, start_date=start_date, end_date=end_date)
        
        # 将DataFrame转换为List[Dict]格式
        result = df.to_dict(orient='records')
        return result
    except Exception as e:
        raise Exception(f"Failed to fetch US stock minute data: {str(e)}")

def test():
    """
    同步测试方法，用于自动化测试
    
    Raises:
        Exception: 当execute方法执行失败时抛出异常
    """
    try:
        # 使用示例参数调用execute方法
        result = asyncio.run(execute(symbol="105.ATER"))
        print("Test executed successfully")
        return result
    except Exception as e:
        print(f"Test failed: {str(e)}")
        raise

if __name__ == '__main__':
    # 演示如何调用异步execute方法
    async def main():
        try:
            data = await execute(symbol="105.ATER")
            print("Data fetched successfully:")
            for item in data[:5]:  # 打印前5条数据
                print(item)
        except Exception as e:
            print(f"Error occurred: {str(e)}")
    
    asyncio.run(main())