from classes.user import UserManager


def handle_show_deposit_history(time_stamp:str,user_name:str,user_manager: UserManager)->str:
    if user_manager.is_registered(user_name) == False:
        return f"deposit_history: {user_name} does not exist"
    history = user_manager.get_history(user_name)
    message = f"{user_name}'s deposit_history:"

    # 型定義
    entry: dict[str,int|str]
    for index,entry in enumerate(history):
        if entry.get("action")=="deposit":
            amount = entry.get("amount",0)
            message += f"\n{index+1}: {amount}"

    return message

