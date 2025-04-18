import asyncio
from typing import List, Dict, Any
import akshare as ak

async def execute() -> List[Dict[str, Any]]:
    """
    东方财富网-数据中心-特色数据-股权质押-重要股东股权质押明细
    
    Returns:
        List[Dict[str, Any]]: 重要股东股权质押明细数据
    """
    try:
        # 调用akshare接口获取数据
        df = ak.stock_gpzy_pledge_ratio_detail_em()
        
        # 将DataFrame转换为List[Dict]格式
        result = df.to_dict(orient='records')
        return result
    except Exception as e:
        raise Exception(f"获取股权质押明细数据失败: {str(e)}")

def test() -> List[Dict[str, Any]]:
    """
    同步测试方法
    
    Returns:
        List[Dict[str, Any]]: 重要股东股权质押明细数据
        
    Raises:
        Exception: 当execute方法执行失败时抛出异常
    """
    try:
        return asyncio.run(execute())
    except Exception as e:
        raise e

if __name__ == '__main__':
    # 演示如何调用异步函数
    async def main():
        try:
            data = await execute()
            print(data[:2])  # 打印前两条数据
        except Exception as e:
            print(f"Error: {e}")
    
    asyncio.run(main())