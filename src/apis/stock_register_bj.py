import asyncio
from typing import List, Dict, Any
import akshare as ak

async def execute() -> List[Dict[str, Any]]:
    """
    异步获取北交所IPO审核信息
    
    Returns:
        List[Dict[str, Any]]: 北交所IPO审核信息列表，每个元素为一个字典，包含各字段信息
        
    Raises:
        Exception: 当获取数据失败时抛出异常
    """
    try:
        # 调用akshare同步接口获取数据
        df = ak.stock_register_bj()
        # 将DataFrame转换为List[Dict]格式
        return df.to_dict("records")
    except Exception as e:
        raise Exception(f"获取北交所IPO审核信息失败: {e}")

def test() -> List[Dict[str, Any]]:
    """
    同步测试函数，用于自动化测试
    
    Returns:
        List[Dict[str, Any]]: 北交所IPO审核信息列表
        
    Raises:
        Exception: 当execute方法执行失败时抛出异常
    """
    try:
        return asyncio.run(execute())
    except Exception as e:
        raise Exception(f"测试执行失败: {e}")

if __name__ == "__main__":
    # 演示如何调用异步函数
    async def main():
        try:
            data = await execute()
            print(data[:2])  # 打印前两条数据示例
        except Exception as e:
            print(f"执行出错: {e}")
    
    asyncio.run(main())