import asyncio
from typing import List, Dict, Any
import akshare as ak

async def execute(symbol: str, start_date: str, end_date: str) -> List[Dict[str, Any]]:
    """
    异步获取巨潮资讯-公司股本变动数据
    
    Args:
        symbol: 股票代码
        start_date: 开始日期，格式为YYYYMMDD
        end_date: 结束日期，格式为YYYYMMDD
    
    Returns:
        公司股本变动数据列表，每个元素为一个字典
        
    Raises:
        Exception: 当获取数据失败时抛出异常
    """
    try:
        # 调用akshare同步接口，使用run_in_executor避免阻塞事件循环
        loop = asyncio.get_running_loop()
        df = await loop.run_in_executor(
            None, 
            ak.stock_share_change_cninfo, 
            symbol=symbol, 
            start_date=start_date, 
            end_date=end_date
        )
        # 将DataFrame转换为List[Dict]格式
        return df.to_dict(orient='records')
    except Exception as e:
        raise Exception(f"获取公司股本变动数据失败: {e}")

def test():
    """
    同步测试方法，用于自动化测试
    
    Raises:
        当execute方法执行失败时直接抛出异常
    """
    # 使用示例参数进行测试
    result = asyncio.run(execute(symbol="002594", start_date="20091227", end_date="20241021"))
    print(result)

if __name__ == '__main__':
    # 演示如何调用异步函数
    async def main():
        try:
            data = await execute(symbol="002594", start_date="20091227", end_date="20241021")
            print(data[:2])  # 打印前两条数据示例
        except Exception as e:
            print(f"Error: {e}")
    
    asyncio.run(main())