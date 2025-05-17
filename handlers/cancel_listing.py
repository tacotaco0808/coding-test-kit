from classes.item import ItemManager
from classes.user import UserManager


def handle_cancel_listing(timestamp:str,user_name:str,item_name:str,user_manager:UserManager,item_manager:ItemManager)->str:
    # 例外処理
    if user_manager.is_registered(user_name)==False:
        return f"cancel_listing: {user_name} does not exist"
    
    if item_manager.is_listed(item_name) == False:
        return f"cancel_listing: {item_name} does not exist"
    
    if item_manager.items[item_name].seller != user_name:
        return f"cancel_listing: {item_name} is not your own listing"
    
    if item_manager.items[item_name].is_sold == True:
        return f"cancel_listing: {item_name} sold"

    # 出品取りやめ
    item_manager.remove_item(item_name)

    return f"cancel_listing: {user_name} canceled {item_name}"