import asyncio
from typing import List, Dict, Any
import akshare as ak
import pandas as pd

async def execute(date: str) -> List[Dict[str, Any]]:
    """
    东方财富网-数据中心-股东分析-股东持股统计-十大股东
    
    Args:
        date: 财报发布季度最后日, 例如: "20210930"
    
    Returns:
        List[Dict[str, Any]]: 十大股东持股统计信息
    
    Raises:
        Exception: 当获取数据失败时抛出异常
    """
    try:
        # 调用akshare接口获取数据
        df = ak.stock_gdfx_holding_statistics_em(date=date)
        
        # 将DataFrame转换为List[Dict]格式
        result = []
        if not df.empty:
            # 处理可能的NaN值
            df = df.where(pd.notnull(df), None)
            result = df.to_dict('records')
        
        return result
    except Exception as e:
        raise Exception(f"获取股东持股统计信息失败: {str(e)}")

def test():
    """
    同步测试方法，用于自动化测试
    
    Raises:
        Exception: 当execute方法执行失败时抛出异常
    """
    # 使用示例中的参数进行测试
    test_date = "20210930"
    try:
        result = asyncio.run(execute(date=test_date))
        print(f"测试成功，获取到{len(result)}条数据")
    except Exception as e:
        raise Exception(f"测试失败: {str(e)}")

if __name__ == '__main__':
    # 演示如何调用异步函数
    async def main():
        try:
            data = await execute(date="20210930")
            print(f"获取到{len(data)}条数据:")
            for item in data[:3]:  # 打印前3条数据
                print(item)
        except Exception as e:
            print(f"发生错误: {str(e)}")
    
    asyncio.run(main())