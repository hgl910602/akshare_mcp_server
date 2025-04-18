import asyncio
from typing import List, Dict, Any
import akshare as ak

async def execute(date: str) -> List[Dict[str, Any]]:
    """
    异步获取融资融券标的证券名单及保证金比例
    
    Args:
        date: 查询日期，格式为YYYYMMDD
        
    Returns:
        融资融券标的证券名单及保证金比例数据列表
        
    Raises:
        Exception: 当akshare接口调用失败时抛出异常
    """
    try:
        # 调用akshare同步接口，使用await在异步环境中执行
        df = await asyncio.get_event_loop().run_in_executor(
            None, 
            lambda: ak.stock_margin_ratio_pa(date=date)
        
        # 将DataFrame转换为List[Dict]格式
        result = df.to_dict(orient="records")
        return result
    except Exception as e:
        raise Exception(f"Failed to fetch stock margin ratio data: {str(e)}")

def test():
    """
    同步测试方法，用于自动化测试
    
    Raises:
        Exception: 当execute方法调用失败时抛出异常
    """
    # 使用示例中的参数进行测试
    test_date = "20231013"
    try:
        result = asyncio.run(execute(date=test_date))
        print(f"Test executed successfully. Got {len(result)} records.")
        return result
    except Exception as e:
        print(f"Test failed: {str(e)}")
        raise

if __name__ == "__main__":
    # 演示如何调用异步函数
    async def main():
        try:
            data = await execute(date="20231013")
            print("Sample data:")
            for i, item in enumerate(data[:3]):  # 打印前3条记录
                print(f"{i+1}. {item}")
        except Exception as e:
            print(f"Error: {str(e)}")
    
    asyncio.run(main())