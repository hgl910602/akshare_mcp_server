import asyncio
from typing import List, Dict, Any
import akshare as ak

async def execute() -> List[Dict[str, Any]]:
    """
    获取东方财富网-数据中心-特色数据-股权质押-上市公司质押比例-行业数据
    
    Returns:
        List[Dict[str, Any]]: 返回处理后的行业质押数据列表
        
    Raises:
        Exception: 当数据获取或处理失败时抛出异常
    """
    try:
        # 调用akshare接口获取数据
        df = ak.stock_gpzy_industry_data_em()
        
        # 将DataFrame转换为字典列表
        result = df.to_dict(orient='records')
        
        # 转换数据类型 (确保float64转换为Python原生float)
        for item in result:
            for key, value in item.items():
                if hasattr(value, 'item'):  # 处理numpy类型
                    item[key] = value.item()
        return result
    except Exception as e:
        raise Exception(f"获取行业质押数据失败: {str(e)}")

def test() -> List[Dict[str, Any]]:
    """
    同步测试方法，用于自动化测试
    
    Returns:
        List[Dict[str, Any]]: 返回行业质押数据
        
    Raises:
        Exception: 当execute方法执行失败时抛出异常
    """
    try:
        return asyncio.run(execute())
    except Exception as e:
        raise Exception(f"测试执行失败: {str(e)}")

if __name__ == '__main__':
    # 演示异步调用
    async def main():
        try:
            data = await execute()
            print("获取行业质押数据成功:")
            for item in data:
                print(item)
        except Exception as e:
            print(f"执行出错: {e}")
    
    asyncio.run(main())