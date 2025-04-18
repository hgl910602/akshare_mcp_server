import asyncio
from typing import List, Dict, Any
import akshare as ak

async def execute(symbol: str = "沪深A股", date: str = "20211231") -> List[Dict[str, Any]]:
    """
    异步获取东方财富-数据中心-年报季报-预约披露时间数据
    
    Args:
        symbol: 股票板块类型，可选值: {'沪深A股', '沪市A股', '科创板', '深市A股', '创业板', '京市A股', 'ST板'}
        date: 报告期，格式为"XXXX0331", "XXXX0630", "XXXX0930", "XXXX1231"，从20081231开始
    
    Returns:
        返回预约披露时间数据列表，每个元素为包含字段的字典
    
    Raises:
        Exception: 当akshare接口调用失败时抛出异常
    """
    try:
        # 调用akshare同步接口，使用await在异步环境中运行
        df = await asyncio.get_event_loop().run_in_executor(
            None, 
            lambda: ak.stock_yysj_em(symbol=symbol, date=date)
        )
        # 将DataFrame转换为List[Dict]格式
        return df.to_dict("records")
    except Exception as e:
        raise Exception(f"获取预约披露时间数据失败: {str(e)}")

def test():
    """
    同步测试方法，用于自动化测试
    
    Raises:
        直接抛出execute方法中的异常
    """
    try:
        result = asyncio.run(execute(symbol="沪深A股", date="20211231"))
        print(f"测试成功，获取到{len(result)}条数据")
        return result
    except Exception as e:
        print(f"测试失败: {str(e)}")
        raise

if __name__ == "__main__":
    # 演示如何调用异步函数
    async def main():
        try:
            data = await execute(symbol="沪深A股", date="20211231")
            print(f"获取到{len(data)}条数据:")
            for item in data[:5]:  # 打印前5条数据
                print(item)
        except Exception as e:
            print(f"调用失败: {str(e)}")
    
    asyncio.run(main())