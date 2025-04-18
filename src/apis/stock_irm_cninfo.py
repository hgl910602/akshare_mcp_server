import asyncio
from typing import List, Dict, Any
import akshare as ak
import pandas as pd

async def execute(symbol: str) -> List[Dict[str, Any]]:
    """
    异步获取互动易-提问数据
    
    Args:
        symbol: 股票代码，例如 "002594"
        
    Returns:
        返回互动易提问数据的字典列表
        
    Raises:
        Exception: 当获取数据失败时抛出异常
    """
    try:
        # 调用akshare接口获取数据
        df = ak.stock_irm_cninfo(symbol=symbol)
        
        # 将DataFrame转换为字典列表
        if not df.empty:
            # 处理datetime类型字段
            datetime_cols = ['提问时间', '更新时间']
            for col in datetime_cols:
                if col in df.columns:
                    df[col] = df[col].astype(str)
            
            return df.to_dict('records')
        return []
    except Exception as e:
        raise Exception(f"获取互动易数据失败: {str(e)}")

def test():
    """
    同步测试方法，用于自动化测试
    
    Returns:
        返回execute方法的执行结果
        
    Raises:
        异常上抛，不捕获
    """
    # 使用示例中的参数
    symbol = "002594"
    return asyncio.run(execute(symbol=symbol))

if __name__ == '__main__':
    # 演示如何调用异步函数
    async def main():
        try:
            data = await execute(symbol="002594")
            print(f"获取到{len(data)}条数据")
            if data:
                print("第一条数据示例:")
                print(data[0])
        except Exception as e:
            print(f"发生错误: {e}")
    
    asyncio.run(main())