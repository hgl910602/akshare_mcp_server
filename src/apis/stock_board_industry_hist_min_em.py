import asyncio
from typing import List, Dict, Any
import akshare as ak
import pandas as pd

async def execute(symbol: str, period: str) -> List[Dict[str, Any]]:
    """
    异步获取东方财富-沪深板块-行业板块-分时历史行情数据
    
    Args:
        symbol: 行业板块名称，如"小金属"
        period: 分时周期，可选 {"1", "5", "15", "30", "60"}
    
    Returns:
        返回处理后的行情数据列表，每个元素为一个字典
        
    Raises:
        Exception: 当akshare接口调用失败或数据处理出错时抛出异常
    """
    try:
        # 调用akshare接口获取数据
        df = ak.stock_board_industry_hist_min_em(symbol=symbol, period=period)
        
        # 处理数据为List[Dict]格式
        if not df.empty:
            # 转换列名
            df.columns = [
                "日期时间", "开盘", "收盘", "最高", "最低", 
                "涨跌幅", "涨跌额", "成交量", "成交额", 
                "振幅", "换手率"
            ]
            # 转换数据类型
            df["日期时间"] = df["日期时间"].astype(str)
            return df.to_dict("records")
        return []
    except Exception as e:
        raise Exception(f"获取行业板块分时数据失败: {e}")

def test():
    """
    同步测试方法，用于自动化测试
    
    Raises:
        原样抛出execute方法中的异常
    """
    try:
        # 使用示例参数调用
        result = asyncio.run(execute(symbol="小金属", period="5"))
        print(f"测试成功，获取到{len(result)}条数据")
        return result
    except Exception as e:
        print(f"测试失败: {e}")
        raise

if __name__ == "__main__":
    # 演示如何调用异步函数
    async def main():
        try:
            data = await execute(symbol="小金属", period="5")
            print(f"获取到{len(data)}条数据")
            if data:
                print("第一条数据示例:")
                print(data[0])
        except Exception as e:
            print(f"调用失败: {e}")
    
    asyncio.run(main())