import asyncio
from typing import List, Dict, Any
import akshare as ak

async def execute(date: str) -> List[Dict[str, Any]]:
    """
    异步获取百度股市通-财报发行数据
    
    Args:
        date: 日期, 格式为"YYYYMMDD"
        
    Returns:
        返回财报发行数据列表
        
    Raises:
        Exception: 当akshare接口调用失败时抛出异常
    """
    try:
        # 调用akshare接口获取数据
        df = ak.news_report_time_baidu(date=date)
        # 将DataFrame转换为List[Dict]格式
        return df.to_dict("records")
    except Exception as e:
        raise Exception(f"获取百度股市通财报发行数据失败: {e}")

def test():
    """
    同步测试方法，用于自动化测试
    
    Raises:
        当execute方法调用失败时抛出异常
    """
    # 使用示例中的参数进行测试
    test_date = "20241107"
    try:
        result = asyncio.run(execute(date=test_date))
        print("测试成功，返回结果:")
        print(result)
    except Exception as e:
        raise Exception(f"测试失败: {e}")

if __name__ == "__main__":
    # 演示如何调用异步函数
    async def main():
        try:
            # 使用示例中的参数
            result = await execute(date="20241107")
            print("调用成功，返回结果:")
            print(result)
        except Exception as e:
            print(f"调用失败: {e}")
    
    asyncio.run(main())