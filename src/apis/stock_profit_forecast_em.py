import asyncio
from typing import List, Dict, Any
import akshare as ak

async def execute(symbol: str = "") -> List[Dict[str, Any]]:
    """
    东方财富网-数据中心-研究报告-盈利预测
    
    Args:
        symbol: 行业板块名称，默认为获取全部数据
        
    Returns:
        List[Dict[str, Any]]: 盈利预测数据列表
        
    Raises:
        Exception: 当获取数据失败时抛出异常
    """
    try:
        # 调用akshare接口获取数据
        df = ak.stock_profit_forecast_em(symbol=symbol)
        
        # 将DataFrame转换为List[Dict]格式
        result = df.to_dict(orient="records")
        
        return result
    except Exception as e:
        raise Exception(f"获取盈利预测数据失败: {str(e)}")

def test():
    """
    同步测试方法，用于自动化测试
    
    Raises:
        Exception: 当execute方法执行失败时抛出异常
    """
    try:
        # 模拟调用示例中的参数
        result = asyncio.run(execute(symbol=""))
        print(result)
    except Exception as e:
        raise Exception(f"测试执行失败: {str(e)}")

if __name__ == "__main__":
    # 演示如何调用异步函数并打印结果
    async def main():
        try:
            # 获取全部数据
            data = await execute()
            print(data)
            
            # 获取特定行业数据
            # data = await execute(symbol="船舶制造")
            # print(data)
        except Exception as e:
            print(f"Error: {str(e)}")
    
    asyncio.run(main())