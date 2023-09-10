## share.py
"""
This module contains the Share class for sharing messages using the WeChat API.
"""
from wechatpy import WeChatClient
from wechatpy.exceptions import WeChatClientException

class Share:
    """
    This class is responsible for sharing messages using the WeChat API.
    """
    def __init__(self, wechat_id: str, message: str):
        """
        Initialize a new instance of the Share class.

        :param wechat_id: The WeChat ID to send the message to.
        :param message: The message to send.
        """
        self.wechat_id = wechat_id
        self.message = message
        self.client = WeChatClient(appid='YOUR_APP_ID', secret='YOUR_APP_SECRET')

    def share(self):
        """
        Share the message to the specified WeChat ID.

        :raises WeChatClientException: If an error occurs while sharing the message.
        """
        try:
            self.client.message.send_text(self.wechat_id, self.message)
        except WeChatClientException as e:
            print(f"An error occurred while sharing the message: {e}")
