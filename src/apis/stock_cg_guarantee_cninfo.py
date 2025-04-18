import asyncio
from typing import List, Dict, Any
import akshare as ak

async def execute(symbol: str = "全部", start_date: str = "20180630", end_date: str = "20210927") -> List[Dict[str, Any]]:
    """
    异步获取巨潮资讯-数据中心-专题统计-公司治理-对外担保数据
    
    Args:
        symbol: 股票市场类型，可选值: "全部", "深市主板", "沪市", "创业板", "科创板"
        start_date: 开始日期，格式: YYYYMMDD
        end_date: 结束日期，格式: YYYYMMDD
    
    Returns:
        返回对外担保数据的字典列表
    
    Raises:
        Exception: 当数据获取失败时抛出异常
    """
    try:
        # 使用akshare同步接口获取数据
        df = ak.stock_cg_guarantee_cninfo(symbol=symbol, start_date=start_date, end_date=end_date)
        
        # 将DataFrame转换为字典列表
        result = df.to_dict(orient='records')
        return result
    except Exception as e:
        raise Exception(f"Failed to fetch stock guarantee data: {str(e)}")

def test():
    """
    同步测试方法，用于自动化测试
    
    Raises:
        当execute方法执行失败时直接抛出异常
    """
    try:
        # 使用示例参数调用异步execute方法
        result = asyncio.run(execute(symbol="全部", start_date="20180630", end_date="20210927"))
        print("Test executed successfully")
        return result
    except Exception as e:
        print(f"Test failed: {str(e)}")
        raise

if __name__ == "__main__":
    # 演示如何调用异步函数并打印结果
    async def main():
        try:
            data = await execute(symbol="全部", start_date="20180630", end_date="20210927")
            print("Data fetched successfully:")
            for item in data[:3]:  # 打印前3条记录
                print(item)
        except Exception as e:
            print(f"Error in main execution: {str(e)}")
    
    asyncio.run(main())