import asyncio
from typing import List, Dict, Any
import akshare as ak

async def execute(symbol: str = "北向资金增持行业板块排行", indicator: str = "今日") -> List[Dict[str, Any]]:
    """
    异步获取东方财富网-数据中心-沪深港通持股-板块排行数据
    
    Args:
        symbol: 板块类型，可选值: 
            "北向资金增持行业板块排行", "北向资金增持概念板块排行", "北向资金增持地域板块排行"
        indicator: 时间周期，可选值: 
            "今日", "3日", "5日", "10日", "1月", "1季", "1年"
            
    Returns:
        返回处理后的字典列表形式的数据
        
    Raises:
        Exception: 当akshare接口调用失败时抛出异常
    """
    try:
        # 调用akshare接口获取数据
        df = ak.stock_hsgt_board_rank_em(symbol=symbol, indicator=indicator)
        # 将DataFrame转换为字典列表
        result = df.to_dict(orient="records")
        return result
    except Exception as e:
        raise Exception(f"获取沪深港通持股板块排行数据失败: {str(e)}")

def test() -> List[Dict[str, Any]]:
    """
    同步测试方法，用于自动化测试
    
    Returns:
        返回execute方法的执行结果
        
    Raises:
        直接抛出execute方法可能产生的异常
    """
    try:
        # 使用示例参数调用execute方法
        return asyncio.run(execute(symbol="北向资金增持行业板块排行", indicator="今日"))
    except Exception as e:
        raise e

if __name__ == "__main__":
    # 演示如何调用异步函数并打印结果
    async def main():
        try:
            data = await execute(symbol="北向资金增持行业板块排行", indicator="今日")
            print(data)
        except Exception as e:
            print(f"发生错误: {e}")
    
    asyncio.run(main())