import asyncio
from typing import List, Dict, Any
import akshare as ak
import pandas as pd

async def execute() -> List[Dict[str, Any]]:
    """
    获取东方财富网-数据中心-大宗交易-市场统计数据
    
    Returns:
        List[Dict[str, Any]]: 大宗交易市场统计数据列表
    """
    try:
        # 调用akshare接口获取数据
        df = ak.stock_dzjy_sctj()
        
        # 将DataFrame转换为List[Dict]格式
        if not df.empty:
            # 处理可能的NaN值
            df = df.fillna(0)
            # 转换日期格式为字符串
            if '交易日期' in df.columns:
                df['交易日期'] = df['交易日期'].astype(str)
            return df.to_dict('records')
        return []
    except Exception as e:
        raise Exception(f"获取大宗交易市场统计数据失败: {e}")

def test() -> List[Dict[str, Any]]:
    """
    同步测试方法
    
    Returns:
        List[Dict[str, Any]]: 大宗交易市场统计数据列表
        
    Raises:
        Exception: 当execute方法执行失败时抛出
    """
    try:
        return asyncio.run(execute())
    except Exception as e:
        raise Exception(f"测试失败: {e}")

if __name__ == '__main__':
    # 异步调用示例
    async def main():
        try:
            data = await execute()
            print(data[:2])  # 打印前两条数据
        except Exception as e:
            print(f"Error: {e}")
    
    asyncio.run(main())