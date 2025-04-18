import asyncio
from typing import List, Dict, Any
import akshare as ak
import pandas as pd
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


async def execute(symbol: str, adjust: str = "") -> List[Dict[str, Any]]:
    """
    异步获取美股历史行情数据
    
    Args:
        symbol: 美股代码
        adjust: 复权类型, "qfq"表示前复权, 默认为空表示不复权
        
    Returns:
        返回包含历史行情数据的字典列表
        
    Raises:
        ValueError: 当symbol为空或无效时抛出
        Exception: 当获取数据失败时抛出
    """
    if not symbol:
        raise ValueError("股票代码不能为空")
    
    try:
        # 调用akshare接口获取数据
        df = ak.stock_us_daily(symbol=symbol, adjust=adjust)
        
        # 处理CIEN股票的特殊情况
        if symbol.upper() == "CIEN" and adjust == "qfq":
            logger.warning("CIEN股票的新浪美股数据由于复权因子错误，暂不返回前复权数据")
            df = ak.stock_us_daily(symbol=symbol, adjust="")
        
        # 将DataFrame转换为字典列表
        if not df.empty:
            # 确保date列是字符串类型
            df['date'] = df['date'].astype(str)
            return df.to_dict(orient='records')
        return []
    except Exception as e:
        logger.error(f"获取美股{symbol}历史数据失败: {str(e)}")
        raise


def test():
    """
    同步测试方法，用于验证execute函数
    
    Raises:
        直接抛出execute方法可能产生的异常
    """
    try:
        # 使用asyncio.run运行异步方法
        result = asyncio.run(execute(symbol="AAPL", adjust="qfq"))
        print(f"测试结果(前复权): {len(result)}条数据")
        
        # 测试不复权情况
        result = asyncio.run(execute(symbol="AAPL"))
        print(f"测试结果(不复权): {len(result)}条数据")
        
        # 测试CIEN特殊情况
        result = asyncio.run(execute(symbol="CIEN", adjust="qfq"))
        print(f"测试结果(CIEN): {len(result)}条数据")
    except Exception as e:
        print(f"测试失败: {str(e)}")
        raise


if __name__ == '__main__':
    # 演示如何调用异步函数
    async def main():
        try:
            # 获取AAPL前复权数据
            aapl_qfq = await execute(symbol="AAPL", adjust="qfq")
            print(f"AAPL前复权数据(前5条): {aapl_qfq[:5]}")
            
            # 获取MSFT不复权数据
            msft = await execute(symbol="MSFT")
            print(f"MSFT不复权数据(前5条): {msft[:5]}")
        except Exception as e:
            print(f"主程序出错: {str(e)}")
    
    asyncio.run(main())