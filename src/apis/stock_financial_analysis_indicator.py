import asyncio
from typing import List, Dict, Any
import akshare as ak

async def execute(symbol: str, start_year: str) -> List[Dict[str, Any]]:
    """
    异步获取股票财务指标数据
    
    Args:
        symbol: 股票代码
        start_year: 开始年份
        
    Returns:
        财务指标数据列表，每个元素为一个时间点的指标数据字典
        
    Raises:
        Exception: 当akshare接口调用失败时抛出异常
    """
    try:
        # 调用akshare同步接口，使用await确保在异步环境中运行
        df = await asyncio.get_event_loop().run_in_executor(
            None,
            ak.stock_financial_analysis_indicator,
            symbol,
            start_year
        )
        
        # 将DataFrame转换为List[Dict]格式
        result = df.to_dict(orient='records')
        return result
    except Exception as e:
        raise Exception(f"获取股票财务指标数据失败: {e}")

def test():
    """
    同步测试方法，用于自动化测试
    
    Returns:
        测试结果数据
        
    Raises:
        原样抛出execute方法中的异常
    """
    # 使用示例参数调用execute方法
    return asyncio.run(execute(symbol="600004", start_year="2020"))

if __name__ == '__main__':
    # 演示如何调用异步函数
    async def main():
        try:
            data = await execute(symbol="600004", start_year="2020")
            print(data[:2])  # 打印前两条数据示例
        except Exception as e:
            print(f"Error: {e}")
    
    asyncio.run(main())