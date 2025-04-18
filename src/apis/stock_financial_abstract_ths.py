import asyncio
from typing import Any, Dict, List, Optional
import akshare as ak

async def execute(symbol: str, indicator: str = "按报告期") -> List[Dict[str, Any]]:
    """
    异步获取同花顺-财务指标-主要指标数据
    
    Args:
        symbol: 股票代码
        indicator: 报告期类型，可选 {"按报告期", "按年度", "按单季度"}
        
    Returns:
        财务指标数据列表，每个元素为字典形式的指标数据
        
    Raises:
        Exception: 当接口调用失败时抛出异常
    """
    try:
        # 调用akshare同步接口，使用await包装
        loop = asyncio.get_running_loop()
        df = await loop.run_in_executor(
            None, 
            ak.stock_financial_abstract_ths, 
            symbol, 
            indicator
        )
        # 将DataFrame转换为List[Dict]格式
        return df.to_dict("records")
    except Exception as e:
        raise Exception(f"获取财务指标数据失败: {e}")

def test():
    """
    同步测试方法，用于自动化测试
    
    Raises:
        Exception: 当execute调用失败时抛出异常
    """
    try:
        # 使用示例参数调用异步execute方法
        result = asyncio.run(execute(symbol="000063", indicator="按报告期"))
        print(result)
        return result
    except Exception as e:
        raise Exception(f"测试失败: {e}")

if __name__ == "__main__":
    # 演示如何调用异步函数
    async def main():
        try:
            data = await execute(symbol="000063", indicator="按报告期")
            print(data)
        except Exception as e:
            print(f"Error: {e}")
    
    asyncio.run(main())