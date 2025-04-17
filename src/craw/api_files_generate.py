import sqlite3
import os
import re
import json  # 新增json导入
from pathlib import Path
from typing import List, Dict  # 新增类型导入
from craw.code_generator import CodeGenerator
from mcp.types import Tool
from enum import Enum
from persistence.generated_tool_repository import GeneratedToolRepository
from persistence.stock_interface_repository import StockInterfaceRepository


def _save_tools_to_db(conn, tools: List[Tool]):
    """将工具信息持久化到SQLite数据库"""
    cursor = conn.cursor()
    
    # 创建工具表(如果不存在)
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS generated_tools (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL UNIQUE,
        description TEXT,
        input_schema TEXT,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    ''')
    
    # 批量插入工具数据
    for tool in tools:
        try:
            cursor.execute('''
            INSERT OR REPLACE INTO generated_tools (name, description, input_schema)
            VALUES (?, ?, ?)
            ''', (
                tool.name,
                tool.description,
                json.dumps(tool.inputSchema)
            ))
        except sqlite3.Error as e:
            print(f"保存工具{tool.name}到数据库失败: {str(e)}")
    
    conn.commit()

def generate_api_files(update_threshold_minutes: int = 30):
    # 获取当前脚本所在目录
    current_dir = os.path.dirname(os.path.abspath(__file__))

    # API文件输出目录（相对路径）
    api_dir = os.path.join(current_dir, "../apis")
    
    # 确保目录存在
    os.makedirs(api_dir, exist_ok=True)
    
    # 初始化仓库 (移除下面重复的初始化)
    interface_repo = StockInterfaceRepository()
    tool_repo = GeneratedToolRepository()
    
    # 获取接口数据
    datas = interface_repo.get_all_interfaces()
    columns = interface_repo.get_table_columns()
    
    # 添加调试信息
    print(f"从数据库查询到 {len(datas)} 条接口记录")
    print(f"数据库列名: {columns}")
    
    # 为每个接口创建Python文件
    max_count = 1  # 限制最多处理5个接口
    processed_count = 0
    
    for data in datas:
        if processed_count >= max_count:
            print(f"已达到最大处理数量限制({max_count}/{processed_count})，停止处理")
            break
            
        # 直接使用返回的字典，不需要重新构造
        data_dict = data  
        interface_name = data_dict.get('interface_name', '')
        print(f"获取到的接口名称: {repr(interface_name)}")
        if not interface_name:
            continue
            
        module_name = re.sub(r'[^\w]', '_', interface_name.lower())
        
        # 检查是否最近更新过，传入时间阈值
        if tool_repo.is_recently_updated(module_name, update_threshold_minutes):
            print(f"接口 {interface_name} 最近已更新，跳过处理")
            processed_count += 1
            continue
            
        file_path = os.path.join(api_dir, f"{module_name}.py")
        
        # 生成代码文件
        generator = CodeGenerator()
        generated_code = generator.generate_implementation(data_dict)
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(generated_code)
        
        # 保存新记录
        tool = Tool(
            name=module_name,
            description=data_dict.get('description', ''),
            inputSchema=_generate_input_schema(data_dict),
        )
        tool_repo.save_tool(tool)
        
        processed_count += 1
        print(f"已生成接口文件: {file_path}")

    print(f"完成! 共生成 {processed_count} 个接口文件")
    return tool_repo.get_all_tools()

def _generate_input_schema(data_dict: Dict) -> Dict:  # 移除了self参数
    """根据接口信息生成输入参数schema"""
    input_params = data_dict.get('input_params', '')
    if not input_params:
        return {"type": "object", "properties": {}, "required": []}
    
    # 解析输入参数表格
    properties = {}
    required = []
    for line in input_params.split('\n'):
        if '|' not in line:
            continue
        parts = [p.strip() for p in line.split('|') if p.strip()]
        if len(parts) >= 3 and parts[0] != '名称':
            param_name = parts[0]
            param_type = parts[1]
            param_desc = parts[2]
            
            # 映射参数类型
            schema_type = "string"
            if "int" in param_type.lower():
                schema_type = "integer"
            elif "float" in param_type.lower():
                schema_type = "number"
            elif "bool" in param_type.lower():
                schema_type = "boolean"
                
            properties[param_name] = {
                "type": schema_type,
                "description": param_desc
            }
            if "必填" in param_desc or "required" in param_desc.lower():
                required.append(param_name)
    
    return {
        "type": "object",
        "properties": properties,
        "required": required
    }

if __name__ == "__main__":
    generate_api_files()