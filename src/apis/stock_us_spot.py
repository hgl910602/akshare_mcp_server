import asyncio
from typing import List, Dict, Any
import akshare as ak

async def execute() -> List[Dict[str, Any]]:
    """
    异步获取美股实时行情数据(新浪财经)
    
    Returns:
        List[Dict[str, Any]]: 美股实时行情数据列表，每个元素是一个字典代表一只股票的数据
        
    Raises:
        Exception: 当数据获取失败时抛出异常
    """
    try:
        # 调用akshare同步接口，使用await在异步环境中执行
        df = await asyncio.get_event_loop().run_in_executor(
            None, 
            ak.stock_us_spot
        )
        # 将DataFrame转换为List[Dict]格式
        return df.to_dict("records")
    except Exception as e:
        raise Exception(f"Failed to fetch US stock spot data: {str(e)}")

def test() -> List[Dict[str, Any]]:
    """
    同步测试方法，用于自动化测试
    
    Returns:
        List[Dict[str, Any]]: 美股实时行情数据
        
    Raises:
        Exception: 当数据获取失败时抛出异常
    """
    try:
        return asyncio.run(execute())
    except Exception as e:
        raise Exception(f"Test failed: {str(e)}")

if __name__ == "__main__":
    # 演示如何调用异步函数
    async def main():
        try:
            data = await execute()
            print(f"Got {len(data)} US stock records")
            if len(data) > 0:
                print("Sample record:")
                print(data[0])
        except Exception as e:
            print(f"Error: {e}")
    
    asyncio.run(main())