import asyncio
from typing import List, Dict, Any
import akshare as ak

async def execute() -> List[Dict[str, Any]]:
    """
    异步获取新浪财经-ESG评级中心-ESG评级-秩鼎数据
    
    Returns:
        List[Dict[str, Any]]: 返回处理后的ESG评级数据列表
    """
    try:
        # 调用akshare接口获取数据
        df = ak.stock_esg_zd_sina()
        
        # 将DataFrame转换为List[Dict]格式
        result = df.to_dict(orient='records')
        return result
    except Exception as e:
        raise Exception(f"获取ESG评级数据失败: {e}")

def test() -> List[Dict[str, Any]]:
    """
    同步测试方法，用于自动化测试
    
    Returns:
        List[Dict[str, Any]]: 返回ESG评级数据
        
    Raises:
        Exception: 当execute方法执行出错时抛出异常
    """
    try:
        return asyncio.run(execute())
    except Exception as e:
        raise Exception(f"测试执行失败: {e}")

if __name__ == '__main__':
    # 演示异步调用
    async def main():
        try:
            data = await execute()
            print(data)
        except Exception as e:
            print(f"Error: {e}")
    
    asyncio.run(main())