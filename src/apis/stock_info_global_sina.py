import asyncio
from typing import List, Dict, Any
import akshare as ak

async def execute() -> List[Dict[str, Any]]:
    """
    异步获取新浪财经-全球财经快讯数据
    
    Returns:
        List[Dict[str, Any]]: 返回全球财经快讯数据列表，每个条目包含时间和内容
        
    Raises:
        Exception: 当数据获取失败时抛出异常
    """
    try:
        # 调用akshare接口获取数据
        df = ak.stock_info_global_sina()
        # 将DataFrame转换为List[Dict]格式
        result = df.to_dict(orient='records')
        return result
    except Exception as e:
        raise Exception(f"Failed to fetch global stock info from sina: {str(e)}")

def test() -> List[Dict[str, Any]]:
    """
    同步测试函数，用于验证execute方法
    
    Returns:
        List[Dict[str, Any]]: 返回全球财经快讯数据
        
    Raises:
        Exception: 当execute方法执行失败时抛出异常
    """
    return asyncio.run(execute())

if __name__ == '__main__':
    # 演示如何异步调用execute方法
    async def main():
        try:
            data = await execute()
            for item in data:
                print(f"时间: {item['时间']}, 内容: {item['内容']}")
        except Exception as e:
            print(f"Error occurred: {e}")
    
    asyncio.run(main())