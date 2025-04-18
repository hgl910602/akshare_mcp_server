import asyncio
from typing import List, Dict, Any
import akshare as ak

async def execute() -> List[Dict[str, Any]]:
    """
    获取同花顺财经-全球财经直播数据
    
    Returns:
        List[Dict[str, Any]]: 全球财经直播数据列表，每个元素包含标题、内容、发布时间和链接
    """
    try:
        # 调用akshare接口获取数据
        df = ak.stock_info_global_ths()
        
        # 将DataFrame转换为List[Dict]格式
        result = df.to_dict(orient='records')
        return result
    except Exception as e:
        raise RuntimeError(f"获取全球财经直播数据失败: {e}")

def test() -> List[Dict[str, Any]]:
    """
    同步测试方法，用于自动化测试
    
    Returns:
        List[Dict[str, Any]]: 全球财经直播数据
        
    Raises:
        Exception: 当execute方法执行出错时抛出
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
            print(f"获取到{len(data)}条全球财经直播数据:")
            for item in data[:3]:  # 打印前3条数据
                print(item)
        except Exception as e:
            print(f"发生错误: {e}")
    
    asyncio.run(main())