import asyncio
from typing import List, Dict, Any
import akshare as ak

async def execute(symbol: str) -> List[Dict[str, Any]]:
    """
    异步获取东方财富-行情中心-盘口异动数据
    
    Args:
        symbol: 异动类型，如"大笔买入"、"火箭发射"等
        
    Returns:
        List[Dict[str, Any]]: 返回异动数据列表，每个元素是一个字典
        
    Raises:
        Exception: 当获取数据失败时抛出异常
    """
    try:
        # 调用akshare的同步接口，使用run_in_executor避免阻塞事件循环
        loop = asyncio.get_running_loop()
        df = await loop.run_in_executor(None, ak.stock_changes_em, symbol)
        return df.to_dict('records')
    except Exception as e:
        raise Exception(f"获取盘口异动数据失败: {str(e)}")

def test():
    """
    同步测试方法，用于自动化测试
    
    Raises:
        Exception: 当execute方法执行失败时抛出异常
    """
    try:
        # 使用示例参数调用execute方法
        result = asyncio.run(execute(symbol="大笔买入"))
        print(result)
    except Exception as e:
        raise Exception(f"测试失败: {str(e)}")

if __name__ == '__main__':
    # 演示如何调用异步函数
    async def main():
        try:
            data = await execute(symbol="大笔买入")
            print(data)
        except Exception as e:
            print(f"Error: {e}")
    
    asyncio.run(main())