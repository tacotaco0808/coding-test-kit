from classes.item import ItemManager
from classes.user import UserManager


def handle_purchase(timestamp: str,user_name:str,item_name:str,user_manager: UserManager,item_manager: ItemManager)->str:
    # 例外処理
    if user_manager.is_registered(user_name) == False:
        return f"purchase: {user_name} does not exist"
    if item_manager.is_listed(item_name) == False:
        return f"purchase: {item_name} does not exist"
    if item_manager.items[item_name].seller == user_name:
        return f"purchase: {item_name} is your own listing"
    if item_manager.items[item_name].price > user_manager.users[user_name].balance:
        return f"purchase: {user_name} does not have enough balance"
    # 購入処理 購入者からアイテムの価格を引き、出品者にアイテムの価格を加算する。売り上げも加算する
    user_manager.users[user_name].balance -= item_manager.items[item_name].price
    seller_name = item_manager.items[item_name].seller
    user_manager.users[seller_name].sales += item_manager.items[item_name].price
    user_manager.users[seller_name].balance += item_manager.items[item_name].price
    # 購入履歴に追加
    price = item_manager.get_item_price(item_name)
    user_manager.add_purchased_item_to_user(user_name,item_name,price)
    # アイテムを売れたことにする
    # item_manager.remove_item(item_name)　//商品が売れても商品一覧に表示されるかどうかで仕様が変わる
    item_manager.sold_item(item_name)


    return f"purchase: {user_name} bought {item_name}"