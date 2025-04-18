import asyncio
from typing import List, Dict, Any
import akshare as ak
import pandas as pd

async def execute(date: str = "20240630") -> List[Dict[str, Any]]:
    """
    异步获取东方财富网-数据中心-特色数据-商誉-个股商誉明细
    
    Args:
        date: 查询日期，格式如"20240630"
        
    Returns:
        返回商誉数据列表，每个元素为包含字段的字典
        
    Raises:
        Exception: 当接口调用或数据处理出错时抛出
    """
    try:
        # 调用akshare接口获取数据
        df = ak.stock_sy_em(date=date)
        
        # 处理可能的空数据
        if df.empty:
            return []
            
        # 转换DataFrame为List[Dict]
        result = []
        for _, row in df.iterrows():
            item = {
                "序号": int(row["序号"]),
                "股票代码": str(row["股票代码"]),
                "股票简称": str(row["股票简称"]),
                "商誉": float(row["商誉"]),
                "商誉占净资产比例": float(row["商誉占净资产比例"]),
                "净利润": float(row["净利润"]),
                "净利润同比": float(row["净利润同比"]),
                "上年商誉": float(row["上年商誉"]),
                "公告日期": str(row["公告日期"]),
                "交易市场": str(row["交易市场"])
            }
            result.append(item)
            
        return result
        
    except Exception as e:
        raise Exception(f"获取商誉数据失败: {str(e)}")

def test():
    """
    同步测试方法，用于自动化测试
    
    Raises:
        原样抛出execute方法中的异常
    """
    try:
        # 使用示例参数调用
        data = asyncio.run(execute(date="20240630"))
        print(f"获取到{len(data)}条商誉数据")
        return data
    except Exception as e:
        print(f"测试失败: {str(e)}")
        raise

if __name__ == "__main__":
    # 演示如何调用异步函数
    async def main():
        try:
            data = await execute(date="20240630")
            print(f"获取到{len(data)}条数据")
            if data:
                print("第一条数据示例:")
                print(data[0])
        except Exception as e:
            print(f"调用失败: {str(e)}")
            
    asyncio.run(main())