from classes.item import ItemManager


def handle_show_items(timestamp:str,item_manager:ItemManager)->str:
    message = f"show_items:\n"
    for index,item in enumerate(item_manager.get_items()):
        message += f"{index+1}: {item.item_name} {item.price} {item.seller}\n"
    return message
