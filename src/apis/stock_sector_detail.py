import asyncio
from typing import List, Dict, Any
import akshare as ak

async def execute(sector: str = "hangye_ZL01") -> List[Dict[str, Any]]:
    """
    异步获取新浪行业-板块行情-成份详情数据
    
    Args:
        sector: 通过 ak.stock_sector_spot 返回数据的 label 字段选择 sector
        
    Returns:
        板块详情数据列表，每个元素为包含各字段的字典
        
    Raises:
        Exception: 当akshare接口调用失败时抛出
    """
    try:
        # 调用akshare同步接口，使用await在异步环境中运行
        df = await asyncio.get_event_loop().run_in_executor(
            None, 
            lambda: ak.stock_sector_detail(sector=sector)
        )
        # 将DataFrame转换为List[Dict]格式
        return df.to_dict("records")
    except Exception as e:
        raise Exception(f"Failed to fetch stock sector detail: {str(e)}")

def test():
    """
    同步测试方法，用于自动化测试
    
    Returns:
        板块详情数据列表
        
    Raises:
        原样抛出execute方法中的异常
    """
    try:
        # 使用asyncio.run运行异步方法
        result = asyncio.run(execute(sector="hangye_ZL01"))
        return result
    except Exception:
        # 异常上抛，不捕获
        raise

if __name__ == "__main__":
    # 演示如何调用异步函数
    async def main():
        try:
            data = await execute(sector="hangye_ZL01")
            print(data[:2])  # 打印前两条数据
        except Exception as e:
            print(f"Error occurred: {e}")
    
    asyncio.run(main())