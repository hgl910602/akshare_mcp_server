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

# Configure logging
logger = logging.getLogger(__name__)

class AKShareTools(str, Enum):
    """
    Enum for AKShare tools.
    """
    STOCK_ZH_A_SPOT = "stock_zh_a_spot"
    STOCK_ZH_A_HIST = "stock_zh_a_hist"
    STOCK_ZH_INDEX_SPOT = "stock_zh_index_spot"
    STOCK_ZH_INDEX_DAILY = "stock_zh_index_daily"
    FUND_ETF_CATEGORY_SINA = "fund_etf_category_sina"
    FUND_ETF_HIST_SINA = "fund_etf_hist_sina"
    MACRO_CHINA_GDP = "macro_china_gdp"
    MACRO_CHINA_CPI = "macro_china_cpi"
    FOREX_SPOT_QUOTE = "forex_spot_quote"
    FUTURES_ZH_SPOT = "futures_zh_spot"
    BOND_ZH_HS_COV_SPOT = "bond_zh_hs_cov_spot"
    STOCK_ZT_POOL_STRONG_EM = "stock_zt_pool_strong_em"
    STOCK_BOARD_INDEX_SPOT = "stock_board_index_spot"
    STOCK_BOARD_INDEX_HIST = "stock_board_index_hist"


# Create the server
server = Server("akshare")


class AKShareTools(str, Enum):
    """自动生成的工具枚举"""
    @classmethod
    def from_generated_tools(cls, tools: List[types.Tool]):
        """从生成的工具创建枚举"""
        for tool in tools:
            setattr(cls, tool.name.upper(), tool.name)
        return cls

# 在初始化时注册工具
from persistence.generated_tool_repository import GeneratedToolRepository

@server.list_tools()
async def handle_list_tools() -> List[types.Tool]:
    """从数据库获取所有工具"""
    repo = GeneratedToolRepository()
    tools = repo.get_all_tools()
    return [
        types.Tool(
            name=tool.name,
            description=tool.description,
            inputSchema=tool.inputSchema
        )
        for tool in tools
    ]

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