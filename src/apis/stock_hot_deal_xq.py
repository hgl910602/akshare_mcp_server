import asyncio
from typing import List, Dict, Any
import akshare as ak

async def execute(symbol: str = "最热门") -> List[Dict[str, Any]]:
    """
    异步获取雪球-沪深股市-热度排行榜-交易排行榜数据
    
    Args:
        symbol: 排行榜类型, "本周新增" 或 "最热门"
    
    Returns:
        返回处理后的字典列表数据
    
    Raises:
        Exception: 当akshare接口调用失败时抛出异常
    """
    try:
        # 调用akshare同步接口
        df = ak.stock_hot_deal_xq(symbol=symbol)
        
        # 转换为List[Dict]格式
        result = df.to_dict(orient="records")
        return result
    except Exception as e:
        raise Exception(f"获取雪球热度排行榜数据失败: {str(e)}")

def test():
    """
    同步测试方法，用于自动化测试
    
    Raises:
        会抛出execute方法中的异常
    """
    try:
        # 使用默认参数测试
        data = asyncio.run(execute(symbol="最热门"))
        print(f"获取到{len(data)}条数据")
        return data
    except Exception as e:
        print(f"测试失败: {str(e)}")
        raise

if __name__ == "__main__":
    # 演示如何调用异步函数
    async def main():
        try:
            data = await execute(symbol="最热门")
            print(f"获取到{len(data)}条数据:")
            for item in data[:3]:  # 打印前3条作为示例
                print(item)
        except Exception as e:
            print(f"调用失败: {str(e)}")
    
    asyncio.run(main())