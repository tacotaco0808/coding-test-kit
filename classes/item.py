class Item:
    def __init__(self, item_name: str,price: int,seller: str):
        self.item_name = item_name
        self.price = price
        self.seller = seller
        self.is_sold = False

    def sold(self):
        self.is_sold = True

    def update_price(self,new_price:int):
        self.price = new_price

class ItemManager:
    def __init__(self):
        self.items: dict[str, Item]={}

    def get_items(self)-> list[Item]:
        return list(self.items.values())

    def add_item(self, item_name:str, price:int, seller:str):
        self.items[item_name] = Item(item_name,price,seller)

    def update_item_price(self,item_name:str,price:int):
        self.items[item_name].update_price(price)

    def sold_item(self,item_name:str):
        self.items[item_name].is_sold = True

    def remove_item(self, item_name:str):
        if item_name in self.items:
            del self.items[item_name]
    
    def is_listed(self,item_name:str)-> bool:
        # アイテムが登録されているか確認する
        # name in self.usersでキーが存在するか確認できる
        return item_name in self.items