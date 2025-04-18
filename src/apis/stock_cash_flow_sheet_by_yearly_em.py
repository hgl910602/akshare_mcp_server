import asyncio
from typing import List, Dict, Any
import akshare as ak

async def execute(symbol: str) -> List[Dict[str, Any]]:
    """
    异步获取东方财富股票年度现金流量表数据
    
    Args:
        symbol: 股票代码，例如 "SH600519"
        
    Returns:
        返回包含现金流量表数据的字典列表
        
    Raises:
        Exception: 当数据获取失败时抛出异常
    """
    try:
        # 调用akshare的同步接口，使用await包装
        loop = asyncio.get_running_loop()
        df = await loop.run_in_executor(
            None, 
            ak.stock_cash_flow_sheet_by_yearly_em, 
            symbol
        )
        # 将DataFrame转换为List[Dict]格式
        return df.to_dict("records")
    except Exception as e:
        raise Exception(f"获取股票年度现金流量表数据失败: {str(e)}")

def test():
    """
    同步测试方法，用于自动化测试
    
    Raises:
        直接抛出执行过程中出现的任何异常
    """
    # 使用示例参数调用
    result = asyncio.run(execute(symbol="SH600519"))
    return result

if __name__ == "__main__":
    # 演示如何调用异步函数
    async def main():
        try:
            data = await execute(symbol="SH600519"))
            print(data[:2])  # 打印前两条数据作为示例
        except Exception as e:
            print(f"Error: {e}")
    
    asyncio.run(main())