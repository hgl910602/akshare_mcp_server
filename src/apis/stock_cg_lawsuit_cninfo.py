import asyncio
from typing import List, Dict, Any
import akshare as ak

async def execute(symbol: str = "全部", start_date: str = "20180630", end_date: str = "20210927") -> List[Dict[str, Any]]:
    """
    异步获取巨潮资讯-数据中心-专题统计-公司治理-公司诉讼数据
    
    Args:
        symbol: 股票市场类型，可选值: "全部", "深市主板", "沪市", "创业板", "科创板"
        start_date: 开始日期，格式: YYYYMMDD
        end_date: 结束日期，格式: YYYYMMDD
    
    Returns:
        公司诉讼数据列表，每个元素为一个字典
    
    Raises:
        Exception: 当获取数据失败时抛出异常
    """
    try:
        # 调用akshare的同步接口，使用await在异步环境中运行
        df = await asyncio.get_event_loop().run_in_executor(
            None,
            lambda: ak.stock_cg_lawsuit_cninfo(symbol=symbol, start_date=start_date, end_date=end_date)
        )
        # 将DataFrame转换为List[Dict]格式
        return df.to_dict("records")
    except Exception as e:
        raise Exception(f"获取公司诉讼数据失败: {e}")

def test():
    """
    同步测试方法，用于自动化测试
    
    Raises:
        原样抛出execute方法中的异常
    """
    try:
        result = asyncio.run(execute(symbol="全部", start_date="20180630", end_date="20210927"))
        print(f"测试成功，获取到{len(result)}条数据")
        return result
    except Exception as e:
        print(f"测试失败: {e}")
        raise

if __name__ == "__main__":
    # 演示如何调用异步函数
    async def main():
        try:
            data = await execute(symbol="全部", start_date="20180630", end_date="20210927")
            print(f"获取到{len(data)}条公司诉讼数据:")
            for item in data[:5]:  # 打印前5条数据
                print(item)
        except Exception as e:
            print(f"获取数据时出错: {e}")
    
    asyncio.run(main())