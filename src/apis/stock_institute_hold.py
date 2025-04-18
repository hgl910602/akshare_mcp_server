import asyncio
from typing import List, Dict, Any
import akshare as ak

async def execute(symbol: str) -> List[Dict[str, Any]]:
    """
    异步获取新浪财经-机构持股-机构持股一览表数据
    
    Args:
        symbol: 从2005年开始, {"一季报":1, "中报":2 "三季报":3 "年报":4}, 
                e.g., "20191"表示2019年一季报, "20193"表示2019年三季报
    
    Returns:
        机构持股数据的字典列表
        
    Raises:
        Exception: 当akshare接口调用失败时抛出
    """
    try:
        # 调用akshare同步接口，使用await在异步环境中执行
        df = await asyncio.get_event_loop().run_in_executor(
            None, 
            lambda: ak.stock_institute_hold(symbol=symbol)
        )
        # 将DataFrame转换为字典列表
        return df.to_dict("records")
    except Exception as e:
        raise Exception(f"Failed to fetch stock institute hold data: {str(e)}")

def test():
    """
    同步测试方法，用于自动化测试
    
    Returns:
        机构持股数据的字典列表
        
    Raises:
        Exception: 当execute方法调用失败时抛出
    """
    # 使用示例中的参数进行测试
    symbol = "20201"
    try:
        return asyncio.run(execute(symbol))
    except Exception as e:
        raise Exception(f"Test failed: {str(e)}")

if __name__ == "__main__":
    # 演示如何调用异步函数
    async def main():
        try:
            data = await execute("20201")
            print(data[:5])  # 打印前5条数据
        except Exception as e:
            print(f"Error occurred: {e}")
    
    asyncio.run(main())