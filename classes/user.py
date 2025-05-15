
# 責務ちゃんと分ける
# ログはUI側で出力する
class User:
    # 「一人のユーザ」 に対しての処理
    def __init__(self,name: str,balance: int):
        self.name = name
        self.balance = balance

    def deposit(self,amount: int):
        self.balance += amount
        return self.balance

    def get_balance(self) -> int:
        return self.balance

class UserManager:
    # 「複数ユーザの管理」 に対しての処理
    def __init__(self):
        self.users: dict[str,User] = {}

    def get_users(self)-> list[User]:
        return list(self.users.values())
       
    def add_user(self,name: str,balance: int):
        # nameというキーでユーザを辞書へ登録する
        self.users[name] = User(name,balance)
    
    def is_registered(self,name:str) -> bool:
        # ユーザが登録されているか確認する
        # name in self.usersでキーが存在するか確認できる
        return name in self.users