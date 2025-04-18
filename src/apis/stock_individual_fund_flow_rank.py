import asyncio
from typing import List, Dict, Any
import akshare as ak
import pandas as pd

async def execute(indicator: str = "今日") -> List[Dict[str, Any]]:
    """
    东方财富网-数据中心-资金流向-排名
    
    Parameters
    ----------
    indicator : str, optional
        indicator="今日"; choice {"今日", "3日", "5日", "10日"}, by default "今日"
    
    Returns
    -------
    List[Dict[str, Any]]
        资金流向排名数据
        
    Raises
    ------
    ValueError
        当indicator参数不合法时抛出
    Exception
        当接口调用失败时抛出
    """
    valid_indicators = {"今日", "3日", "5日", "10日"}
    if indicator not in valid_indicators:
        raise ValueError(f"indicator参数必须为{valid_indicators}中的一个")
    
    try:
        df = ak.stock_individual_fund_flow_rank(indicator=indicator)
        if not isinstance(df, pd.DataFrame) or df.empty:
            return []
        return df.to_dict("records")
    except Exception as e:
        raise Exception(f"获取资金流向排名数据失败: {e}")

def test():
    """
    同步测试方法
    """
    try:
        result = asyncio.run(execute(indicator="10日"))
        print(f"获取到{len(result)}条数据")
        return result
    except Exception as e:
        print(f"测试失败: {e}")
        raise

if __name__ == "__main__":
    # 演示如何调用异步函数
    async def main():
        try:
            data = await execute(indicator="5日")
            print(f"获取到{len(data)}条数据")
            if data:
                print("第一条数据:", data[0])
        except Exception as e:
            print(f"调用失败: {e}")
    
    asyncio.run(main())