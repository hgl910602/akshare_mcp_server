import asyncio
from typing import List, Dict, Any
import akshare as ak

async def execute(date: str) -> List[Dict[str, Any]]:
    """
    异步获取巨潮资讯-数据中心-评级预测-投资评级数据
    
    Args:
        date: 交易日, 格式如 "20210910"
        
    Returns:
        List[Dict[str, Any]]: 转换后的机构评级数据列表
        
    Raises:
        Exception: 当接口调用或数据处理出错时抛出
    """
    try:
        # 调用akshare接口获取数据
        df = ak.stock_rank_forecast_cninfo(date=date)
        
        # 将DataFrame转换为List[Dict]格式
        result = df.to_dict(orient="records")
        return result
    except Exception as e:
        raise Exception(f"获取机构评级数据失败: {str(e)}")

def test():
    """
    同步测试方法，用于自动化测试
    
    Returns:
        List[Dict[str, Any]]: 机构评级数据
        
    Raises:
        Exception: 当execute方法调用出错时抛出
    """
    # 使用示例中的日期参数
    test_date = "20230817"
    return asyncio.run(execute(date=test_date))

if __name__ == "__main__":
    # 演示如何调用异步函数
    async def main():
        try:
            data = await execute(date="20230817")
            print(data[:2])  # 打印前两条数据
        except Exception as e:
            print(f"Error: {e}")
    
    asyncio.run(main())