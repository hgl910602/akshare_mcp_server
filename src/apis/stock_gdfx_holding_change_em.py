import asyncio
from typing import List, Dict, Any
import akshare as ak
import pandas as pd

async def execute(date: str) -> List[Dict[str, Any]]:
    """
    东方财富网-数据中心-股东分析-股东持股变动统计-十大股东
    
    Args:
        date: 财报发布季度最后日, 例如: "20210930"
    
    Returns:
        List[Dict[str, Any]]: 转换后的股东持股变动数据列表
    
    Raises:
        Exception: 当接口调用或数据处理出错时抛出
    """
    try:
        # 调用akshare接口获取数据
        df = ak.stock_gdfx_holding_change_em(date=date)
        
        # 将DataFrame转换为List[Dict]格式
        if not df.empty:
            # 处理可能的NaN值
            df = df.fillna(0)
            # 转换数据类型
            df = df.astype({
                '序号': 'int',
                '股东名称': 'str',
                '股东类型': 'str',
                '期末持股只数统计-总持有': 'float',
                '期末持股只数统计-新进': 'float',
                '期末持股只数统计-增加': 'float',
                '期末持股只数统计-不变': 'float',
                '期末持股只数统计-减少': 'float',
                '流通市值统计': 'float',
                '持有个股': 'str'
            })
            return df.to_dict('records')
        return []
    except Exception as e:
        raise Exception(f"获取股东持股变动数据失败: {str(e)}")

def test():
    """
    同步测试方法，用于自动化测试
    
    Returns:
        List[Dict[str, Any]]: 转换后的股东持股变动数据列表
    
    Raises:
        Exception: 当execute方法调用出错时抛出
    """
    try:
        # 使用示例中的参数进行测试
        return asyncio.run(execute(date="20210930"))
    except Exception as e:
        raise Exception(f"测试失败: {str(e)}")

if __name__ == '__main__':
    # 演示如何调用异步函数
    async def main():
        try:
            data = await execute(date="20210930")
            print(data)
        except Exception as e:
            print(f"Error: {e}")
    
    asyncio.run(main())