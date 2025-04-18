import asyncio
from typing import List, Dict, Any
import akshare as ak

async def execute() -> List[Dict[str, Any]]:
    """
    异步获取乐咕乐股网-赚钱效应分析数据
    
    Returns:
        List[Dict[str, Any]]: 返回处理后的数据列表，每个元素为字典形式
    """
    try:
        # 调用akshare的同步接口，使用run_in_executor避免阻塞事件循环
        loop = asyncio.get_running_loop()
        df = await loop.run_in_executor(None, ak.stock_market_activity_legu)
        
        # 将DataFrame转换为List[Dict]格式
        result = df.to_dict(orient="records")
        return result
    except Exception as e:
        raise Exception(f"获取乐咕乐股网数据失败: {e}")

def test() -> List[Dict[str, Any]]:
    """
    同步测试方法，用于自动化测试
    
    Returns:
        List[Dict[str, Any]]: 返回处理后的数据列表
        
    Raises:
        Exception: 当execute方法执行失败时抛出异常
    """
    try:
        return asyncio.run(execute())
    except Exception as e:
        raise Exception(f"测试执行失败: {e}")

if __name__ == "__main__":
    # 演示异步调用
    async def main():
        try:
            data = await execute()
            print(data)
        except Exception as e:
            print(f"Error: {e}")
    
    asyncio.run(main())