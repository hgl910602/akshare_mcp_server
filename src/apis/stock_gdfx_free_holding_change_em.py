import asyncio
from typing import List, Dict, Any
import akshare as ak

async def execute(date: str) -> List[Dict[str, Any]]:
    """
    东方财富网-数据中心-股东分析-股东持股变动统计-十大流通股东
    
    Parameters
    ----------
    date : str
        财报发布季度最后日, 例如: "20210930"
    
    Returns
    -------
    List[Dict[str, Any]]
        十大流通股东持股变动数据
    
    Raises
    ------
    Exception
        当获取数据失败时抛出异常
    """
    try:
        df = ak.stock_gdfx_free_holding_change_em(date=date)
        return df.to_dict(orient="records")
    except Exception as e:
        raise Exception(f"Failed to fetch stock_gdfx_free_holding_change_em data: {str(e)}")

def test():
    """
    同步测试方法，用于自动化测试
    
    Raises
    ------
    Exception
        当execute方法执行失败时抛出异常
    """
    try:
        result = asyncio.run(execute(date="20210930"))
        return result
    except Exception as e:
        raise Exception(f"Test failed: {str(e)}")

if __name__ == "__main__":
    # 演示如何调用异步函数并打印结果
    async def main():
        try:
            data = await execute(date="20210930")
            print(data)
        except Exception as e:
            print(f"Error occurred: {e}")
    
    asyncio.run(main())