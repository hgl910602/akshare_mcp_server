import sqlite3
import json
import os
import datetime
from typing import List, Optional
from mcp.types import Tool

class GeneratedToolRepository:
    def __init__(self):
        """初始化仓库，使用固定路径的数据库文件"""
        current_dir = os.path.dirname(os.path.abspath(__file__))
        self.db_path = os.path.join(current_dir, "tools_meta.db")
        self._ensure_table_exists()
    
    def _ensure_table_exists(self):
        """确保表存在并包含所有需要的列"""
        conn = sqlite3.connect(self.db_path)
        try:
            cursor = conn.cursor()
            cursor.execute('''
            CREATE TABLE IF NOT EXISTS generated_tools (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL UNIQUE,
                description TEXT,
                input_schema TEXT,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
            ''')
            conn.commit()
        finally:
            conn.close()

    def get_tool(self, name: str) -> Optional[Tool]:
        """获取指定工具"""
        conn = sqlite3.connect(self.db_path)
        try:
            cursor = conn.cursor()
            cursor.execute('''
            SELECT name, description, input_schema, updated_at 
            FROM generated_tools 
            WHERE name = ?
            ''', (name,))
            result = cursor.fetchone()
            if result:
                return Tool(
                    name=result[0],
                    description=result[1],
                    inputSchema=json.loads(result[2])
                ), result[3]  # 返回Tool对象和更新时间
            return None, None
        finally:
            conn.close()

    def is_recently_updated(self, name: str, minutes: int) -> bool:
        """检查工具是否在指定分钟内更新过
        Args:
            name: 工具名称
            minutes: 检查的时间范围(分钟)
        """
        conn = sqlite3.connect(self.db_path)
        try:
            cursor = conn.cursor()
            cursor.execute('''
            SELECT updated_at FROM generated_tools 
            WHERE name = ? AND datetime(updated_at) > datetime('now', ?)
            ''', (name, f'-{minutes} minutes'))
            return cursor.fetchone() is not None
        finally:
            conn.close()

    def get_all_tools(self) -> List[Tool]:
        """获取所有工具"""
        conn = sqlite3.connect(self.db_path)
        try:
            cursor = conn.cursor()
            cursor.execute("SELECT name, description, input_schema FROM generated_tools")
            tools = []
            for name, description, input_schema in cursor.fetchall():
                tools.append(
                    Tool(
                        name=name,
                        description=description,
                        inputSchema=json.loads(input_schema)
                    )
                )
            return tools
        finally:
            conn.close()
    
    def delete_tool(self, name: str):
        """删除指定工具"""
        conn = sqlite3.connect(self.db_path)
        try:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM generated_tools WHERE name = ?", (name,))
            conn.commit()
        finally:
            conn.close()
    
    def save_tool(self, tool: Tool):
        """保存或更新工具数据"""
        conn = sqlite3.connect(self.db_path)
        try:
            cursor = conn.cursor()
            # 检查工具是否已存在
            cursor.execute("SELECT 1 FROM generated_tools WHERE name = ?", (tool.name,))
            exists = cursor.fetchone() is not None
            
            if exists:
                # 更新现有记录
                cursor.execute('''
                UPDATE generated_tools 
                SET description = ?, input_schema = ?, updated_at = CURRENT_TIMESTAMP
                WHERE name = ?
                ''', (
                    tool.description,
                    json.dumps(tool.inputSchema),
                    tool.name
                ))
            else:
                # 插入新记录
                cursor.execute('''
                INSERT INTO generated_tools 
                (name, description, input_schema, updated_at)
                VALUES (?, ?, ?, CURRENT_TIMESTAMP)
                ''', (
                    tool.name,
                    tool.description,
                    json.dumps(tool.inputSchema)
                ))
            conn.commit()
        finally:
            conn.close()