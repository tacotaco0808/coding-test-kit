from classes.user import UserManager


def handle_show_sold_items(timestamp:str,user_name:str,user_manager:UserManager)->str:
    if user_manager.is_registered(user_name)==False:
        return f"sold_items: {user_name} does not exist"
    message = f"{user_name}'s sold_items:"
    entry: dict[str,str|int]
    for index,entry in enumerate(user_manager.get_sold_items(user_name)):
        item_name = entry.get("item_name","")
        price = entry.get("amount",0)
        message += f"\n{index+1}: {item_name} {price}"
        
    return message