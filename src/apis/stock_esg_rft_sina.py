import asyncio
from typing import List, Dict, Any
import akshare as ak

async def execute() -> List[Dict[str, Any]]:
    """
    获取新浪财经-ESG评级中心-ESG评级-路孚特数据
    
    Returns:
        List[Dict[str, Any]]: 返回ESG评级数据的字典列表
        
    Raises:
        Exception: 当获取数据失败时抛出异常
    """
    try:
        # 调用akshare接口获取数据
        df = ak.stock_esg_rft_sina()
        
        # 将DataFrame转换为字典列表
        result = df.to_dict(orient='records')
        return result
    except Exception as e:
        raise Exception(f"Failed to fetch ESG data: {str(e)}")

def test() -> List[Dict[str, Any]]:
    """
    同步测试方法，用于自动化测试
    
    Returns:
        List[Dict[str, Any]]: 返回ESG评级数据的字典列表
        
    Raises:
        Exception: 当execute方法执行失败时抛出异常
    """
    try:
        return asyncio.run(execute())
    except Exception as e:
        raise Exception(f"Test failed: {str(e)}")

if __name__ == '__main__':
    # 演示如何调用异步函数
    async def main():
        try:
            data = await execute()
            print("Successfully fetched ESG data:")
            for item in data[:3]:  # 打印前3条记录
                print(item)
        except Exception as e:
            print(f"Error: {str(e)}")
    
    asyncio.run(main())