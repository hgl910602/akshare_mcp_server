import asyncio
from typing import List, Dict, Any
import akshare as ak

async def execute(date: str) -> List[Dict[str, Any]]:
    """
    异步获取北交所资产负债表数据
    
    Args:
        date: 财报日期，格式为"YYYY0331", "YYYY0630", "YYYY0930", "YYYY1231"
    
    Returns:
        返回处理后的字典列表形式的数据
        
    Raises:
        Exception: 当akshare接口调用失败时抛出异常
    """
    try:
        # 调用akshare接口获取数据
        df = ak.stock_zcfz_bj_em(date=date)
        
        # 将DataFrame转换为字典列表
        result = df.to_dict(orient="records")
        
        return result
    except Exception as e:
        raise Exception(f"获取北交所资产负债表数据失败: {e}")

def test():
    """
    同步测试方法，用于自动化测试
    
    Returns:
        返回execute方法的执行结果
        
    Raises:
        直接抛出execute方法可能产生的异常
    """
    # 使用示例中的参数进行测试
    date = "20240331"
    return asyncio.run(execute(date))

if __name__ == "__main__":
    # 演示如何调用异步函数
    async def main():
        try:
            data = await execute(date="20240331")
            print(data[:2])  # 打印前两条数据作为示例
        except Exception as e:
            print(f"Error: {e}")
    
    asyncio.run(main())