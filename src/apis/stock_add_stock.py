import asyncio
from typing import List, Dict, Any
import akshare as ak

async def execute(symbol: str) -> List[Dict[str, Any]]:
    """
    异步获取股票增发数据
    
    Args:
        symbol: 股票代码
        
    Returns:
        增发数据列表，每个元素为字典形式
        
    Raises:
        Exception: 当akshare接口调用失败时抛出
    """
    try:
        # 调用akshare同步接口，使用await在异步环境中执行
        df = await asyncio.get_event_loop().run_in_executor(
            None, 
            ak.stock_add_stock, 
            symbol
        )
        # 将DataFrame转换为List[Dict]格式
        return df.to_dict('records')
    except Exception as e:
        raise Exception(f"获取股票增发数据失败: {e}")

def test():
    """
    同步测试方法，用于自动化测试
    
    Raises:
        Exception: 当execute方法调用失败时抛出
    """
    # 使用示例中的参数进行测试
    symbol = "600004"
    try:
        result = asyncio.run(execute(symbol))
        print(result)
        return result
    except Exception as e:
        raise Exception(f"测试失败: {e}")

if __name__ == '__main__':
    # 演示如何调用异步函数
    async def main():
        try:
            result = await execute("600004")
            print(result)
        except Exception as e:
            print(f"Error: {e}")
    
    asyncio.run(main())