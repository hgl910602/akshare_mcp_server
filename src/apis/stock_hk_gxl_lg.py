import asyncio
from typing import List, Dict, Any
import akshare as ak

async def execute() -> List[Dict[str, Any]]:
    """
    异步获取乐咕乐股-股息率-恒生指数股息率数据
    
    Returns:
        List[Dict[str, Any]]: 返回处理后的数据列表，每个元素为包含日期和股息率的字典
        
    Raises:
        Exception: 当数据获取或处理失败时抛出异常
    """
    try:
        # 调用akshare接口获取数据
        df = ak.stock_hk_gxl_lg()
        
        # 将DataFrame转换为List[Dict]格式
        result = []
        for _, row in df.iterrows():
            result.append({
                "日期": str(row["日期"]),
                "股息率": float(row["股息率"])
            })
        return result
    except Exception as e:
        raise Exception(f"获取恒生指数股息率数据失败: {str(e)}")

def test() -> List[Dict[str, Any]]:
    """
    同步测试方法，用于自动化测试
    
    Returns:
        List[Dict[str, Any]]: 返回execute方法的结果
        
    Raises:
        Exception: 当execute方法执行失败时抛出异常
    """
    try:
        return asyncio.run(execute())
    except Exception as e:
        raise Exception(f"测试执行失败: {str(e)}")

if __name__ == "__main__":
    # 演示如何异步调用该函数
    async def main():
        try:
            data = await execute()
            print(data)
        except Exception as e:
            print(f"Error: {e}")
    
    asyncio.run(main())