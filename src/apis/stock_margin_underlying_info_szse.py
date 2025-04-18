import asyncio
from typing import List, Dict, Any
import akshare as ak

async def execute(date: str) -> List[Dict[str, Any]]:
    """
    异步获取深圳证券交易所融资融券标的证券信息
    
    Args:
        date: 日期, 格式为"YYYYMMDD"
        
    Returns:
        融资融券标的证券信息列表，每个证券信息以字典形式存储
        
    Raises:
        Exception: 当akshare接口调用失败时抛出异常
    """
    try:
        # 调用akshare同步接口，使用await在异步环境中执行
        df = await asyncio.get_event_loop().run_in_executor(
            None, 
            ak.stock_margin_underlying_info_szse, 
            date
        )
        # 将DataFrame转换为List[Dict]格式
        return df.to_dict('records')
    except Exception as e:
        raise Exception(f"获取深圳证券交易所融资融券标的证券信息失败: {e}")

def test():
    """
    同步测试方法，用于自动化测试
    
    Returns:
        融资融券标的证券信息列表
        
    Raises:
        异常上抛，不捕获
    """
    # 使用示例中的测试日期
    test_date = "20210727"
    return asyncio.run(execute(test_date))

if __name__ == '__main__':
    # 演示如何调用异步函数
    async def main():
        try:
            result = await execute(date="20210727")
            print(result)
        except Exception as e:
            print(f"Error: {e}")
    
    asyncio.run(main())