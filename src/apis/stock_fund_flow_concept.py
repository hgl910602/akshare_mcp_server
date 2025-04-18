import asyncio
from typing import List, Dict, Any
import akshare as ak
import pandas as pd

async def execute(symbol: str = "即时") -> List[Dict[str, Any]]:
    """
    同花顺-数据中心-资金流向-概念资金流
    
    Args:
        symbol: choice of {"即时", "3日排行", "5日排行", "10日排行", "20日排行"}
    
    Returns:
        List[Dict[str, Any]]: 返回概念资金流数据
        
    Raises:
        Exception: 当获取数据失败时抛出异常
    """
    try:
        # 调用akshare接口获取数据
        df = ak.stock_fund_flow_concept(symbol=symbol)
        
        # 将DataFrame转换为List[Dict]格式
        result = []
        if not df.empty:
            # 处理可能的NaN值
            df = df.fillna(0)
            # 转换数据类型
            df = df.astype({
                "序号": "int32",
                "行业": "str",
                "公司家数": "int64",
                "行业指数": "float64",
                "阶段涨跌幅": "str",
                "流入资金": "float64",
                "流出资金": "float64",
                "净额": "float64"
            })
            result = df.to_dict("records")
        return result
    except Exception as e:
        raise Exception(f"获取概念资金流数据失败: {str(e)}")

def test():
    """
    同步测试方法，用于自动化测试
    
    Returns:
        List[Dict[str, Any]]: 返回概念资金流数据
        
    Raises:
        Exception: 当获取数据失败时抛出异常
    """
    try:
        # 使用示例参数调用execute方法
        return asyncio.run(execute(symbol="3日排行"))
    except Exception as e:
        raise e

if __name__ == "__main__":
    # 演示如何调用异步函数并打印结果
    async def main():
        try:
            data = await execute(symbol="5日排行"))
            print(data)
        except Exception as e:
            print(f"Error: {e}")
    
    asyncio.run(main())