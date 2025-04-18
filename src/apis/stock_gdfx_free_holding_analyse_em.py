import asyncio
from typing import List, Dict, Any
import akshare as ak

async def execute(date: str) -> List[Dict[str, Any]]:
    """
    异步获取东方财富网-数据中心-股东分析-股东持股分析-十大流通股东数据
    
    Args:
        date: 财报发布季度最后日, 格式如 "20230930"
        
    Returns:
        List[Dict[str, Any]]: 转换后的十大流通股东数据列表
        
    Raises:
        Exception: 当akshare接口调用失败时抛出异常
    """
    try:
        # 调用akshare同步接口
        df = ak.stock_gdfx_free_holding_analyse_em(date=date)
        # 将DataFrame转换为List[Dict]格式
        return df.to_dict(orient="records")
    except Exception as e:
        raise Exception(f"获取十大流通股东数据失败: {str(e)}")

def test():
    """
    同步测试方法，用于自动化测试
    
    Returns:
        List[Dict[str, Any]]: 转换后的十大流通股东数据列表
        
    Raises:
        原样抛出execute方法可能抛出的异常
    """
    # 使用示例中的参数
    test_date = "20230930"
    return asyncio.run(execute(date=test_date))

if __name__ == "__main__":
    # 演示如何调用异步函数
    async def main():
        try:
            data = await execute(date="20230930")
            print(data[:2])  # 打印前两条数据示例
        except Exception as e:
            print(f"Error: {e}")
    
    asyncio.run(main())