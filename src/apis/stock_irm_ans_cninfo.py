import asyncio
from typing import List, Dict, Any
import akshare as ak
import pandas as pd

async def execute(symbol: str) -> List[Dict[str, Any]]:
    """
    异步获取互动易-回答数据
    
    Args:
        symbol: 通过 ak.stock_irm_cninfo 获取的提问者编号
        
    Returns:
        互动易回答数据列表，每个回答以字典形式返回
        
    Raises:
        Exception: 当接口调用或数据处理出错时抛出异常
    """
    try:
        # 调用akshare接口获取数据
        df = ak.stock_irm_ans_cninfo(symbol=symbol)
        
        # 将DataFrame转换为List[Dict]格式
        if not df.empty:
            # 处理datetime类型字段
            df['提问时间'] = pd.to_datetime(df['提问时间']).dt.strftime('%Y-%m-%d %H:%M:%S')
            df['回答时间'] = pd.to_datetime(df['回答时间']).dt.strftime('%Y-%m-%d %H:%M:%S')
            return df.to_dict('records')
        return []
    except Exception as e:
        raise Exception(f"获取互动易回答数据失败: {str(e)}")

def test():
    """
    同步测试方法，用于自动化测试
    
    Returns:
        互动易回答数据列表
        
    Raises:
        异常上抛不捕获
    """
    # 使用示例中的symbol参数
    symbol = "1495108801386602496"
    return asyncio.run(execute(symbol=symbol))

if __name__ == '__main__':
    # 演示如何调用异步函数
    async def main():
        try:
            symbol = "1495108801386602496"
            data = await execute(symbol=symbol)
            print(f"获取到{len(data)}条互动易回答数据:")
            for item in data[:2]:  # 打印前两条数据
                print(item)
        except Exception as e:
            print(f"调用出错: {e}")
    
    asyncio.run(main())