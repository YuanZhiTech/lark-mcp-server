"""lark-mcp-server — 飞书 MCP Server，基于 fastmcp

使用方式：
    python -m lark_mcp_server
    # 或安装后：lark-mcp-server

配置到 Claude Desktop：
    {
        "mcpServers": {
            "lark": {
                "command": "uvx",
                "args": ["lark-mcp-server"]
            }
        }
    }
"""
import logging
from typing import Optional

from fastmcp import FastMCP

from .client import LarkClient

logger = logging.getLogger(__name__)

# MCP Server 实例
mcp = FastMCP("lark-mcp-server")

# 全局 client 实例
_client: Optional[LarkClient] = None


def get_client() -> LarkClient:
    global _client
    if _client is None:
        _client = LarkClient()
    return _client


# ════════════════════════════════════════════
# IM 消息工具
# ════════════════════════════════════════════

@mcp.tool()
def lark_send_message(chat_id: str, content: str,
                      msg_type: str = "text") -> str:
    """发送消息到飞书聊天

    Args:
        chat_id: 聊天 ID（群聊 oc_xxx 或 P2P 会话）
        content: 消息内容
        msg_type: 消息类型，可选 text / markdown / post
    """
    return get_client().send_message(chat_id, content, msg_type)


@mcp.tool()
def lark_reply_message(message_id: str, content: str,
                       msg_type: str = "text",
                       is_thread: bool = False) -> str:
    """回复飞书消息

    Args:
        message_id: 被回复的消息 ID（om_xxx）
        content: 回复内容
        msg_type: 消息类型，可选 text / markdown / post
        is_thread: 是否回复到原帖（thread）
    """
    return get_client().reply_message(message_id, content, msg_type, is_thread)


@mcp.tool()
def lark_list_chats(page_size: int = 20,
                    page_token: Optional[str] = None) -> str:
    """列出飞书群聊列表

    Args:
        page_size: 每页数量（默认 20）
        page_token: 分页 token
    """
    return get_client().list_chats(page_size, page_token)


@mcp.tool()
def lark_get_chat_members(chat_id: str) -> str:
    """获取群聊成员列表

    Args:
        chat_id: 群聊 ID
    """
    return get_client().get_chat_members(chat_id)


@mcp.tool()
def lark_list_messages(chat_id: str, page_size: int = 20) -> str:
    """查看聊天历史消息

    Args:
        chat_id: 聊天 ID
        page_size: 获取消息数量（默认 20）
    """
    return get_client().list_messages(chat_id, page_size)


@mcp.tool()
def lark_send_card(chat_id: str, card_json: str) -> str:
    """发送交互卡片到飞书聊天

    Args:
        chat_id: 聊天 ID
        card_json: 卡片 JSON（schema 2.0 格式）
    """
    return get_client().send_card(chat_id, card_json)


# ════════════════════════════════════════════
# 联系人工具
# ════════════════════════════════════════════

@mcp.tool()
def lark_get_user_info(user_id: Optional[str] = None) -> str:
    """获取飞书用户信息，不传 user_id 查自己

    Args:
        user_id: 用户 ID（可选）
    """
    return get_client().get_user_info(user_id)


# ════════════════════════════════════════════
# 日历工具
# ════════════════════════════════════════════

@mcp.tool()
def lark_get_agenda(start: Optional[str] = None,
                    end: Optional[str] = None,
                    calendar_id: str = "primary") -> str:
    """查看飞书日程安排

    Args:
        start: 开始时间（ISO 8601，默认今天开始）
        end: 结束时间（ISO 8601，默认今天结束）
        calendar_id: 日历 ID（默认 primary）
    """
    return get_client().get_agenda(start, end, calendar_id)


# ════════════════════════════════════════════
# 入口
# ════════════════════════════════════════════

def main():
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(name)s] %(levelname)s: %(message)s",
    )
    logger.info("启动飞书 MCP Server...")
    mcp.run()


if __name__ == "__main__":
    main()
