import asyncio
from typing import Any, Dict, List
import akshare as ak

async def execute(symbol: str = "430489") -> List[Dict[str, Any]]:
    """
    异步获取北京证券交易所-信息披露-监管信息-董监高及相关人员持股变动数据
    
    Args:
        symbol: 股票代码或"全部", 默认为"430489"
    
    Returns:
        List[Dict[str, Any]]: 持股变动数据列表
    
    Raises:
        Exception: 当获取数据失败时抛出异常
    """
    try:
        # 调用akshare同步接口，使用await包装
        df = await asyncio.get_event_loop().run_in_executor(
            None, 
            lambda: ak.stock_share_hold_change_bse(symbol=symbol)
        )
        # 将DataFrame转换为List[Dict]格式
        return df.to_dict("records")
    except Exception as e:
        raise Exception(f"获取持股变动数据失败: {e}")

def test():
    """
    同步测试方法，用于自动化测试
    
    Raises:
        Exception: 当execute方法执行失败时抛出异常
    """
    try:
        result = asyncio.run(execute(symbol="430489"))
        print(f"测试成功，获取到{len(result)}条数据")
        return result
    except Exception as e:
        print(f"测试失败: {e}")
        raise

if __name__ == "__main__":
    # 演示如何调用异步函数
    async def main():
        try:
            data = await execute(symbol="430489")
            print(f"获取到{len(data)}条数据:")
            for item in data[:3]:  # 打印前3条数据
                print(item)
        except Exception as e:
            print(f"执行出错: {e}")
    
    asyncio.run(main())