import asyncio
from typing import List, Dict, Any
import akshare as ak

async def execute(symbol: str = "SZ000665") -> List[Dict[str, Any]]:
    """
    东方财富-个股人气榜-热门关键词
    :param symbol: 股票代码，如 "SZ000665"
    :return: List[Dict[str, Any]] 转换后的数据列表
    """
    try:
        # 调用akshare的同步接口
        df = ak.stock_hot_keyword_em(symbol=symbol)
        # 将DataFrame转换为List[Dict]格式
        return df.to_dict("records")
    except Exception as e:
        raise RuntimeError(f"获取股票热门关键词数据失败: {e}")

def test():
    """
    同步测试方法，用于自动化测试
    """
    try:
        result = asyncio.run(execute(symbol="SZ000665"))
        print("测试成功，返回数据条数:", len(result))
        return result
    except Exception as e:
        print("测试失败:", str(e))
        raise

if __name__ == "__main__":
    # 演示如何调用异步函数
    async def main():
        try:
            data = await execute(symbol="SZ000665")
            print("获取到的数据:")
            for item in data[:3]:  # 打印前3条数据
                print(item)
        except Exception as e:
            print(f"发生错误: {e}")
    
    asyncio.run(main())