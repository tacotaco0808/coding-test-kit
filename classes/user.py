
# 責務ちゃんと分ける
# ログはUI側で出力する
class User:
    # 「一人のユーザ」 に対しての処理
    def __init__(self,name: str,balance: int):
        self.name = name
        self.balance = balance
        self.sales = 0
        self.history : list[dict[str,int|str]] = []
        self.sold_items: list[dict[str,int|str]] = []

    def deposit(self,amount: int):
        self.balance += amount
        self.history.append({"action":"deposit","amount":amount})
        return self.balance

    def get_balance(self) -> int:
        return self.balance

    def add_sold_item(self,item_name:str,price:int):
        self.sold_items.append(
            {
            "action": "sold_item",
            "item_name": item_name,
            "amount": price
            }
        )


class UserManager:
    # 「複数ユーザの管理」に対しての処理
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
    
    def get_history(self,user_name: str):
        return self.users[user_name].history
    
    def add_sold_item_to_user(self,user_name:str,item_name:str,price: int):
        self.users[user_name].add_sold_item(item_name,price)

    def get_sold_items(self,user_name:str ):
        return self.users[user_name].sold_items