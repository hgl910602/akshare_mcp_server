import asyncio
from typing import Any, Dict, List
import akshare as ak

async def execute(date: str = "20230331") -> List[Dict[str, Any]]:
    """
    异步获取东方财富网-数据中心-特色数据-商誉-个股商誉减值明细
    
    Args:
        date: 报告日期, 格式如"20230331"
        
    Returns:
        List[Dict[str, Any]]: 返回转换后的字典列表
        
    Raises:
        Exception: 当akshare接口调用失败时抛出异常
    """
    try:
        # 调用akshare同步接口
        df = ak.stock_sy_jz_em(date=date)
        # 转换DataFrame为字典列表
        return df.to_dict("records")
    except Exception as e:
        raise Exception(f"获取个股商誉减值明细失败: {str(e)}")

def test():
    """
    同步测试方法，用于自动化测试
    
    Returns:
        List[Dict[str, Any]]: 返回转换后的字典列表
        
    Raises:
        Exception: 当execute方法调用失败时抛出异常
    """
    try:
        # 使用示例参数调用异步方法
        return asyncio.run(execute(date="20230331"))
    except Exception as e:
        raise Exception(f"测试失败: {str(e)}")

if __name__ == "__main__":
    # 演示如何调用异步函数
    async def main():
        try:
            data = await execute(date="20230331")
            print(data[:2])  # 打印前两条数据
        except Exception as e:
            print(f"Error: {e}")
    
    asyncio.run(main())