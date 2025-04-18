import asyncio
from typing import List, Dict, Any
import akshare as ak

async def execute(symbol: str = "全部") -> List[Dict[str, Any]]:
    """
    异步获取巨潮资讯-实际控制人持股变动数据
    
    Args:
        symbol: 控制类型, 可选 {"单独控制", "实际控制人", "一致行动人", "家族控制", "全部"}
    
    Returns:
        实际控制人持股变动数据列表
    
    Raises:
        Exception: 当akshare接口调用失败时抛出
    """
    try:
        # 调用akshare同步接口，使用asyncio.to_thread转为异步
        df = await asyncio.to_thread(ak.stock_hold_control_cninfo, symbol=symbol)
        return df.to_dict(orient="records")
    except Exception as e:
        raise Exception(f"获取实际控制人持股变动数据失败: {e}")

def test() -> List[Dict[str, Any]]:
    """
    同步测试方法，用于自动化测试
    
    Returns:
        实际控制人持股变动数据列表
    
    Raises:
        Exception: 当execute方法调用失败时抛出
    """
    try:
        return asyncio.run(execute(symbol="全部"))
    except Exception as e:
        raise Exception(f"测试execute方法失败: {e}")

if __name__ == "__main__":
    # 演示异步调用
    async def main():
        try:
            data = await execute(symbol="全部")
            print(f"获取到{len(data)}条数据")
            if len(data) > 0:
                print("第一条数据示例:")
                print(data[0])
        except Exception as e:
            print(f"调用失败: {e}")
    
    asyncio.run(main())