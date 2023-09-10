## notification.py
from wechatpy import WeChatClient
from wechatpy.exceptions import WeChatClientException

class Notification:
    def __init__(self, wechat_id: str, message: str):
        self.wechat_id = wechat_id
        self.message = message
        self.client = WeChatClient(appid='YOUR_APP_ID', secret='YOUR_APP_SECRET')

    def send(self):
        try:
            self.client.message.send_text(self.wechat_id, self.message)
        except WeChatClientException as e:
            print(f"An error occurred while sending the notification: {e}")
