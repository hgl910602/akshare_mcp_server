import asyncio
from typing import List, Dict, Any
import akshare as ak

async def execute() -> List[Dict[str, Any]]:
    """
    获取东方财富-个股人气榜-人气榜-港股市场数据
    
    Returns:
        List[Dict[str, Any]]: 港股市场人气榜数据列表
    """
    try:
        # 调用akshare接口获取数据
        df = ak.stock_hk_hot_rank_em()
        
        # 将DataFrame转换为List[Dict]格式
        result = df.to_dict(orient='records')
        return result
    except Exception as e:
        raise RuntimeError(f"获取港股人气榜数据失败: {str(e)}")

def test() -> List[Dict[str, Any]]:
    """
    同步测试方法
    
    Returns:
        List[Dict[str, Any]]: 港股市场人气榜数据列表
        
    Raises:
        Exception: 当execute方法执行失败时抛出异常
    """
    return asyncio.run(execute())

if __name__ == '__main__':
    # 异步调用示例
    async def main():
        try:
            data = await execute()
            print(data)
        except Exception as e:
            print(f"Error: {e}")
    
    asyncio.run(main())