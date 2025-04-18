import asyncio
from typing import List, Dict, Any
import akshare as ak

async def execute(analyst_id: str, indicator: str) -> List[Dict[str, Any]]:
    """
    异步获取东方财富分析师详情数据
    
    Args:
        analyst_id: 分析师ID, 从 ak.stock_analyst_rank_em() 获取
        indicator: 指标类型, 从 {"最新跟踪成分股", "历史跟踪成分股", "历史指数"} 中选择
        
    Returns:
        返回处理后的字典列表
        
    Raises:
        Exception: 当akshare接口调用失败时抛出异常
    """
    try:
        # 调用akshare接口获取数据
        df = ak.stock_analyst_detail_em(analyst_id=analyst_id, indicator=indicator)
        
        # 将DataFrame转换为字典列表
        result = df.to_dict(orient="records")
        return result
    except Exception as e:
        raise Exception(f"获取分析师详情数据失败: {str(e)}")

def test():
    """
    同步测试方法，用于自动化测试
    
    Raises:
        直接抛出execute方法可能产生的异常
    """
    # 使用示例参数调用
    test_analyst_id = "11000200926"
    test_indicator = "历史指数"
    
    # 异步调用execute方法
    result = asyncio.run(execute(test_analyst_id, test_indicator))
    return result

if __name__ == "__main__":
    # 演示如何调用异步函数
    async def main():
        try:
            # 使用示例参数调用
            analyst_id = "11000200926"
            indicator = "历史指数"
            
            result = await execute(analyst_id, indicator)
            print(result)
        except Exception as e:
            print(f"发生错误: {e}")
    
    # 运行主函数
    asyncio.run(main())