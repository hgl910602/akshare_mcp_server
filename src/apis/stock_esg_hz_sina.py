import asyncio
from typing import List, Dict, Any
import akshare as ak
import pandas as pd

async def execute() -> List[Dict[str, Any]]:
    """
    异步获取新浪财经-ESG评级中心-华证指数ESG评级数据
    
    Returns:
        List[Dict[str, Any]]: 转换后的ESG评级数据列表
    """
    try:
        # 调用akshare接口获取数据
        df = ak.stock_esg_hz_sina()
        
        # 将DataFrame转换为List[Dict]格式
        if not df.empty:
            return df.to_dict(orient='records')
        return []
    except Exception as e:
        raise RuntimeError(f"获取ESG评级数据失败: {e}")

def test() -> List[Dict[str, Any]]:
    """
    同步测试方法，用于外部调用测试
    
    Returns:
        List[Dict[str, Any]]: ESG评级数据
        
    Raises:
        Exception: 当execute方法执行出错时抛出
    """
    try:
        return asyncio.run(execute())
    except Exception as e:
        raise Exception(f"测试执行失败: {e}")

if __name__ == '__main__':
    # 演示如何调用异步函数
    async def main():
        try:
            data = await execute()
            print(f"获取到{len(data)}条ESG评级数据")
            if data:
                print("第一条数据示例:")
                print(data[0])
        except Exception as e:
            print(f"执行出错: {e}")
    
    asyncio.run(main())