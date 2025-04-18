import asyncio
from typing import List, Dict, Any
import akshare as ak

async def execute(symbol: str, indicator: str, date: str) -> List[Dict[str, Any]]:
    """
    异步获取股票历史分红配股详情
    
    Args:
        symbol: 股票代码
        indicator: 类型, "分红" 或 "配股"
        date: 分红配股的具体日期
    
    Returns:
        分红配股详情列表
        
    Raises:
        Exception: 当akshare接口调用失败时抛出
    """
    try:
        # 调用akshare同步接口，使用run_in_executor避免阻塞事件循环
        loop = asyncio.get_running_loop()
        df = await loop.run_in_executor(
            None, 
            ak.stock_history_dividend_detail,
            symbol=symbol,
            indicator=indicator,
            date=date
        )
        # 将DataFrame转换为List[Dict]格式
        return df.to_dict(orient='records')
    except Exception as e:
        raise Exception(f"Failed to fetch dividend details: {str(e)}")

def test():
    """
    同步测试方法，用于自动化测试
    
    Raises:
        Exception: 当execute方法调用失败时抛出
    """
    try:
        result = asyncio.run(execute(
            symbol="000002",
            indicator="配股",
            date="1999-12-22"
        ))
        print("Test executed successfully")
        return result
    except Exception as e:
        print(f"Test failed: {str(e)}")
        raise

if __name__ == '__main__':
    # 演示如何调用异步函数
    async def main():
        try:
            result = await execute(
                symbol="600012",
                indicator="配股",
                date="1994-12-24"
            )
            print(result)
        except Exception as e:
            print(f"Error: {str(e)}")
    
    asyncio.run(main())