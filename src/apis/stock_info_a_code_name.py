import asyncio
from typing import List, Dict, Any
import akshare as ak

async def execute() -> List[Dict[str, Any]]:
    """
    异步获取沪深京A股股票代码和股票简称数据
    
    Returns:
        List[Dict[str, Any]]: 包含股票代码和名称的字典列表
        
    Raises:
        Exception: 当数据获取失败时抛出异常
    """
    try:
        # 调用akshare同步接口获取数据
        df = ak.stock_info_a_code_name()
        # 将DataFrame转换为字典列表
        result = df.to_dict(orient='records')
        return result
    except Exception as e:
        raise Exception(f"Failed to fetch stock info: {str(e)}")

def test() -> List[Dict[str, Any]]:
    """
    同步测试方法，用于自动化测试
    
    Returns:
        List[Dict[str, Any]]: 包含股票代码和名称的字典列表
        
    Raises:
        Exception: 当数据获取失败时抛出异常
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
            print(f"获取到 {len(data)} 条股票数据")
            print("前5条数据示例:")
            for item in data[:5]:
                print(item)
        except Exception as e:
            print(f"发生错误: {e}")
    
    asyncio.run(main())