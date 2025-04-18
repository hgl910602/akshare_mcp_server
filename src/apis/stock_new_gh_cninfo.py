import asyncio
from typing import List, Dict, Any
import akshare as ak

async def execute() -> List[Dict[str, Any]]:
    """
    获取巨潮资讯-数据中心-新股数据-新股过会数据
    
    Returns:
        List[Dict[str, Any]]: 新股过会数据列表，每个元素是一个字典代表一条记录
        
    Raises:
        Exception: 当获取数据失败时抛出异常
    """
    try:
        # 调用akshare接口获取数据
        df = ak.stock_new_gh_cninfo()
        # 将DataFrame转换为List[Dict]格式
        result = df.to_dict(orient='records')
        return result
    except Exception as e:
        raise Exception(f"获取新股过会数据失败: {str(e)}")

def test() -> List[Dict[str, Any]]:
    """
    同步测试方法，用于自动化测试
    
    Returns:
        List[Dict[str, Any]]: 新股过会数据列表
        
    Raises:
        Exception: 当execute方法执行失败时抛出异常
    """
    try:
        return asyncio.run(execute())
    except Exception as e:
        raise Exception(f"测试执行失败: {str(e)}")

if __name__ == '__main__':
    # 演示如何调用异步函数
    async def main():
        try:
            data = await execute()
            print(data)
        except Exception as e:
            print(f"Error: {e}")
    
    asyncio.run(main())