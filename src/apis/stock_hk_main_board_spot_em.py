import asyncio
from typing import Any, Dict, List
import akshare as ak
import pandas as pd

async def execute() -> List[Dict[str, Any]]:
    """
    获取港股主板的实时行情数据(有15分钟延时)
    
    Returns:
        List[Dict[str, Any]]: 港股主板实时行情数据列表，每个元素为一个股票的数据字典
        
    Raises:
        Exception: 当获取数据失败时抛出异常
    """
    try:
        # 调用akshare接口获取数据
        df = ak.stock_hk_main_board_spot_em()
        
        # 将DataFrame转换为List[Dict]格式
        result = df.to_dict(orient='records')
        
        # 转换数据类型，确保与接口描述一致
        for item in result:
            item['序号'] = int(item['序号'])
            item['代码'] = str(item['代码'])
            item['名称'] = str(item['名称'])
            item['最新价'] = float(item['最新价'])
            item['涨跌额'] = float(item['涨跌额'])
            item['涨跌幅'] = float(item['涨跌幅'])
            item['今开'] = float(item['今开'])
            item['最高'] = float(item['最高'])
            item['最低'] = float(item['最低'])
            item['昨收'] = float(item['昨收'])
            item['成交量'] = float(item['成交量'])
            item['成交额'] = float(item['成交额'])
            
        return result
    except Exception as e:
        raise Exception(f"获取港股主板实时行情数据失败: {e}")

def test() -> List[Dict[str, Any]]:
    """
    同步测试方法，用于自动化测试
    
    Returns:
        List[Dict[str, Any]]: 港股主板实时行情数据列表
        
    Raises:
        Exception: 当execute方法执行失败时抛出异常
    """
    try:
        return asyncio.run(execute())
    except Exception as e:
        raise Exception(f"测试获取港股主板实时行情数据失败: {e}")

if __name__ == '__main__':
    # 演示如何调用异步函数
    async def main():
        try:
            data = await execute()
            print(f"获取到{len(data)}条港股主板行情数据")
            if len(data) > 0:
                print("第一条数据示例:")
                print(data[0])
        except Exception as e:
            print(f"发生错误: {e}")
    
    asyncio.run(main())