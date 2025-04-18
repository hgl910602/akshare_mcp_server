import asyncio
from typing import List, Dict, Any
import akshare as ak
import pandas as pd

async def execute() -> List[Dict[str, Any]]:
    """
    异步获取两融账户信息数据
    
    Returns:
        List[Dict[str, Any]]: 转换后的两融账户信息列表
        
    Raises:
        Exception: 当数据获取或处理失败时抛出异常
    """
    try:
        # 调用akshare接口获取数据
        df = ak.stock_margin_account_info()
        
        # 将DataFrame转换为List[Dict]格式
        result = []
        if not df.empty:
            # 处理可能的NaN值
            df = df.fillna(0)
            # 转换日期格式为字符串
            df['日期'] = df['日期'].astype(str)
            result = df.to_dict('records')
        return result
    except Exception as e:
        raise Exception(f"获取两融账户信息失败: {str(e)}")

def test() -> List[Dict[str, Any]]:
    """
    同步测试方法，用于自动化测试
    
    Returns:
        List[Dict[str, Any]]: 转换后的两融账户信息列表
        
    Raises:
        Exception: 当execute方法执行失败时抛出异常
    """
    try:
        return asyncio.run(execute())
    except Exception as e:
        raise Exception(f"测试执行失败: {str(e)}")

if __name__ == '__main__':
    # 演示如何调用异步函数
    async def main():
        try:
            data = await execute()
            print("获取两融账户信息成功:")
            for item in data:
                print(item)
        except Exception as e:
            print(f"发生错误: {e}")
    
    asyncio.run(main())