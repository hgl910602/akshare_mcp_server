import asyncio
from typing import List, Dict, Any
import akshare as ak

async def execute(symbol: str, indicator: str) -> List[Dict[str, Any]]:
    """
    异步获取百度股市通- A 股或指数-股评-投票数据
    
    Args:
        symbol: A 股股票或指数代码
        indicator: 类型，可选值为 "指数" 或 "股票"
    
    Returns:
        返回处理后的投票数据列表
    
    Raises:
        Exception: 当获取数据失败时抛出异常
    """
    try:
        # 调用akshare同步接口获取数据
        df = ak.stock_zh_vote_baidu(symbol=symbol, indicator=indicator)
        
        # 将DataFrame转换为List[Dict]格式
        result = df.to_dict(orient="records")
        return result
    except Exception as e:
        raise Exception(f"获取百度股市通投票数据失败: {str(e)}")

def test():
    """
    同步测试方法，用于自动化测试
    
    Raises:
        异常上抛不捕获
    """
    # 使用示例参数调用异步execute方法
    result = asyncio.run(execute(symbol="000001", indicator="指数"))
    return result

if __name__ == "__main__":
    # 演示如何调用异步函数并打印结果
    async def main():
        try:
            data = await execute(symbol="000001", indicator="指数")
            print(data)
        except Exception as e:
            print(f"Error: {e}")
    
    asyncio.run(main())