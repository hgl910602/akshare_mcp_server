import asyncio
from typing import List, Dict, Any
import akshare as ak

async def execute(date: str) -> List[Dict[str, Any]]:
    """
    异步获取新浪财经-龙虎榜-每日详情数据
    
    Args:
        date: 交易日, 格式如 "20240222"
        
    Returns:
        龙虎榜每日详情数据列表
        
    Raises:
        Exception: 当获取数据失败时抛出异常
    """
    try:
        # 调用akshare接口获取数据
        df = ak.stock_lhb_detail_daily_sina(date=date)
        
        # 将DataFrame转换为List[Dict]格式
        result = df.to_dict(orient="records")
        
        return result
    except Exception as e:
        raise Exception(f"获取龙虎榜详情数据失败: {e}")

def test():
    """
    同步测试方法，用于自动化测试
    
    Raises:
        Exception: 当execute方法执行失败时抛出异常
    """
    # 使用示例中的参数进行测试
    test_date = "20240222"
    try:
        result = asyncio.run(execute(date=test_date))
        print(f"测试成功，获取到{len(result)}条数据")
    except Exception as e:
        raise Exception(f"测试失败: {e}")

if __name__ == "__main__":
    # 演示如何调用该函数
    async def main():
        try:
            # 使用示例参数调用
            data = await execute(date="20240222")
            print("获取到的龙虎榜详情数据:")
            for item in data:
                print(item)
        except Exception as e:
            print(f"发生错误: {e}")
    
    # 运行主程序
    asyncio.run(main())