import asyncio
from typing import List, Dict, Any
import akshare as ak
import pandas as pd

async def execute(symbol: str = "基金持仓", date: str = "20200630") -> List[Dict[str, Any]]:
    """
    异步获取东方财富网-数据中心-主力数据-基金持仓数据
    
    Args:
        symbol: 持仓类型, choice of {"基金持仓", "QFII持仓", "社保持仓", "券商持仓", "保险持仓", "信托持仓"}
        date: 财报发布日期, 格式为xxxx0331, xxxx0630, xxxx0930, xxxx1231
    
    Returns:
        基金持仓数据列表，每个元素为一个字典
        
    Raises:
        Exception: 当akshare接口调用失败时抛出异常
    """
    try:
        # 调用akshare接口获取数据
        df = ak.stock_report_fund_hold(symbol=symbol, date=date)
        
        # 将DataFrame转换为List[Dict]格式
        if not df.empty:
            # 处理可能的NaN值
            df = df.fillna(0)
            # 转换数据类型
            df = df.astype({
                "序号": int,
                "股票代码": str,
                "股票简称": str,
                "持有基金家数": int,
                "持股总数": int,
                "持股市值": float,
                "持股变化": str,
                "持股变动数值": int,
                "持股变动比例": float
            })
            return df.to_dict("records")
        return []
    except Exception as e:
        raise Exception(f"获取基金持仓数据失败: {str(e)}")

def test():
    """
    同步测试方法，用于自动化测试
    
    Returns:
        基金持仓数据列表
        
    Raises:
        原样抛出execute方法中的异常
    """
    try:
        return asyncio.run(execute(symbol="基金持仓", date="20200630"))
    except Exception as e:
        raise e

if __name__ == "__main__":
    # 演示如何调用异步函数
    async def main():
        try:
            data = await execute(symbol="基金持仓", date="20200630")
            print(f"获取到{len(data)}条基金持仓数据")
            if data:
                print("第一条数据示例:")
                print(data[0])
        except Exception as e:
            print(f"发生错误: {e}")
    
    asyncio.run(main())