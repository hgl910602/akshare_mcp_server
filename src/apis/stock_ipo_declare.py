import asyncio
from typing import List, Dict, Any
import akshare as ak

async def execute() -> List[Dict[str, Any]]:
    """
    异步获取首发申报企业信息
    
    Returns:
        List[Dict[str, Any]]: 首发申报企业信息列表，每个企业信息以字典形式存储
    """
    try:
        # 调用akshare接口获取数据
        df = ak.stock_ipo_declare()
        # 将DataFrame转换为List[Dict]格式
        result = df.to_dict(orient='records')
        return result
    except Exception as e:
        raise Exception(f"获取首发申报企业信息失败: {e}")

def test() -> List[Dict[str, Any]]:
    """
    同步测试方法，用于自动化测试
    
    Returns:
        List[Dict[str, Any]]: 首发申报企业信息列表
        
    Raises:
        Exception: 当execute方法执行失败时抛出异常
    """
    try:
        return asyncio.run(execute())
    except Exception as e:
        raise Exception(f"测试执行失败: {e}")

if __name__ == '__main__':
    # 演示如何调用异步函数
    async def main():
        try:
            data = await execute()
            print(data[:2])  # 打印前两条数据作为示例
        except Exception as e:
            print(f"Error: {e}")
    
    asyncio.run(main())