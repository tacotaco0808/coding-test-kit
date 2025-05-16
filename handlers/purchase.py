from classes.item import ItemManager
from classes.user import UserManager


def handle_purchase(timestamp: str,user_name:str,item_name:str,user_manager: UserManager,item_manager: ItemManager)->str:
    if user_manager.is_registered(user_name) == False:
        return f"purchase: {user_name} does not exist"
    if item_manager.is_listed(item_name) == False:
        return f"purchase: {item_name} does not exist"
    if item_manager.items[item_name].seller == user_name:
        return f"purchase: {item_name} is your own listing"
    if item_manager.items[item_name].price > user_manager.users[user_name].balance:
        return f"purchase: {user_name} does not have enough balance"

    return f"purchase: {user_name} bought {item_name}"