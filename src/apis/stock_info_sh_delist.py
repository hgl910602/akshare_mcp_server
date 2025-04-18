import asyncio
from typing import List, Dict, Any
import akshare as ak

async def execute(symbol: str = "全部") -> List[Dict[str, Any]]:
    """
    获取上海证券交易所暂停/终止上市股票信息
    
    Args:
        symbol: 股票市场类型, 可选 {"全部", "沪市", "科创板"}
    
    Returns:
        上海证券交易所暂停/终止上市股票信息列表
        
    Raises:
        Exception: 当获取数据失败时抛出异常
    """
    try:
        # 调用akshare接口获取数据
        df = ak.stock_info_sh_delist(symbol=symbol)
        # 将DataFrame转换为List[Dict]格式
        return df.to_dict("records")
    except Exception as e:
        raise Exception(f"获取上海证券交易所暂停/终止上市股票信息失败: {e}")

def test():
    """
    同步测试方法，用于自动化测试
    
    Raises:
        Exception: 当execute方法执行失败时抛出异常
    """
    try:
        # 使用asyncio.run运行异步方法
        result = asyncio.run(execute(symbol="全部"))
        print("测试成功，获取数据条数:", len(result))
        return result
    except Exception as e:
        print("测试失败:", str(e))
        raise

if __name__ == "__main__":
    # 演示如何调用异步函数
    async def main():
        try:
            data = await execute(symbol="全部")
            print("获取数据成功，前5条记录:")
            for item in data[:5]:
                print(item)
        except Exception as e:
            print(f"发生错误: {e}")
    
    asyncio.run(main())