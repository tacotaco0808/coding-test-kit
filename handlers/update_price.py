from classes.item import ItemManager
from classes.user import UserManager


def handle_update_price(timestamp:str,user_name:str,item_name:str,new_price:int,user_manager:UserManager,item_manager:ItemManager)->str:
    # 例外処理
    if user_manager.is_registered(user_name) == False:
        return f"update_price: {user_name} does not exist"
    
    if item_manager.is_listed(item_name) == False:
        return f"update_price: {item_name} does not exist"
    
    if new_price < 0:
        return f"update_price: {new_price} is invalid"
    
    if item_manager.items[item_name].seller != user_name:
        return f"update_price: {item_name} is not your own listing"
    
    if item_manager.items[item_name].is_sold == True:
        return f"update_price: {item_name} sold"
    
    # 価格変更処理
    item_manager.update_item_price(item_name,new_price)
    return f"update_price: {user_name} changed {item_name} price to {new_price}"