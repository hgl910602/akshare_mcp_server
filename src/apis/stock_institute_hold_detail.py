import asyncio
from typing import List, Dict, Any
import akshare as ak

async def execute(stock: str, quarter: str) -> List[Dict[str, Any]]:
    """
    异步获取机构持股详情数据
    
    Args:
        stock: 股票代码
        quarter: 季度报告，格式如"20201"(2020年一季报)
    
    Returns:
        机构持股详情数据列表
    
    Raises:
        Exception: 当akshare接口调用失败时抛出
    """
    try:
        # 调用akshare同步接口，使用run_in_executor避免阻塞事件循环
        loop = asyncio.get_running_loop()
        df = await loop.run_in_executor(
            None, 
            ak.stock_institute_hold_detail, 
            stock=stock, 
            quarter=quarter
        )
        # 将DataFrame转换为List[Dict]格式
        return df.to_dict("records")
    except Exception as e:
        raise Exception(f"Failed to fetch stock institute hold details: {str(e)}")

def test():
    """
    同步测试方法，用于自动化测试
    
    Returns:
        机构持股详情数据列表
    
    Raises:
        原始异常: 当execute方法调用失败时抛出
    """
    # 使用示例参数调用异步execute方法
    return asyncio.run(execute(stock="300003", quarter="20201"))

if __name__ == "__main__":
    # 演示如何调用异步函数
    async def main():
        try:
            data = await execute(stock="300003", quarter="20201")
            print(data)
        except Exception as e:
            print(f"Error occurred: {e}")
    
    asyncio.run(main())