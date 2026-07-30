"""飞书 MCP Server 集成测试"""
import json
import unittest
from lark_mcp_server.client import LarkClient


class TestLarkClient(unittest.TestCase):
    """LarkClient 集成测试（需 lark-cli 已认证）"""

    @classmethod
    def setUpClass(cls):
        cls.client = LarkClient()
        cls.test_chat_id = "oc_9edfb338e77b043b23b822f3e2c0538b"
        cls.group_chat_id = "oc_7b37547d7f240a2c66f189529a6353dc"

    def test_01_list_chats(self):
        """列群聊"""
        result = self.client.list_chats(page_size=5)
        data = json.loads(result)
        self.assertTrue(data.get("ok"))
        self.assertIn("chats", data.get("data", {}))

    def test_02_send_message(self):
        """发送文本消息"""
        result = self.client.send_message(self.test_chat_id, "🤖 自动测试消息")
        data = json.loads(result)
        self.assertTrue(data.get("ok"))
        self.assertIn("message_id", data.get("data", {}))

    def test_03_send_markdown(self):
        """发送 Markdown 消息"""
        md = "**Markdown 测试**\n- 项目A\n- 项目B"
        result = self.client.send_message(self.test_chat_id, md, msg_type="markdown")
        data = json.loads(result)
        self.assertTrue(data.get("ok"))

    def test_04_list_messages(self):
        """查看聊天历史"""
        result = self.client.list_messages(self.test_chat_id, page_size=3)
        data = json.loads(result)
        self.assertTrue(data.get("ok"))

    def test_05_get_agenda(self):
        """获取日程"""
        result = self.client.get_agenda()
        data = json.loads(result)
        self.assertTrue(data.get("ok"))


if __name__ == "__main__":
    unittest.main(verbosity=2)
