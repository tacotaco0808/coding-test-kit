class Item:
    def __init__(self, item_name: str,price: int,seller: str):
        self.item_name = item_name
        self.price = price
        self.seller = seller

class ItemManager:
    def __init__(self):
        self.items: dict[str, Item]={}

    def get_items(self)-> list[Item]:
        return list(self.items.values())

    def add_item(self, item_name:str, price:int, seller:str):
        self.items[item_name] = Item(item_name,price,seller)
    
    def is_listed(self,item_name:str)-> bool:
        # アイテムが登録されているか確認する
        # name in self.usersでキーが存在するか確認できる
        return item_name in self.items