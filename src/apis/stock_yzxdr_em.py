import asyncio
from typing import List, Dict, Any
import akshare as ak

async def execute(date: str = "20210331") -> List[Dict[str, Any]]:
    """
    获取东方财富网-数据中心-特色数据-一致行动人数据
    
    Args:
        date: 每年的季度末时间点, 例如: "20210331"
    
    Returns:
        List[Dict[str, Any]]: 一致行动人数据列表
        
    Raises:
        Exception: 当获取数据失败时抛出异常
    """
    try:
        # 调用akshare接口获取数据
        df = ak.stock_yzxdr_em(date=date)
        # 将DataFrame转换为List[Dict]格式
        result = df.to_dict("records")
        return result
    except Exception as e:
        raise Exception(f"获取一致行动人数据失败: {e}")

def test():
    """
    同步测试方法，用于自动化测试
    
    Returns:
        List[Dict[str, Any]]: 一致行动人数据列表
        
    Raises:
        Exception: 当获取数据失败时抛出异常
    """
    try:
        # 使用示例参数调用execute方法
        return asyncio.run(execute(date="20210331"))
    except Exception as e:
        raise e

if __name__ == "__main__":
    # 演示如何调用异步函数
    async def main():
        try:
            data = await execute(date="20210331")
            print(data[:5])  # 打印前5条数据
        except Exception as e:
            print(f"Error: {e}")
    
    asyncio.run(main())