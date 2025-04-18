import asyncio
from typing import List, Dict, Any
import akshare as ak

async def execute(symbol: str, date: str) -> List[Dict[str, Any]]:
    """
    异步获取沪深京A股公告数据
    
    Args:
        symbol: 公告类型，可选值: {"全部", "重大事项", "财务报告", "融资公告", "风险提示", "资产重组", "信息变更", "持股变动"}
        date: 指定日期，格式如"20220511"
    
    Returns:
        返回公告数据列表，每个元素为包含公告信息的字典
        
    Raises:
        Exception: 当akshare接口调用失败时抛出异常
    """
    try:
        # 调用akshare接口获取数据
        df = ak.stock_notice_report(symbol=symbol, date=date)
        # 将DataFrame转换为List[Dict]格式
        return df.to_dict(orient='records')
    except Exception as e:
        raise Exception(f"获取公告数据失败: {str(e)}")

def test():
    """
    同步测试方法，用于自动化测试
    
    Raises:
        原样抛出execute方法中的异常
    """
    # 使用示例参数调用
    symbol = "财务报告"
    date = "20240613"
    # 异步执行并返回结果
    return asyncio.run(execute(symbol=symbol, date=date))

if __name__ == '__main__':
    # 演示如何调用异步函数
    async def main():
        try:
            result = await execute(symbol="财务报告", date="20240613")
            print(result)
        except Exception as e:
            print(f"Error: {e}")
    
    asyncio.run(main())