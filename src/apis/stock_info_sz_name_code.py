import asyncio
from typing import List, Dict, Any
import akshare as ak
import pandas as pd

async def execute(symbol: str = "A股列表") -> List[Dict[str, Any]]:
    """
    异步获取深证证券交易所股票代码和股票简称数据
    
    Args:
        symbol: 股票列表类型, 可选 {"A股列表", "B股列表", "CDR列表", "AB股列表"}
        
    Returns:
        List[Dict[str, Any]]: 转换后的股票数据列表
        
    Raises:
        ValueError: 当输入参数不合法时
        Exception: 当获取数据失败时
    """
    if symbol not in {"A股列表", "B股列表", "CDR列表", "AB股列表"}:
        raise ValueError("symbol参数必须是{'A股列表', 'B股列表', 'CDR列表', 'AB股列表'}中的一个")
    
    try:
        # 调用akshare同步接口
        df = ak.stock_info_sz_name_code(symbol=symbol)
        
        # 将DataFrame转换为List[Dict]格式
        result = df.to_dict(orient="records")
        
        # 处理可能的NaN值
        for item in result:
            for key in item:
                if pd.isna(item[key]):
                    item[key] = None
                    
        return result
    except Exception as e:
        raise Exception(f"获取深证股票列表数据失败: {str(e)}")

def test():
    """
    同步测试方法，用于自动化测试
    
    Returns:
        List[Dict[str, Any]]: 股票数据列表
        
    Raises:
        原样抛出execute方法可能抛出的异常
    """
    try:
        # 使用asyncio.run运行异步方法
        return asyncio.run(execute(symbol="A股列表"))
    except Exception as e:
        raise e

if __name__ == "__main__":
    # 演示如何调用异步函数
    async def main():
        try:
            data = await execute(symbol="A股列表")
            print(f"获取到{len(data)}条数据")
            if len(data) > 0:
                print("第一条数据:", data[0])
        except Exception as e:
            print(f"发生错误: {e}")
    
    asyncio.run(main())