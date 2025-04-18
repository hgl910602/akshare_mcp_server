import asyncio
from typing import List, Dict, Any
import akshare as ak

async def execute() -> List[Dict[str, Any]]:
    """
    异步获取东方财富网-数据中心-股东大会数据
    
    Returns:
        List[Dict[str, Any]]: 股东大会数据列表，每个元素是一个字典代表一条记录
        
    Raises:
        Exception: 当获取数据失败时抛出异常
    """
    try:
        # 调用akshare的同步接口，使用asyncio.to_thread转为异步
        df = await asyncio.to_thread(ak.stock_gddh_em)
        # 将DataFrame转换为List[Dict]格式
        return df.to_dict(orient='records')
    except Exception as e:
        raise Exception(f"获取股东大会数据失败: {e}")

def test() -> List[Dict[str, Any]]:
    """
    同步测试方法，用于自动化测试
    
    Returns:
        List[Dict[str, Any]]: 股东大会数据列表
        
    Raises:
        Exception: 当execute方法执行失败时抛出异常
    """
    return asyncio.run(execute())

if __name__ == '__main__':
    # 演示如何调用异步函数
    async def main():
        try:
            data = await execute()
            print(f"获取到{len(data)}条股东大会数据")
            if data:
                print("第一条数据示例:")
                print(data[0])
        except Exception as e:
            print(f"发生错误: {e}")
    
    asyncio.run(main())