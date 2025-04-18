import asyncio
from typing import List, Dict, Any
import akshare as ak

async def execute(symbol: str = "可燃冰") -> List[Dict[str, Any]]:
    """
    异步获取东方财富网-行情中心-沪深京板块-概念板块-实时行情
    
    Args:
        symbol: 概念板块名称，默认为"可燃冰"
    
    Returns:
        List[Dict[str, Any]]: 返回概念板块实时行情数据列表
    
    Raises:
        Exception: 当获取数据失败时抛出异常
    """
    try:
        # 调用akshare同步接口，使用await在异步环境中执行
        df = await asyncio.get_event_loop().run_in_executor(
            None, 
            ak.stock_board_concept_spot_em,
            symbol
        )
        # 将DataFrame转换为List[Dict]格式
        return df.to_dict("records")
    except Exception as e:
        raise Exception(f"获取概念板块实时行情失败: {e}")

def test():
    """
    同步测试方法，用于自动化测试
    
    Raises:
        Exception: 当execute方法执行失败时抛出异常
    """
    try:
        result = asyncio.run(execute("可燃冰"))
        print("测试成功，返回数据条数:", len(result))
        return result
    except Exception as e:
        print("测试失败:", str(e))
        raise

if __name__ == "__main__":
    # 演示如何调用异步函数
    async def main():
        try:
            data = await execute("可燃冰")
            print("获取数据成功:")
            for item in data[:3]:  # 打印前3条数据
                print(item)
        except Exception as e:
            print(f"执行出错: {e}")
    
    asyncio.run(main())