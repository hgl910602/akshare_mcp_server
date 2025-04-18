import asyncio
from typing import List, Dict, Any
import akshare as ak

async def execute(date: str) -> List[Dict[str, Any]]:
    """
    异步获取深圳证券交易所融资融券汇总数据
    
    Args:
        date: 交易日期，格式为YYYYMMDD
        
    Returns:
        融资融券数据列表，每个元素为一个字典
        
    Raises:
        Exception: 当akshare接口调用失败时抛出异常
    """
    try:
        # 调用akshare同步接口，使用await在异步环境中执行
        df = await asyncio.get_event_loop().run_in_executor(
            None, 
            lambda: ak.stock_margin_szse(date=date)
        )
        
        # 将DataFrame转换为List[Dict]格式
        result = df.to_dict(orient="records")
        return result
    except Exception as e:
        raise Exception(f"获取深圳证券交易所融资融券数据失败: {e}")

def test():
    """
    同步测试方法，用于自动化测试
    
    Raises:
        原样抛出execute方法中的异常
    """
    # 使用示例中的参数进行测试
    test_date = "20240411"
    try:
        result = asyncio.run(execute(date=test_date))
        print(result)
        return result
    except Exception as e:
        print(f"测试失败: {e}")
        raise

if __name__ == "__main__":
    # 演示如何调用异步函数
    async def main():
        try:
            data = await execute(date="20240411")
            print(data)
        except Exception as e:
            print(f"调用失败: {e}")
    
    asyncio.run(main())