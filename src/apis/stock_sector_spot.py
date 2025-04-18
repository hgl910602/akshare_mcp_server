import asyncio
from typing import List, Dict, Any
import akshare as ak

async def execute(indicator: str = "新浪行业") -> List[Dict[str, Any]]:
    """
    异步获取新浪行业板块行情数据
    
    Args:
        indicator: 板块类型, 可选: "新浪行业", "启明星行业", "概念", "地域", "行业"
        
    Returns:
        板块行情数据列表, 每个元素为一个字典
        
    Raises:
        Exception: 当获取数据失败时抛出异常
    """
    try:
        # 使用akshare同步接口, 通过run_in_executor转为异步
        loop = asyncio.get_event_loop()
        df = await loop.run_in_executor(
            None, 
            lambda: ak.stock_sector_spot(indicator=indicator)
        )
        return df.to_dict(orient="records")
    except Exception as e:
        raise Exception(f"获取板块行情数据失败: {str(e)}")

def test():
    """
    同步测试方法, 用于自动化测试
    
    Raises:
        Exception: 当execute执行失败时抛出异常
    """
    try:
        # 使用asyncio.run执行异步方法
        result = asyncio.run(execute(indicator="新浪行业"))
        print(f"测试成功, 获取到{len(result)}条数据")
        return result
    except Exception as e:
        print(f"测试失败: {str(e)}")
        raise

if __name__ == "__main__":
    # 演示如何调用异步函数
    async def main():
        try:
            data = await execute(indicator="新浪行业")
            print(f"获取到{len(data)}条数据")
            if len(data) > 0:
                print("第一条数据示例:")
                print(data[0])
        except Exception as e:
            print(f"执行出错: {str(e)}")
    
    asyncio.run(main())