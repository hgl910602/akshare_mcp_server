import asyncio
from typing import List, Dict, Any
import akshare as ak

async def execute(symbol: str = "上证50") -> List[Dict[str, Any]]:
    """
    异步获取乐咕乐股-指数市盈率数据
    
    Args:
        symbol: 指数名称, 可选: {"上证50", "沪深300", "上证380", "创业板50", "中证500", 
                              "上证180", "深证红利", "深证100", "中证1000", "上证红利", 
                              "中证100", "中证800"}
    
    Returns:
        返回处理后的指数市盈率数据列表, 每个元素为一个字典
        
    Raises:
        Exception: 当获取数据失败时抛出异常
    """
    try:
        # 调用akshare接口获取数据
        df = ak.stock_index_pe_lg(symbol=symbol)
        
        # 处理数据为List[Dict]格式
        result = []
        for _, row in df.iterrows():
            item = {
                "日期": str(row["日期"]),
                "指数": float(row["指数"]),
                "等权静态市盈率": float(row["等权静态市盈率"]),
                "静态市盈率": float(row["静态市盈率"]),
                "静态市盈率中位数": float(row["静态市盈率中位数"]),
                "等权滚动市盈率": float(row["等权滚动市盈率"]),
                "滚动市盈率": float(row["滚动市盈率"]),
                "滚动市盈率中位数": float(row["滚动市盈率中位数"]),
            }
            result.append(item)
            
        return result
    except Exception as e:
        raise Exception(f"获取指数市盈率数据失败: {e}")

def test():
    """
    同步测试方法, 用于自动化测试
    
    Returns:
        返回execute方法的执行结果
        
    Raises:
        直接抛出execute方法可能抛出的异常
    """
    # 使用示例参数调用execute方法
    return asyncio.run(execute(symbol="上证50"))

if __name__ == "__main__":
    # 演示如何调用异步函数并打印结果
    async def main():
        try:
            data = await execute(symbol="上证50")
            for item in data:
                print(item)
        except Exception as e:
            print(f"Error: {e}")
    
    asyncio.run(main())