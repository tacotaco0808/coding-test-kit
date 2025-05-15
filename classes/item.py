class Item:
    def __init__(self, item_name: str,price: int,seller: str):
        self.item_name = item_name
        self.price = price
        self.seller = seller

class ItemManager:
    def __init__(self):
        self.items: dict[str, Item]={}

    def show_items(self):
        # d登録されているアイテムを表示する
        for name, item in self.items.items():
            print(f"{name}: {item.price} by {item.seller}")

    def add_item(self, item_name:str, price:int, seller:str):
        self.items[item_name] = Item(item_name,price,seller)
    
    def is_listed(self,item_name:str)-> bool:
        # アイテムが登録されているか確認する
        # name in self.usersでキーが存在するか確認できる
        return item_name in self.items