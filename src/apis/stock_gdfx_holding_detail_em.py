import asyncio
from typing import List, Dict, Any
import akshare as ak
import pandas as pd

async def execute(date: str, indicator: str, symbol: str) -> List[Dict[str, Any]]:
    """
    异步获取东方财富网-股东持股明细-十大股东数据
    
    Args:
        date: 财报发布季度最后日，格式如"20230331"
        indicator: 股东类型，可选值: {"个人", "基金", "QFII", "社保", "券商", "信托"}
        symbol: 持股变动，可选值: {"新进", "增加", "不变", "减少"}
    
    Returns:
        返回处理后的股东持股明细数据列表
        
    Raises:
        Exception: 当akshare接口调用失败或数据处理出错时抛出
    """
    try:
        # 调用akshare接口获取数据
        df = ak.stock_gdfx_holding_detail_em(date=date, indicator=indicator, symbol=symbol)
        
        # 处理数据为List[Dict]格式
        if not df.empty:
            # 转换NaN为None
            df = df.where(pd.notnull(df), None)
            # 转换datetime列
            for col in df.columns:
                if df[col].dtype == 'datetime64[ns]':
                    df[col] = df[col].astype(str)
            return df.to_dict('records')
        return []
    except Exception as e:
        raise Exception(f"获取股东持股明细数据失败: {str(e)}")

def test():
    """
    同步测试方法，用于自动化测试
    
    Raises:
        原样抛出execute方法中的异常
    """
    try:
        result = asyncio.run(execute(date="20230331", indicator="个人", symbol="新进"))
        print(f"测试成功，获取到{len(result)}条数据")
        return result
    except Exception as e:
        print(f"测试失败: {str(e)}")
        raise

if __name__ == '__main__':
    # 演示如何调用异步函数
    async def main():
        try:
            data = await execute(date="20230331", indicator="个人", symbol="新进")
            print(f"获取到{len(data)}条数据:")
            for item in data[:2]:  # 打印前两条数据
                print(item)
        except Exception as e:
            print(f"调用失败: {str(e)}")
    
    asyncio.run(main())