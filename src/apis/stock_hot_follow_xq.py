import asyncio
from typing import Any, Dict, List
import akshare as ak

async def execute(symbol: str = "最热门") -> List[Dict[str, Any]]:
    """
    异步获取雪球-沪深股市-热度排行榜-关注排行榜数据
    
    Args:
        symbol: 排行榜类型, "本周新增" 或 "最热门"
    
    Returns:
        返回处理后的数据列表, 每个元素为包含股票信息的字典
    
    Raises:
        Exception: 当akshare接口调用失败时抛出异常
    """
    try:
        # 调用akshare同步接口
        df = ak.stock_hot_follow_xq(symbol=symbol)
        
        # 将DataFrame转换为List[Dict]格式
        result = []
        for _, row in df.iterrows():
            item = {
                "股票代码": row["股票代码"],
                "股票简称": row["股票简称"],
                "关注": float(row["关注"]),
                "最新价": float(row["最新价"]),
            }
            result.append(item)
        return result
    except Exception as e:
        raise Exception(f"获取雪球关注排行榜数据失败: {e}")

def test():
    """
    同步测试方法, 用于自动化测试
    
    Raises:
        原样抛出execute方法中的异常
    """
    try:
        # 使用asyncio.run运行异步方法
        result = asyncio.run(execute(symbol="最热门"))
        print("测试成功, 获取数据条数:", len(result))
        return result
    except Exception as e:
        print("测试失败:", str(e))
        raise

if __name__ == "__main__":
    # 演示如何调用异步函数
    async def main():
        try:
            data = await execute(symbol="最热门"))
            print("获取数据成功:")
            for item in data[:3]:  # 打印前3条数据
                print(item)
        except Exception as e:
            print("调用失败:", e)
    
    asyncio.run(main())