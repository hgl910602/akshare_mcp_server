import asyncio
from typing import Any, Dict, List
import akshare as ak

async def execute(symbol: str = "行业关注度") -> List[Dict[str, Any]]:
    """
    异步获取新浪财经-机构推荐池数据
    
    Args:
        symbol: 指标类型，默认为"行业关注度"
            choice of {'最新投资评级', '上调评级股票', '下调评级股票', '股票综合评级', 
                      '首次评级股票', '目标涨幅排名', '机构关注度', '行业关注度', '投资评级选股'}
    
    Returns:
        机构推荐数据列表，每个元素为一个字典
        
    Raises:
        Exception: 当akshare接口调用失败时抛出
    """
    try:
        # 调用akshare同步接口，使用await包装
        result_df = await asyncio.get_event_loop().run_in_executor(
            None, 
            ak.stock_institute_recommend, 
            symbol
        )
        # 将DataFrame转换为List[Dict]格式
        return result_df.to_dict(orient="records")
    except Exception as e:
        raise Exception(f"获取机构推荐数据失败: {e}")

def test():
    """
    同步测试方法，用于自动化测试
    
    Raises:
        原样抛出execute方法中的异常
    """
    try:
        # 使用示例参数调用
        result = asyncio.run(execute(symbol="投资评级选股"))
        return result
    except Exception as e:
        raise e

if __name__ == "__main__":
    # 演示如何调用异步函数
    async def main():
        try:
            data = await execute(symbol="机构关注度")
            print(data[:2])  # 打印前两条数据
        except Exception as e:
            print(f"Error: {e}")
    
    asyncio.run(main())