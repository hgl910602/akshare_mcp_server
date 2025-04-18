import asyncio
from typing import List, Dict, Any
import akshare as ak

async def execute() -> List[Dict[str, Any]]:
    """
    异步获取新浪财经-发行与分配-历史分红数据
    
    Returns:
        List[Dict[str, Any]]: 历史分红数据列表，每个元素为一个字典代表一条记录
        
    Raises:
        Exception: 当获取数据失败时抛出异常
    """
    try:
        # 调用akshare同步接口获取数据
        df = ak.stock_history_dividend()
        
        # 将DataFrame转换为List[Dict]格式
        result = df.to_dict(orient='records')
        return result
    except Exception as e:
        raise Exception(f"获取历史分红数据失败: {str(e)}")

def test() -> List[Dict[str, Any]]:
    """
    同步测试函数，用于自动化测试
    
    Returns:
        List[Dict[str, Any]]: 历史分红数据列表
        
    Raises:
        原样抛出execute方法中的异常
    """
    return asyncio.run(execute())

if __name__ == '__main__':
    # 演示如何调用异步函数并打印结果
    async def main():
        try:
            data = await execute()
            print("获取历史分红数据成功:")
            for item in data[:3]:  # 打印前3条记录作为示例
                print(item)
        except Exception as e:
            print(f"获取数据时出错: {e}")
    
    asyncio.run(main())