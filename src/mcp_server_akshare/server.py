"""
MCP server implementation for AKShare.
"""

import asyncio
import json
import logging
from enum import Enum
from typing import Any, Dict, List, Optional, Union

import mcp.server.stdio
import mcp.types as types
from mcp.server import NotificationOptions, Server
from mcp.server.models import InitializationOptions
from persistence.generated_tool_repository import GeneratedToolRepository

# Configure logging
logger = logging.getLogger(__name__)

# Create the server
server = Server("akshare")

class AKShareTools(str, Enum):
    """动态生成的工具枚举"""
    @classmethod
    def initialize(cls):
        """从数据库初始化工具枚举"""
        repo = GeneratedToolRepository()
        tools = repo.get_all_tools()
        for tool in tools:
            setattr(cls, tool.name.upper(), tool.name)
        return cls

# Initialize tools when module loads
AKShareTools.initialize()

@server.list_tools()
async def handle_list_tools() -> List[types.Tool]:
    """从数据库获取所有工具"""
    repo = GeneratedToolRepository()
    return repo.get_all_tools()

def _get_input_schema(func: callable) -> Dict:
    """从函数签名生成输入schema"""
    # 实现从函数参数生成schema的逻辑
    # ... 具体实现根据函数参数生成 ...


@server.call_tool()
async def handle_call_tool(
    name: str, arguments: Dict[str, Any] | None
) -> List[types.TextContent | types.ImageContent | types.EmbeddedResource]:
    try:
        if arguments is None:
            arguments = {}
            
        # 动态导入对应的API模块
        module_name = f"apis.{name}"
        try:
            module = __import__(module_name, fromlist=[''])
        except ImportError as e:
            raise ValueError(f"Tool module {name} not found: {str(e)}")
        
        # 检查模块中是否有execute方法
        if not hasattr(module, 'execute'):
            raise ValueError(f"Module {name} does not have execute method")
            
        # 调用execute方法并传入参数
        result = await module.execute(**arguments)
        
        # 转换结果为JSON字符串
        if hasattr(result, 'to_dict'):  # 检查是否是DataFrame
            result_json = json.dumps(result.to_dict(orient='records'), ensure_ascii=False, indent=2)
        else:
            result_json = json.dumps(result, ensure_ascii=False, indent=2)
            
        return [types.TextContent(type="text", text=result_json)]
        
    except Exception as e:
        logger.error(f"Error executing tool {name}: {e}", exc_info=True)
        try:
            line_no = e.__traceback__.tb_lineno
            error_message = f"Error executing tool {name} at line {line_no}: {str(e)}"
        except AttributeError:
            error_message = f"Error executing tool {name}: {str(e)}"
        return [types.TextContent(type="text", text=error_message)]


async def main() -> None:
    """
    Main entry point for the server.
    """
    # Run the server using stdin/stdout streams
    async with mcp.server.stdio.stdio_server() as (read_stream, write_stream):
        await server.run(
            read_stream,
            write_stream,
            InitializationOptions(
                server_name="akshare",
                server_version="0.1.0",
                capabilities=server.get_capabilities(
                    notification_options=NotificationOptions(),
                    experimental_capabilities={},
                ),
            ),
        )