import asyncio
from typing import List, Dict, Any
import akshare as ak

async def execute() -> List[Dict[str, Any]]:
    """
    异步获取财新网-财新数据通-内容精选数据
    
    Returns:
        List[Dict[str, Any]]: 返回处理后的财经新闻数据列表
    """
    try:
        # 调用akshare接口获取数据
        df = ak.stock_news_main_cx()
        
        # 将DataFrame转换为List[Dict]格式
        result = df.to_dict(orient='records')
        return result
    except Exception as e:
        raise Exception(f"获取财新网财经新闻失败: {str(e)}")

def test() -> List[Dict[str, Any]]:
    """
    同步测试方法，用于自动化测试
    
    Returns:
        List[Dict[str, Any]]: 返回财经新闻数据列表
        
    Raises:
        Exception: 当execute方法执行失败时抛出异常
    """
    return asyncio.run(execute())

if __name__ == '__main__':
    # 演示如何调用异步函数
    async def main():
        try:
            data = await execute()
            print(data[:2])  # 打印前两条数据示例
        except Exception as e:
            print(f"Error: {e}")
    
    asyncio.run(main())