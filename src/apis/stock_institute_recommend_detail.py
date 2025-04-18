import asyncio
from typing import List, Dict, Any
import akshare as ak

async def execute(symbol: str) -> List[Dict[str, Any]]:
    """
    异步获取新浪财经-机构推荐池-股票评级记录
    
    Args:
        symbol: 股票代码, 如 "000001"
        
    Returns:
        机构推荐详情列表, 每个元素为包含详细信息的字典
        
    Raises:
        Exception: 当获取数据失败时抛出异常
    """
    try:
        # 调用akshare同步接口, 使用await让出控制权
        df = await asyncio.get_event_loop().run_in_executor(
            None, 
            ak.stock_institute_recommend_detail, 
            symbol
        )
        
        # 将DataFrame转换为List[Dict]格式
        result = df.to_dict(orient="records")
        return result
    except Exception as e:
        raise Exception(f"获取机构推荐详情失败: {e}")

def test():
    """
    同步测试方法, 用于自动化测试
    
    Raises:
        Exception: 当execute方法执行失败时抛出异常
    """
    # 使用示例中的测试参数
    test_symbol = "002709"
    try:
        result = asyncio.run(execute(test_symbol))
        print("测试成功, 返回结果示例:", result[:1] if result else "空列表")
        return result
    except Exception as e:
        print(f"测试失败: {e}")
        raise

if __name__ == "__main__":
    # 演示如何调用异步函数
    async def main():
        try:
            # 使用示例中的参数
            result = await execute("002709")
            print("获取到的机构推荐详情:")
            for item in result[:3]:  # 打印前3条记录
                print(item)
        except Exception as e:
            print(f"执行出错: {e}")
    
    asyncio.run(main())