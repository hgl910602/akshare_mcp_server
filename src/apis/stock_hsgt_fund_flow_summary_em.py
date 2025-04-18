import asyncio
from typing import List, Dict, Any
import akshare as ak

async def execute() -> List[Dict[str, Any]]:
    """
    获取东方财富网-数据中心-资金流向-沪深港通资金流向数据
    
    Returns:
        List[Dict[str, Any]]: 沪深港通资金流向数据列表，每个元素为字典形式的数据记录
        
    Raises:
        Exception: 当获取数据失败时抛出异常
    """
    try:
        # 调用akshare接口获取数据
        df = ak.stock_hsgt_fund_flow_summary_em()
        # 将DataFrame转换为List[Dict]格式
        return df.to_dict(orient='records')
    except Exception as e:
        raise Exception(f"获取沪深港通资金流向数据失败: {e}")

def test() -> List[Dict[str, Any]]:
    """
    同步测试方法，用于自动化测试
    
    Returns:
        List[Dict[str, Any]]: 沪深港通资金流向数据
        
    Raises:
        Exception: 当execute方法执行失败时抛出异常
    """
    return asyncio.run(execute())

if __name__ == '__main__':
    # 演示如何调用异步函数并打印结果
    async def main():
        try:
            data = await execute()
            print("沪深港通资金流向数据:")
            for item in data:
                print(item)
        except Exception as e:
            print(f"发生错误: {e}")
    
    asyncio.run(main())