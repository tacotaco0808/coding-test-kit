from classes.item import ItemManager
from classes.user import UserManager


def handle_sell(timestamp: str, user_name:str,item_name: str, price: int,user_manager: UserManager,item_manager: ItemManager)-> str:
    # 例外処理
    if user_manager.is_registered(user_name)==False:
        return f"sell: {user_name} does not exist"
    
    if item_manager.is_listed(item_name):
        return f"sell: {item_name} is already listed"
    
    if price < 0:
        return f"sell: {price} is invalid"
    
    # アイテムを登録する
    item_manager.add_item(item_name,price,user_name)
    user_manager.add_sold_item_to_user(user_name,item_name,price)
    return f"sell: {user_name} listed {item_name} for {price}"
