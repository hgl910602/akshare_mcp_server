import asyncio
from typing import List, Dict, Any
import akshare as ak

async def execute(symbol: str = "主板A股") -> List[Dict[str, Any]]:
    """
    异步获取上海证券交易所股票代码和简称数据
    
    Args:
        symbol: 股票类型，可选值: "主板A股", "主板B股", "科创板"
        
    Returns:
        返回股票信息列表，每个股票信息为字典格式
        
    Raises:
        Exception: 当akshare接口调用失败时抛出异常
    """
    try:
        # 调用akshare同步接口，使用await包装
        df = await asyncio.get_event_loop().run_in_executor(
            None, 
            lambda: ak.stock_info_sh_name_code(symbol=symbol)
        )
        # 将DataFrame转换为List[Dict]格式
        return df.to_dict("records")
    except Exception as e:
        raise Exception(f"获取上证股票列表失败: {str(e)}")

def test() -> List[Dict[str, Any]]:
    """
    同步测试方法，用于自动化测试
    
    Returns:
        返回股票信息列表
        
    Raises:
        原样抛出execute方法可能产生的异常
    """
    return asyncio.run(execute(symbol="主板A股"))

if __name__ == "__main__":
    # 演示异步调用方式
    async def main():
        try:
            data = await execute(symbol="主板A股")
            print(f"获取到{len(data)}条上证A股数据")
            if data:
                print("示例数据:")
                print(data[0])
        except Exception as e:
            print(f"调用失败: {e}")
    
    asyncio.run(main())