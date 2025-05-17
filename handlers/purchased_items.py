from classes.item import ItemManager
from classes.user import UserManager


def handle_purchased_items(timestamp:str,user_name:str,user_manager:UserManager)->str:
    if user_manager.is_registered(user_name) == False:
        return f"purchased_items: {user_name} does not exist"
    
    message = f"{user_name}'s purchased_items:"
    # 型定義
    entry: dict[str,str|int]
    for index,entry in enumerate(user_manager.get_purchased_item_from_user(user_name)):
        item_name = str(entry.get("item_name",""))
        price = entry.get("amount",0)
        message += f"\n{index+1}: {item_name} {price}"
        


    return message
