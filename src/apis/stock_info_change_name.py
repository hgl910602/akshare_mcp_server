import asyncio
from typing import List, Dict, Any
import akshare as ak

async def execute(symbol: str) -> List[Dict[str, Any]]:
    """
    异步获取股票曾用名信息
    
    Args:
        symbol: 股票代码, 例如 "000503"
        
    Returns:
        包含股票曾用名信息的字典列表
        
    Raises:
        Exception: 当akshare接口调用失败时抛出
    """
    try:
        # 调用akshare同步接口，使用await包装
        result = await asyncio.get_event_loop().run_in_executor(
            None, 
            ak.stock_info_change_name, 
            symbol
        )
        # 将DataFrame转换为List[Dict]格式
        return result.to_dict("records")
    except Exception as e:
        raise Exception(f"获取股票曾用名信息失败: {e}")

def test():
    """
    同步测试方法，用于自动化测试
    
    Raises:
        Exception: 当execute方法调用失败时抛出
    """
    try:
        # 使用示例参数调用execute方法
        result = asyncio.run(execute(symbol="000503"))
        print(result)
    except Exception as e:
        raise Exception(f"测试失败: {e}")

if __name__ == "__main__":
    # 演示如何调用异步函数
    async def main():
        try:
            result = await execute(symbol="000503")
            print(result)
        except Exception as e:
            print(f"Error: {e}")
    
    asyncio.run(main())