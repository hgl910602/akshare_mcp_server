import asyncio
from typing import List, Dict, Any
import akshare as ak

async def execute(symbol: str, period: str = '1', adjust: str = "") -> List[Dict[str, Any]]:
    """
    异步获取新浪财经B股股票或指数的分时数据
    
    Args:
        symbol: 股票代码，例如'sh900901'
        period: 数据频率，可选'1', '5', '15', '30', '60'分钟
        adjust: 复权类型，''(不复权), 'qfq'(前复权), 'hfq'(后复权)
    
    Returns:
        包含分时数据的字典列表
        
    Raises:
        Exception: 当akshare接口调用失败时抛出
    """
    try:
        # 调用akshare接口获取数据
        df = ak.stock_zh_b_minute(symbol=symbol, period=period, adjust=adjust)
        # 将DataFrame转换为字典列表
        return df.to_dict('records')
    except Exception as e:
        raise Exception(f"Failed to fetch B stock minute data: {str(e)}")

def test():
    """
    同步测试方法，用于自动化测试
    
    Raises:
        Exception: 当execute方法调用失败时抛出
    """
    try:
        # 使用示例参数调用execute方法
        result = asyncio.run(execute(symbol='sh900901', period='1', adjust="qfq"))
        print("Test executed successfully")
        return result
    except Exception as e:
        raise Exception(f"Test failed: {str(e)}")

if __name__ == '__main__':
    # 演示如何调用异步函数
    async def main():
        try:
            data = await execute(symbol='sh900901', period='5', adjust='')
            print(data[:5])  # 打印前5条数据
        except Exception as e:
            print(f"Error occurred: {e}")
    
    asyncio.run(main())