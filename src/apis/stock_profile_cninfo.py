import asyncio
from typing import Any, Dict, List
import akshare as ak

async def execute(symbol: str) -> List[Dict[str, Any]]:
    """
    异步获取巨潮资讯个股公司概况信息
    
    Args:
        symbol: 股票代码，例如 "600030"
        
    Returns:
        公司概况信息列表，每个条目是一个字典
        
    Raises:
        Exception: 当接口调用失败时抛出异常
    """
    try:
        # 调用akshare接口获取数据
        df = ak.stock_profile_cninfo(symbol=symbol)
        # 将DataFrame转换为List[Dict]格式
        result = df.to_dict(orient="records")
        return result
    except Exception as e:
        raise Exception(f"获取公司概况信息失败: {str(e)}")

def test():
    """
    同步测试方法，用于自动化测试
    
    Raises:
        异常上抛，不捕获
    """
    # 使用示例中的参数进行测试
    result = asyncio.run(execute(symbol="600030"))
    return result

if __name__ == "__main__":
    # 演示如何调用异步函数
    async def main():
        try:
            data = await execute(symbol="600030")
            print(data)
        except Exception as e:
            print(f"Error: {e}")
    
    asyncio.run(main())