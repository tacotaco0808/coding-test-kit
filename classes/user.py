
# 責務ちゃんと分ける
class User:
    # 「一人のユーザ」 に対しての処理
    def __init__(self,name: str,balance: int):
        self.name = name
        self.balance = balance

    def deposit(self,amount: int):
        self.balance += amount

class UserManager:
    # 「複数ユーザの管理」 に対しての処理
    def __init__(self):
        self.users: dict[str,User] = {}

    def show_users(self):
        # d登録されているユーザを表示する
        for name, user in self.users.items():
            print(f"{name}: {user.balance}")
    
    def add_user(self,name: str,balance: int):
        # nameというキーでユーザを辞書へ登録する
        self.users[name] = User(name,balance)
    
    def is_registered(self,name:str) -> bool:
        # ユーザが登録されているか確認する
        # name in self.usersでキーが存在するか確認できる
        return name in self.users