import asyncio
from typing import List, Dict, Any
import akshare as ak

async def execute() -> List[Dict[str, Any]]:
    """
    异步获取乐估乐股-底部研究-巴菲特指标数据
    
    Returns:
        List[Dict[str, Any]]: 包含巴菲特指标数据的字典列表
        
    Raises:
        Exception: 当获取数据失败时抛出异常
    """
    try:
        # 调用akshare接口获取数据
        df = ak.stock_buffett_index_lg()
        
        # 将DataFrame转换为List[Dict]格式
        result = df.to_dict("records")
        return result
    except Exception as e:
        raise Exception(f"获取巴菲特指标数据失败: {e}")

def test() -> List[Dict[str, Any]]:
    """
    同步测试方法，用于自动化测试
    
    Returns:
        List[Dict[str, Any]]: 包含巴菲特指标数据的字典列表
        
    Raises:
        Exception: 当获取数据失败时抛出异常
    """
    try:
        return asyncio.run(execute())
    except Exception as e:
        raise e

if __name__ == "__main__":
    # 演示如何调用异步函数
    async def main():
        try:
            data = await execute()
            print(data)
        except Exception as e:
            print(f"Error: {e}")
    
    asyncio.run(main())