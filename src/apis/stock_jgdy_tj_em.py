import asyncio
from typing import List, Dict, Any
import akshare as ak
import pandas as pd

async def execute(date: str) -> List[Dict[str, Any]]:
    """
    异步获取机构调研统计数据
    
    Args:
        date: 查询日期，格式为"YYYYMMDD"
        
    Returns:
        机构调研统计数据列表，每个元素为一个字典
        
    Raises:
        Exception: 当akshare接口调用失败时抛出异常
    """
    try:
        # 调用akshare接口获取数据
        df = ak.stock_jgdy_tj_em(date=date)
        
        # 将DataFrame转换为List[Dict]格式
        if not df.empty:
            # 处理可能的NaN值
            df = df.fillna("")
            # 转换数据类型
            df["序号"] = df["序号"].astype(int)
            df["最新价"] = df["最新价"].astype(float)
            df["涨跌幅"] = df["涨跌幅"].astype(float)
            df["接待机构数量"] = df["接待机构数量"].astype(int)
            return df.to_dict("records")
        return []
    except Exception as e:
        raise Exception(f"获取机构调研统计数据失败: {str(e)}")

def test():
    """
    同步测试方法，用于自动化测试
    
    Returns:
        机构调研统计数据列表
        
    Raises:
        异常上抛，不捕获
    """
    # 使用示例中的参数
    date = "20210128"
    return asyncio.run(execute(date=date))

if __name__ == "__main__":
    # 演示如何调用异步函数
    async def main():
        try:
            data = await execute(date="20210128")
            print(f"获取到{len(data)}条机构调研数据")
            if data:
                print("第一条数据示例:")
                print(data[0])
        except Exception as e:
            print(f"发生错误: {e}")
    
    asyncio.run(main())