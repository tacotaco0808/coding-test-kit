from classes.user import UserManager


def handle_show_sales(timestamp:str,user_name:str,user_manager:UserManager)->str:
    if user_manager.is_registered(user_name)== False:
        return f"show_sales: {user_name} does not exist"
    total_sales = user_manager.users[user_name].sales
    return f"show_sales: {user_name}'s total sales {total_sales}"
