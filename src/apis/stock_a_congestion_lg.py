import asyncio
from typing import List, Dict, Any
import akshare as ak

async def execute() -> List[Dict[str, Any]]:
    """
    异步获取乐咕乐股-大盘拥挤度数据
    
    Returns:
        List[Dict[str, Any]]: 返回处理后的数据列表，每个元素为包含日期、收盘价和拥挤度的字典
        
    Raises:
        Exception: 当数据获取或处理过程中出现错误时抛出异常
    """
    try:
        # 调用akshare接口获取数据
        df = ak.stock_a_congestion_lg()
        
        # 将DataFrame转换为List[Dict]格式
        result = []
        for _, row in df.iterrows():
            result.append({
                "date": row["date"],
                "close": row["close"],
                "congestion": row["congestion"]
            })
        return result
    except Exception as e:
        raise Exception(f"获取大盘拥挤度数据失败: {str(e)}")

def test() -> List[Dict[str, Any]]:
    """
    同步测试方法，用于自动化测试
    
    Returns:
        List[Dict[str, Any]]: 返回处理后的数据列表
        
    Raises:
        Exception: 当execute方法执行失败时抛出异常
    """
    try:
        return asyncio.run(execute())
    except Exception as e:
        raise e

if __name__ == "__main__":
    # 演示如何调用异步函数
    async def main():
        try:
            data = await execute()
            print(data[:5])  # 打印前5条数据
        except Exception as e:
            print(f"Error: {e}")
    
    asyncio.run(main())