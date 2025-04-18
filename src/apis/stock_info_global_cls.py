import asyncio
from typing import List, Dict, Any
import akshare as ak

async def execute(symbol: str = "全部") -> List[Dict[str, Any]]:
    """
    异步获取财联社-电报信息
    
    Args:
        symbol: 选择类型, "全部" 或 "重点"
    
    Returns:
        List[Dict[str, Any]]: 包含电报信息的字典列表
    
    Raises:
        Exception: 当获取数据失败时抛出异常
    """
    try:
        # 调用akshare的同步接口，使用await包装
        df = await asyncio.get_event_loop().run_in_executor(
            None, 
            lambda: ak.stock_info_global_cls(symbol=symbol)
        
        # 将DataFrame转换为List[Dict]格式
        result = df.to_dict("records")
        return result
    except Exception as e:
        raise Exception(f"获取财联社电报信息失败: {str(e)}")


def test():
    """
    同步测试方法，用于自动化测试
    
    Raises:
        Exception: 当execute方法执行失败时抛出异常
    """
    try:
        # 模拟调用示例参数
        result = asyncio.run(execute(symbol="全部"))
        print(f"测试成功，获取到{len(result)}条数据")
        return result
    except Exception as e:
        print(f"测试失败: {str(e)}")
        raise


if __name__ == "__main__":
    # 演示如何调用异步函数
    async def main():
        try:
            data = await execute(symbol="全部")
            print(f"获取到{len(data)}条数据:")
            for item in data[:3]:  # 打印前3条作为示例
                print(item)
        except Exception as e:
            print(f"执行出错: {str(e)}")
    
    asyncio.run(main())