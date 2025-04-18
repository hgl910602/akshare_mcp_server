import asyncio
from typing import List, Dict, Any
import akshare as ak

async def execute(date: str) -> List[Dict[str, Any]]:
    """
    异步获取巨潮资讯-数据中心-专题统计-公司治理-股权质押数据
    
    Args:
        date: 查询日期, 格式如 "20210930"
    
    Returns:
        返回处理后的字典列表
    
    Raises:
        Exception: 当akshare接口调用失败时抛出异常
    """
    try:
        # 调用akshare同步接口
        df = ak.stock_cg_equity_mortgage_cninfo(date=date)
        
        # 将DataFrame转换为字典列表
        result = df.to_dict(orient='records')
        return result
    except Exception as e:
        raise Exception(f"获取股权质押数据失败: {str(e)}")

def test():
    """
    同步测试方法，用于自动化测试
    
    Raises:
        异常上抛不捕获
    """
    # 使用示例参数调用
    result = asyncio.run(execute(date="20210930"))
    return result

if __name__ == '__main__':
    # 演示如何调用异步函数
    async def main():
        try:
            data = await execute(date="20210930")
            print(data[:2])  # 打印前两条数据
        except Exception as e:
            print(f"Error: {e}")
    
    asyncio.run(main())