import asyncio
from typing import List, Dict, Any
import akshare as ak
import pandas as pd

async def execute() -> List[Dict[str, Any]]:
    """
    异步获取乐咕乐股-A股等权重市盈率与中位数市盈率数据
    
    Returns:
        List[Dict[str, Any]]: 转换后的市盈率数据列表
        
    Raises:
        Exception: 当数据获取或处理失败时抛出异常
    """
    try:
        # 调用akshare接口获取数据
        df = ak.stock_a_ttm_lyr()
        
        # 将DataFrame转换为字典列表
        result = df.to_dict(orient='records')
        
        # 转换日期格式为字符串(如果存在)
        for item in result:
            if 'date' in item and pd.notna(item['date']):
                if isinstance(item['date'], pd.Timestamp):
                    item['date'] = item['date'].strftime('%Y-%m-%d')
                elif not isinstance(item['date'], str):
                    item['date'] = str(item['date'])
                    
        return result
    except Exception as e:
        raise Exception(f"Failed to fetch stock A TTM/LYR data: {str(e)}")

def test() -> List[Dict[str, Any]]:
    """
    同步测试方法，用于验证execute函数
    
    Returns:
        List[Dict[str, Any]]: 转换后的市盈率数据列表
        
    Raises:
        Exception: 当execute方法执行失败时抛出异常
    """
    return asyncio.run(execute())

if __name__ == '__main__':
    # 演示如何调用异步函数
    async def main():
        try:
            data = await execute()
            print("Successfully fetched data:")
            for item in data[:3]:  # 打印前3条数据作为示例
                print(item)
        except Exception as e:
            print(f"Error occurred: {e}")
    
    asyncio.run(main())