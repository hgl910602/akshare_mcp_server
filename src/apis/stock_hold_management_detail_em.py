import asyncio
from typing import List, Dict, Any
import akshare as ak

async def execute() -> List[Dict[str, Any]]:
    """
    获取东方财富网-数据中心-特色数据-高管持股-董监高及相关人员持股变动明细
    
    Returns:
        List[Dict[str, Any]]: 返回高管持股变动明细数据列表
    """
    try:
        # 调用akshare接口获取数据
        df = ak.stock_hold_management_detail_em()
        
        # 将DataFrame转换为List[Dict]格式
        result = df.to_dict(orient='records')
        return result
    except Exception as e:
        raise Exception(f"获取高管持股变动明细数据失败: {e}")

def test():
    """
    同步测试方法，用于自动化测试
    """
    try:
        # 使用asyncio.run执行异步方法
        result = asyncio.run(execute())
        return result
    except Exception as e:
        # 异常上抛，不捕获
        raise e

if __name__ == '__main__':
    # 演示如何调用异步函数并打印结果
    async def main():
        try:
            data = await execute()
            print(data[:2])  # 打印前两条数据示例
        except Exception as e:
            print(f"Error: {e}")
    
    asyncio.run(main())