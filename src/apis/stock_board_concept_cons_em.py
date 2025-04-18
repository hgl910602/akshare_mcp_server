import asyncio
from typing import List, Dict, Any
import akshare as ak
import pandas as pd

async def execute(symbol: str = "融资融券") -> List[Dict[str, Any]]:
    """
    异步获取东方财富-概念板块成份股数据
    
    Args:
        symbol: 板块名称或代码，例如 "融资融券" 或 "BK0655"
        
    Returns:
        返回板块成份股数据列表，每个股票信息以字典形式存储
        
    Raises:
        Exception: 当akshare接口调用失败时抛出异常
    """
    try:
        # 调用akshare同步接口，使用await在异步环境中执行
        df = await asyncio.get_event_loop().run_in_executor(
            None, 
            ak.stock_board_concept_cons_em, 
            symbol
        )
        
        # 将DataFrame转换为List[Dict]格式
        if not df.empty:
            # 处理可能的NaN值
            df = df.fillna(0)
            return df.to_dict("records")
        return []
    except Exception as e:
        raise Exception(f"获取概念板块成份股数据失败: {str(e)}")

def test():
    """
    同步测试方法，用于验证execute函数
    
    Raises:
        直接抛出execute方法可能产生的异常
    """
    try:
        # 使用示例参数调用异步execute方法
        result = asyncio.run(execute(symbol="融资融券"))
        print(f"测试成功，获取到{len(result)}条数据")
        return result
    except Exception as e:
        print(f"测试失败: {str(e)}")
        raise

if __name__ == "__main__":
    # 演示如何调用异步函数
    async def main():
        try:
            data = await execute(symbol="融资融券")
            print(f"获取到{len(data)}条数据:")
            for item in data[:3]:  # 打印前3条数据
                print(item)
        except Exception as e:
            print(f"调用失败: {str(e)}")
    
    asyncio.run(main())