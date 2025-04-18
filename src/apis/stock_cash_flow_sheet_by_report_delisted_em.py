import asyncio
from typing import List, Dict, Any
import akshare as ak

async def execute(symbol: str) -> List[Dict[str, Any]]:
    """
    获取东方财富-已退市股票现金流量表数据(按报告期)
    
    Args:
        symbol: 带市场标识的已退市股票代码, 如 "SZ000013"
        
    Returns:
        现金流量表数据列表, 每个元素为一个报告期的数据字典
        
    Raises:
        Exception: 当接口调用失败时抛出
    """
    try:
        # 调用akshare同步接口, 在异步函数中使用默认线程池执行
        loop = asyncio.get_running_loop()
        df = await loop.run_in_executor(
            None, 
            ak.stock_cash_flow_sheet_by_report_delisted_em,
            symbol
        )
        # 将DataFrame转换为List[Dict]格式
        return df.to_dict("records")
    except Exception as e:
        raise Exception(f"获取已退市股票现金流量表数据失败: {e}")

def test():
    """
    同步测试方法, 用于自动化测试
    
    Raises:
        Exception: 当execute调用失败时抛出
    """
    try:
        # 使用示例参数调用execute方法
        result = asyncio.run(execute(symbol="SZ000013"))
        return result
    except Exception as e:
        raise Exception(f"测试失败: {e}")

if __name__ == "__main__":
    # 演示如何调用异步函数并打印结果
    async def main():
        try:
            data = await execute(symbol="SZ000013")
            print(data[:2])  # 打印前两条记录
        except Exception as e:
            print(f"Error: {e}")
    
    asyncio.run(main())