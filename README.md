# Lark MCP Server / 飞书 MCP Server

> 🇨🇳 The first Chinese MCP Server for Lark/Feishu — let any AI client operate Feishu through MCP protocol.
> 🇨🇳 首个飞书 MCP Server — 让任何 AI 客户端通过标准 MCP 协议操作飞书。

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Python](https://img.shields.io/badge/python-3.10+-blue.svg)](pyproject.toml)
[![MCP](https://img.shields.io/badge/MCP-2025--11--25-blue)](https://modelcontextprotocol.io)

## 🚀 Quick Start / 快速开始

### Install / 安装

```bash
# via pip
pip install lark-mcp-server

# or via uvx (no install needed)
uvx lark-mcp-server
```

### Prerequisites / 前提条件

You need [lark-cli](https://github.com/agent-garden/lark-cli) installed and authenticated:

```bash
# Install lark-cli & login
lark-cli auth login
```

### Configure with Claude Desktop / 配置到 Claude Desktop

Add to your `claude_desktop_config.json`:

```json
{
  "mcpServers": {
    "lark": {
      "command": "uvx",
      "args": ["lark-mcp-server"]
    }
  }
}
```

Now Claude can send/receive Feishu messages, list chats, and more! 🤖

---

## 🛠️ Tools / 工具列表

### 💬 IM Messages / 消息

| Tool | Description | 说明 |
|------|-------------|------|
| `lark_send_message` | Send text/markdown to a chat | 发送消息到聊天 |
| `lark_reply_message` | Reply to a message | 回复消息 |
| `lark_list_chats` | List group chats | 列出群聊列表 |
| `lark_get_chat_members` | Get chat member list | 获取群成员 |
| `lark_list_messages` | View chat history | 查看聊天历史 |
| `lark_send_card` | Send interactive card | 发送交互卡片 |

### 👤 Contacts / 联系人

| Tool | Description | 说明 |
|------|-------------|------|
| `lark_get_user_info` | Get user information | 获取用户信息 |

### 📅 Calendar / 日历

| Tool | Description | 说明 |
|------|-------------|------|
| `lark_get_agenda` | View calendar agenda | 查看日程安排 |

---

## 💡 Use Cases / 使用场景

### 🤖 AI Agent Automates Feishu / Agent 自动处理飞书消息

```python
# Your AI agent can now:
# - Monitor and reply to messages automatically
# - Send batch notifications to group chats
# - Check meeting schedules and notify attendees
```

### 📊 Data Integration / 数据集成

```python
# Connect Feishu with other tools via MCP:
# - Read Feishu messages → process with AI → write to database
# - Sync calendar events to your task manager
# - Automate HR onboarding workflows
```

### 🔄 Cross-platform Automation / 跨平台自动化

```python
# Feishu + GitHub + Slack = automated workflow
# All connected through standard MCP protocol
```

---

## 📦 Project Structure / 项目结构

```
lark-mcp-server/
├── pyproject.toml          # Python package config
├── src/lark_mcp_server/
│   ├── server.py           # MCP server entry, tool registration
│   └── client.py           # LarkClient — lark-cli subprocess wrapper
└── tests/
    └── test_client.py      # Integration tests
```

---

## 🔗 Related Projects / 相关项目

- [lark-cli](https://github.com/agent-garden/lark-cli) — Lark/Feishu CLI tool
- [YuanZhiTech](https://github.com/YuanZhiTech) — Our Agent Garden organization

---

## 📄 License

MIT © 2026 Agent Garden

*Built by AI Agents, for AI Agents.* 🤖
*由 AI Agent 构建，为 AI Agent 服务。*
