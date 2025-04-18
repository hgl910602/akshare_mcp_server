import asyncio
from typing import List, Dict, Any
import akshare as ak
import pandas as pd

async def execute(symbol: str = "巨潮行业分类标准") -> List[Dict[str, Any]]:
    """
    异步获取巨潮资讯行业分类数据
    
    Args:
        symbol: 行业分类标准, 可选值: 
            "证监会行业分类标准", "巨潮行业分类标准", "申银万国行业分类标准", 
            "新财富行业分类标准", "国资委行业分类标准", "巨潮产业细分标准", 
            "天相行业分类标准", "全球行业分类标准"
            
    Returns:
        行业分类数据列表, 每个条目是一个字典
        
    Raises:
        Exception: 当获取数据失败时抛出异常
    """
    try:
        # 调用akshare同步接口
        df = ak.stock_industry_category_cninfo(symbol=symbol)
        
        # 将DataFrame转换为List[Dict]格式
        result = df.to_dict(orient="records")
        
        # 处理datetime64类型字段
        for item in result:
            if "终止日期" in item and pd.notna(item["终止日期"]):
                item["终止日期"] = item["终止日期"].to_pydatetime()
                
        return result
    except Exception as e:
        raise Exception(f"获取行业分类数据失败: {str(e)}")

def test():
    """
    同步测试方法, 用于自动化测试
    
    Returns:
        行业分类数据列表
        
    Raises:
        原样抛出execute方法中的异常
    """
    # 使用asyncio.run运行异步方法
    return asyncio.run(execute(symbol="巨潮行业分类标准"))

if __name__ == "__main__":
    # 演示如何调用异步函数
    async def main():
        try:
            data = await execute(symbol="巨潮行业分类标准")
            print(f"获取到{len(data)}条行业分类数据")
            for i, item in enumerate(data[:3], 1):  # 打印前3条数据
                print(f"\n第{i}条数据:")
                for k, v in item.items():
                    print(f"{k}: {v}")
        except Exception as e:
            print(f"发生错误: {e}")
    
    asyncio.run(main())