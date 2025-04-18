import asyncio
from typing import List, Dict, Any
import akshare as ak

async def execute(symbol: str = "A股", date: str = "20230421", time: str = "今日") -> List[Dict[str, Any]]:
    """
    异步获取百度股市通热搜股票数据
    
    Args:
        symbol: 股票市场类型，可选值为 "全部", "A股", "港股", "美股"
        date: 查询日期，格式为YYYYMMDD
        time: 查询时间范围，可选值为 "今日" 或 "1小时"
        
    Returns:
        热搜股票数据列表，每个元素为包含股票信息的字典
        
    Raises:
        Exception: 当akshare接口调用失败时抛出异常
    """
    try:
        # 调用akshare接口获取数据
        df = ak.stock_hot_search_baidu(symbol=symbol, date=date, time=time)
        # 将DataFrame转换为List[Dict]格式
        return df.to_dict("records")
    except Exception as e:
        raise Exception(f"获取百度热搜股票数据失败: {str(e)}")

def test():
    """
    同步测试方法，用于自动化测试
    
    Raises:
        直接抛出execute方法中产生的任何异常
    """
    try:
        result = asyncio.run(execute(symbol="A股", date="20230421", time="今日"))
        print("测试成功，返回数据条数:", len(result))
        return result
    except Exception as e:
        print("测试失败:", str(e))
        raise

if __name__ == "__main__":
    # 演示如何调用异步函数
    async def main():
        try:
            data = await execute(symbol="A股", date="20230421", time="今日")
            print("获取到的热搜股票数据:")
            for item in data:
                print(item)
        except Exception as e:
            print(f"发生错误: {str(e)}")
    
    asyncio.run(main())