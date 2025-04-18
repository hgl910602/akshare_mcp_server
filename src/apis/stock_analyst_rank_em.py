import asyncio
from typing import List, Dict, Any
import akshare as ak

async def execute(year: str = '2024') -> List[Dict[str, Any]]:
    """
    异步获取东方财富分析师指数排行数据
    
    Args:
        year: 年份，从2013年至今
        
    Returns:
        返回分析师排行数据的字典列表
        
    Raises:
        Exception: 当获取数据失败时抛出异常
    """
    try:
        # 调用akshare接口获取数据
        df = ak.stock_analyst_rank_em(year=year)
        # 将DataFrame转换为字典列表
        return df.to_dict('records')
    except Exception as e:
        raise Exception(f"获取分析师排行数据失败: {str(e)}")

def test():
    """
    同步测试方法，用于自动化测试
    
    Raises:
        直接抛出execute方法中的异常
    """
    try:
        result = asyncio.run(execute(year='2024'))
        print("测试成功，获取数据条数:", len(result))
        return result
    except Exception as e:
        print("测试失败:", str(e))
        raise

if __name__ == '__main__':
    # 演示如何调用异步函数
    async def main():
        try:
            data = await execute(year='2024')
            print("获取数据成功，样例数据:")
            print(data[0] if data else "无数据")
        except Exception as e:
            print("调用失败:", str(e))
    
    asyncio.run(main())