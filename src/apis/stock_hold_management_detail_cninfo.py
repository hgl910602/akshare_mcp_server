import asyncio
from typing import List, Dict, Any
import akshare as ak
import pandas as pd

async def execute(symbol: str = "增持") -> List[Dict[str, Any]]:
    """
    获取巨潮资讯-数据中心-专题统计-股东股本-高管持股变动明细
    
    Args:
        symbol: 持股变动类型，"增持" 或 "减持"
    
    Returns:
        List[Dict[str, Any]]: 高管持股变动明细数据
    
    Raises:
        ValueError: 当输入参数不符合要求时
        Exception: 当数据获取失败时
    """
    if symbol not in {"增持", "减持"}:
        raise ValueError("symbol 参数必须是 '增持' 或 '减持'")
    
    try:
        # 调用akshare接口获取数据
        df = ak.stock_hold_management_detail_cninfo(symbol=symbol)
        
        # 将DataFrame转换为List[Dict]格式
        if not df.empty:
            # 处理可能的NaN值
            df = df.where(pd.notnull(df), None)
            return df.to_dict("records")
        return []
    except Exception as e:
        raise Exception(f"获取高管持股变动明细数据失败: {str(e)}")

def test():
    """
    同步测试方法，用于自动化测试
    
    Returns:
        List[Dict[str, Any]]: 高管持股变动明细数据
    
    Raises:
        Exception: 当数据获取失败时
    """
    try:
        # 使用示例参数调用execute方法
        result = asyncio.run(execute(symbol="增持"))
        return result
    except Exception as e:
        raise e

if __name__ == "__main__":
    # 演示如何调用异步函数并打印结果
    async def main():
        try:
            data = await execute(symbol="增持")
            print(data[:2])  # 打印前两条数据作为示例
        except Exception as e:
            print(f"发生错误: {e}")
    
    asyncio.run(main())