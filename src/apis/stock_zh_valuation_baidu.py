import asyncio
from typing import List, Dict, Any
import akshare as ak

async def execute(symbol: str, indicator: str, period: str) -> List[Dict[str, Any]]:
    """
    异步获取百度股市通-A股估值数据
    
    Args:
        symbol: A股代码，如"002044"
        indicator: 估值指标，可选 {"总市值", "市盈率(TTM)", "市盈率(静)", "市净率", "市现率"}
        period: 时间周期，可选 {"近一年", "近三年", "近五年", "近十年", "全部"}
    
    Returns:
        估值数据列表，每个元素为包含date和value的字典
    
    Raises:
        Exception: 当akshare接口调用失败时抛出异常
    """
    try:
        # 调用akshare同步接口，使用await在异步环境中执行
        df = await asyncio.get_event_loop().run_in_executor(
            None, 
            ak.stock_zh_valuation_baidu, 
            symbol, 
            indicator, 
            period
        )
        # 将DataFrame转换为List[Dict]格式
        return df.to_dict('records')
    except Exception as e:
        raise Exception(f"获取估值数据失败: {str(e)}")

def test():
    """
    同步测试方法，用于自动化测试
    
    Raises:
        Exception: 当execute方法调用失败时抛出异常
    """
    try:
        result = asyncio.run(execute(symbol="002044", indicator="总市值", period="近一年"))
        print("测试成功，返回数据条数:", len(result))
        return result
    except Exception as e:
        print("测试失败:", str(e))
        raise

if __name__ == '__main__':
    # 演示如何调用异步函数
    async def main():
        try:
            data = await execute(symbol="002044", indicator="总市值", period="近一年")
            print("获取到的估值数据:")
            for item in data:
                print(item)
        except Exception as e:
            print(f"Error: {e}")
    
    asyncio.run(main())