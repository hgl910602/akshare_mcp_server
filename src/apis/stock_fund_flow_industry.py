import asyncio
from typing import List, Dict, Any
import akshare as ak
import pandas as pd

async def execute(symbol: str = "即时") -> List[Dict[str, Any]]:
    """
    同花顺-数据中心-资金流向-行业资金流
    
    Args:
        symbol: choice of {"即时", "3日排行", "5日排行", "10日排行", "20日排行"}
    
    Returns:
        List[Dict[str, Any]]: 行业资金流数据
        
    Raises:
        Exception: 当获取数据失败时抛出异常
    """
    try:
        # 调用akshare接口获取数据
        df = ak.stock_fund_flow_industry(symbol=symbol)
        
        # 将DataFrame转换为List[Dict]格式
        result = []
        if not df.empty:
            # 处理可能的NaN值
            df = df.fillna(0)
            # 转换数据类型
            for _, row in df.iterrows():
                item = {
                    "序号": int(row["序号"]),
                    "行业": str(row["行业"]),
                    "公司家数": int(row["公司家数"]),
                    "行业指数": float(row["行业指数"]),
                    "阶段涨跌幅": str(row["阶段涨跌幅"]),
                    "流入资金": float(row["流入资金"]),
                    "流出资金": float(row["流出资金"]),
                    "净额": float(row["净额"]),
                }
                result.append(item)
        return result
    except Exception as e:
        raise Exception(f"获取行业资金流数据失败: {str(e)}")

def test():
    """
    同步测试方法，用于自动化测试
    
    Raises:
        Exception: 当execute方法执行失败时抛出异常
    """
    try:
        # 使用asyncio.run运行异步方法
        result = asyncio.run(execute(symbol="3日排行"))
        print("测试成功，返回数据条数:", len(result))
        return result
    except Exception as e:
        raise Exception(f"测试失败: {str(e)}")

if __name__ == "__main__":
    # 演示如何调用异步函数
    async def main():
        try:
            # 调用示例
            data = await execute(symbol="5日排行")
            print("获取到的数据:")
            for item in data[:3]:  # 打印前3条数据
                print(item)
        except Exception as e:
            print(f"发生错误: {str(e)}")
    
    # 运行主函数
    asyncio.run(main())