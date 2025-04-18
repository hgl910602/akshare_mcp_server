import asyncio
from typing import List, Dict, Any
import akshare as ak

async def execute(symbol: str, indicator: str, period: str) -> List[Dict[str, Any]]:
    """
    异步获取港股估值指标数据
    
    Args:
        symbol: 港股代码，如 "02358"
        indicator: 估值指标，可选 {"总市值", "市盈率(TTM)", "市盈率(静)", "市净率", "市现率"}
        period: 时间周期，可选 {"近一年", "近三年", "全部"}
    
    Returns:
        返回包含日期和值的字典列表
    
    Raises:
        Exception: 当获取数据失败时抛出异常
    """
    try:
        # 调用akshare同步接口，由于akshare没有原生异步支持，这里用run_in_executor包装
        loop = asyncio.get_running_loop()
        df = await loop.run_in_executor(
            None, 
            ak.stock_hk_valuation_baidu, 
            symbol, 
            indicator, 
            period
        )
        
        # 将DataFrame转换为List[Dict]格式
        result = df.to_dict(orient="records")
        return result
    except Exception as e:
        raise Exception(f"获取港股估值数据失败: {str(e)}")

def test():
    """
    同步测试方法，用于自动化测试
    
    Raises:
        异常上抛不捕获
    """
    try:
        # 使用示例参数调用
        result = asyncio.run(execute(symbol="06969", indicator="总市值", period="近一年"))
        print("测试成功，返回结果:", result)
        return result
    except Exception as e:
        print("测试失败:", str(e))
        raise

if __name__ == "__main__":
    # 演示如何调用异步函数
    async def main():
        try:
            data = await execute(symbol="02358", indicator="市盈率(TTM)", period="近三年")
            print("获取到的数据:")
            for item in data:
                print(item)
        except Exception as e:
            print(f"调用失败: {e}")
    
    asyncio.run(main())