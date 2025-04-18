import asyncio
from typing import List, Dict, Any
import akshare as ak

async def execute(symbol: str, indicator: str) -> List[Dict[str, Any]]:
    """
    异步获取同花顺盈利预测数据
    
    Args:
        symbol: 股票代码
        indicator: 预测指标类型
        
    Returns:
        返回处理后的盈利预测数据列表
        
    Raises:
        Exception: 当akshare接口调用失败时抛出异常
    """
    try:
        # 调用akshare接口获取数据
        df = ak.stock_profit_forecast_ths(symbol=symbol, indicator=indicator)
        
        # 将DataFrame转换为List[Dict]格式
        result = df.to_dict(orient='records')
        return result
    except Exception as e:
        raise Exception(f"Failed to fetch stock profit forecast: {str(e)}")

def test():
    """
    同步测试方法，用于自动化测试
    
    Raises:
        原样抛出execute方法中的异常
    """
    symbol = "600519"
    indicator = "业绩预测详表-详细指标预测"
    try:
        result = asyncio.run(execute(symbol=symbol, indicator=indicator))
        print(result)
        return result
    except Exception as e:
        print(f"Test failed: {str(e)}")
        raise

if __name__ == '__main__':
    # 演示如何调用异步函数
    async def main():
        symbol = "600519"
        indicator = "业绩预测详表-详细指标预测"
        try:
            result = await execute(symbol=symbol, indicator=indicator)
            print("获取盈利预测数据成功:")
            for item in result:
                print(item)
        except Exception as e:
            print(f"获取数据失败: {str(e)}")
    
    asyncio.run(main())