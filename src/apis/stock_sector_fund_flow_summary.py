import asyncio
from typing import List, Dict, Any
import akshare as ak

async def execute(symbol: str, indicator: str = "今日") -> List[Dict[str, Any]]:
    """
    异步获取东方财富网-数据中心-资金流向-行业资金流-xx行业个股资金流数据
    
    Args:
        symbol: 行业名称，如"电源设备"
        indicator: 时间周期，可选 "今日", "5日", "10日"
    
    Returns:
        返回行业个股资金流数据列表，每个元素是一个字典
    
    Raises:
        Exception: 当akshare接口调用失败时抛出异常
    """
    try:
        # 调用akshare同步接口，使用await在异步环境中运行
        df = await asyncio.get_event_loop().run_in_executor(
            None,
            ak.stock_sector_fund_flow_summary,
            symbol,
            indicator
        )
        # 将DataFrame转换为List[Dict]格式
        return df.to_dict("records")
    except Exception as e:
        raise Exception(f"获取行业资金流数据失败: {str(e)}")

def test():
    """
    同步测试方法，用于自动化测试
    
    Raises:
        当execute方法调用失败时直接抛出异常
    """
    # 使用示例参数调用异步execute方法
    result = asyncio.run(execute(symbol="电源设备", indicator="今日"))
    print(result)

if __name__ == "__main__":
    # 演示如何调用异步函数并打印结果
    async def main():
        try:
            data = await execute(symbol="电源设备", indicator="今日")
            print(data)
        except Exception as e:
            print(f"Error: {e}")
    
    asyncio.run(main())