import asyncio
from typing import List, Dict, Any
import akshare as ak
import pandas as pd

async def execute(date: str) -> List[Dict[str, Any]]:
    """
    东方财富网-数据中心-股东分析-股东持股分析-十大股东
    
    Args:
        date: 财报发布季度最后日, 例如: "20210930"
    
    Returns:
        List[Dict[str, Any]]: 十大股东数据列表
    
    Raises:
        Exception: 当接口调用失败时抛出异常
    """
    try:
        # 调用akshare接口获取数据
        df = ak.stock_gdfx_holding_analyse_em(date=date)
        
        # 将DataFrame转换为List[Dict]格式
        if not df.empty:
            # 处理可能的NaN值
            df = df.fillna(0)
            # 转换数据类型
            df = df.astype({
                '序号': int,
                '期末持股-数量': float,
                '期末持股-数量变化': float,
                '期末持股-数量变化比例': float,
                '期末持股-持股变动': float,
                '期末持股-流通市值': float,
                '公告日后涨跌幅-10个交易日': float,
                '公告日后涨跌幅-30个交易日': float,
                '公告日后涨跌幅-60个交易日': float
            })
            return df.to_dict('records')
        return []
    except Exception as e:
        raise Exception(f"获取股东持股分析数据失败: {str(e)}")

def test():
    """
    同步测试方法，用于自动化测试
    
    Returns:
        List[Dict[str, Any]]: 十大股东数据列表
    
    Raises:
        Exception: 当接口调用失败时抛出异常
    """
    try:
        # 使用示例中的参数进行测试
        result = asyncio.run(execute(date="20210930"))
        return result
    except Exception as e:
        raise Exception(f"测试失败: {str(e)}")

if __name__ == '__main__':
    # 演示如何调用异步函数
    async def main():
        try:
            data = await execute(date="20210930")
            print(f"获取到 {len(data)} 条股东持股数据")
            if data:
                print("第一条数据示例:")
                print(data[0])
        except Exception as e:
            print(f"发生错误: {e}")
    
    asyncio.run(main())