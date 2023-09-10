class User:
    users = []

    def __init__(self, wechat_id: str, name: str, birth_date: str):
        self.wechat_id = wechat_id
        self.name = name
        self.birth_date = birth_date
        self.history = []
        self.__class__.users.append(self)

    @classmethod
    def get_user(cls, wechat_id: str):
        for user in cls.users:
            if user.wechat_id == wechat_id:
                return user
        return None

    def get_history(self) -> list:
        return self.history

    def add_to_history(self, prediction: str):
        self.history.append(prediction)
