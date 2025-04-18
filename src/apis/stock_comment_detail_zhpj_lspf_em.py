import asyncio
from typing import List, Dict, Any
import akshare as ak

async def execute(symbol: str) -> List[Dict[str, Any]]:
    """
    异步获取东方财富网-数据中心-特色数据-千股千评-综合评价-历史评分数据
    
    Args:
        symbol: 股票代码，如 "600000"
        
    Returns:
        返回包含历史评分数据的字典列表
        
    Raises:
        Exception: 当获取数据失败时抛出异常
    """
    try:
        # 调用akshare同步接口，使用run_in_executor避免阻塞事件循环
        loop = asyncio.get_running_loop()
        df = await loop.run_in_executor(
            None, 
            ak.stock_comment_detail_zhpj_lspf_em, 
            symbol
        )
        
        # 将DataFrame转换为List[Dict]格式
        result = df.to_dict(orient='records')
        return result
    except Exception as e:
        raise Exception(f"获取股票{symbol}综合评价历史评分失败: {str(e)}")

def test():
    """
    同步测试方法，用于自动化测试
    
    Returns:
        返回execute方法的执行结果
        
    Raises:
        直接抛出execute方法可能产生的异常
    """
    # 使用示例中的测试参数
    symbol = "600000"
    return asyncio.run(execute(symbol))

if __name__ == '__main__':
    # 演示如何调用异步函数
    async def main():
        try:
            data = await execute("600000")
            print("获取数据成功:")
            for item in data:
                print(item)
        except Exception as e:
            print(f"发生错误: {e}")
    
    asyncio.run(main())