import asyncio
from typing import List, Dict, Any
import akshare as ak

async def execute(date: str = "20240930") -> List[Dict[str, Any]]:
    """
    异步获取东方财富网-数据中心-特色数据-商誉-行业商誉数据
    
    Args:
        date: 查询日期，格式如"20240930"
        
    Returns:
        行业商誉数据列表，每个元素为包含字段的字典
        
    Raises:
        Exception: 当接口调用失败时抛出异常
    """
    try:
        # 调用akshare同步接口，使用await在异步环境中执行
        df = await asyncio.get_event_loop().run_in_executor(
            None, 
            lambda: ak.stock_sy_hy_em(date=date)
        )
        # 将DataFrame转换为List[Dict]格式
        return df.to_dict("records")
    except Exception as e:
        raise Exception(f"获取行业商誉数据失败: {str(e)}")

def test():
    """
    同步测试方法，用于自动化测试
    
    Returns:
        行业商誉数据列表
        
    Raises:
        原样抛出execute方法中的异常
    """
    try:
        return asyncio.run(execute(date="20240930"))
    except Exception as e:
        raise e

if __name__ == "__main__":
    # 演示异步调用
    async def main():
        try:
            data = await execute(date="20240930")
            print(data)
        except Exception as e:
            print(f"Error: {e}")
    
    asyncio.run(main())