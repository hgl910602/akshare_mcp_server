import asyncio
from typing import List, Dict, Any
import akshare as ak
import pandas as pd

async def execute() -> List[Dict[str, Any]]:
    """
    获取乐咕乐股-A 股等权重与中位数市净率数据
    
    Returns:
        List[Dict[str, Any]]: 转换后的市净率数据列表
    """
    try:
        # 调用akshare接口获取数据
        df = ak.stock_a_all_pb()
        
        # 将DataFrame转换为List[Dict]格式
        result = []
        if not df.empty:
            # 确保列名正确
            expected_columns = [
                'date', 'middlePB', 'equalWeightAveragePB', 'close',
                'quantileInAllHistoryMiddlePB', 'quantileInRecent10YearsMiddlePB',
                'quantileInAllHistoryEqualWeightAveragePB', 'quantileInRecent10YearsEqualWeightAveragePB'
            ]
            # 检查列是否存在
            for col in expected_columns:
                if col not in df.columns:
                    raise ValueError(f"Column '{col}' not found in response data")
            
            # 转换数据
            result = df.to_dict('records')
        return result
    except Exception as e:
        raise Exception(f"Failed to fetch stock A all PB data: {str(e)}")

def test() -> List[Dict[str, Any]]:
    """
    同步测试方法，用于验证execute函数
    
    Returns:
        List[Dict[str, Any]]: 市净率数据列表
        
    Raises:
        Exception: 当execute执行失败时抛出异常
    """
    try:
        return asyncio.run(execute())
    except Exception as e:
        raise Exception(f"Test failed: {str(e)}")

if __name__ == '__main__':
    # 示例调用
    async def main():
        try:
            data = await execute()
            print("Successfully fetched data:")
            for item in data[:5]:  # 打印前5条记录
                print(item)
        except Exception as e:
            print(f"Error occurred: {e}")
    
    asyncio.run(main())