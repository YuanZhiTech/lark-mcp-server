"""lark-cli 子进程调用封装"""
import subprocess
import json
import logging
from typing import Optional

logger = logging.getLogger(__name__)

# lark-cli 命令路径（假设在 PATH 中）
LARK_CLI = "lark-cli"

# 调用超时（秒）
CMD_TIMEOUT = 30


class LarkClient:
    """封装对 lark-cli 的 subprocess 调用"""

    @staticmethod
    def _run(cmd: list[str], timeout: int = CMD_TIMEOUT) -> str:
        """执行 lark-cli 命令，返回 stdout"""
        try:
            result = subprocess.run(
                [LARK_CLI, *cmd],
                capture_output=True,
                text=True,
                timeout=timeout,
            )
            if result.returncode != 0:
                err = result.stderr.strip() or f"exit code {result.returncode}"
                raise RuntimeError(f"lark-cli 调用失败: {err}")
            return result.stdout.strip()
        except subprocess.TimeoutExpired:
            raise RuntimeError(f"lark-cli 超时 ({timeout}s)")
        except FileNotFoundError:
            raise RuntimeError("未找到 lark-cli，请确认已安装并在 PATH 中")
        except RuntimeError:
            raise

    # ── IM 消息 ──

    def send_message(self, chat_id: str, content: str,
                     msg_type: str = "text") -> str:
        """发送消息到飞书聊天"""
        if msg_type == "text":
            return self._run([
                "im", "+messages-send",
                "--chat-id", chat_id,
                "--text", content,
                "--format", "json",
            ])
        elif msg_type == "markdown":
            return self._run([
                "im", "+messages-send",
                "--chat-id", chat_id,
                "--markdown", content,
                "--format", "json",
            ])
        else:
            return self._run([
                "im", "+messages-send",
                "--chat-id", chat_id,
                "--msg-type", msg_type,
                "--content", content,
                "--format", "json",
            ])

    def reply_message(self, message_id: str, content: str,
                      msg_type: str = "text",
                      is_thread: bool = False) -> str:
        """回复消息"""
        cmd = [
            "im", "+messages-reply",
            "--message-id", message_id,
            "--format", "json",
        ]
        if msg_type == "text":
            cmd.extend(["--text", content])
        elif msg_type == "markdown":
            cmd.extend(["--markdown", content])
        else:
            cmd.extend(["--msg-type", msg_type, "--content", content])
        if is_thread:
            cmd.append("--reply-in-thread")
        return self._run(cmd)

    def list_chats(self, page_size: int = 20,
                   page_token: Optional[str] = None) -> str:
        """列出群聊列表"""
        cmd = ["im", "+chat-list", "--page-size", str(page_size), "--format", "json"]
        if page_token:
            cmd.extend(["--page-token", page_token])
        return self._run(cmd)

    def get_chat_members(self, chat_id: str) -> str:
        """获取群成员列表"""
        return self._run([
            "im", "+chat-members-list",
            "--chat-id", chat_id,
            "--format", "json",
        ])

    def list_messages(self, chat_id: str, page_size: int = 20) -> str:
        """获取聊天历史消息"""
        return self._run([
            "im", "+chat-messages-list",
            "--chat-id", chat_id,
            "--page-size", str(page_size),
            "--format", "json",
        ])

    def send_card(self, chat_id: str, card_json: str) -> str:
        """发送交互卡片"""
        return self._run([
            "im", "send-card",
            "--chat-id", chat_id,
            "--card", card_json,
            "--format", "json",
        ])

    # ── 联系人 ──

    def get_user_info(self, user_id: Optional[str] = None) -> str:
        """获取用户信息，不传 user_id 查自己"""
        cmd = ["contact", "+get-user", "--format", "json"]
        if user_id:
            cmd.extend(["--user-id", user_id])
        return self._run(cmd)

    # ── 日历 ──

    def get_agenda(self, start: Optional[str] = None,
                   end: Optional[str] = None,
                   calendar_id: str = "primary") -> str:
        """查看日程"""
        cmd = ["calendar", "+agenda", "--calendar-id", calendar_id, "--format", "json"]
        if start:
            cmd.extend(["--start", start])
        if end:
            cmd.extend(["--end", end])
        return self._run(cmd)
