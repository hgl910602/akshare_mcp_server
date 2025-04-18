import asyncio
from typing import List, Dict, Any
import akshare as ak

async def execute() -> List[Dict[str, Any]]:
    """
    异步获取申万宏源研究-行业分类-全部行业分类数据
    
    Returns:
        List[Dict[str, Any]]: 返回处理后的行业分类数据列表
    """
    try:
        # 调用akshare接口获取数据
        df = ak.stock_industry_clf_hist_sw()
        
        # 将DataFrame转换为List[Dict]格式
        result = df.to_dict(orient='records')
        return result
    except Exception as e:
        raise Exception(f"获取申万行业分类数据失败: {str(e)}")

def test() -> List[Dict[str, Any]]:
    """
    同步测试方法，用于自动化测试
    
    Returns:
        List[Dict[str, Any]]: 返回行业分类数据
        
    Raises:
        Exception: 当execute方法执行出错时抛出异常
    """
    try:
        return asyncio.run(execute())
    except Exception as e:
        raise e

if __name__ == '__main__':
    # 演示如何调用异步函数
    async def main():
        try:
            data = await execute()
            print(data[:5])  # 打印前5条数据
        except Exception as e:
            print(f"Error: {e}")
    
    asyncio.run(main())