from classes.user import UserManager


def handle_deposit(timestamp: str,user_name: str, amount: int, user_manager: UserManager):

    # 例外処理
    if user_manager.is_registered(user_name)== False:
        return f"deposit: {user_name} does not exist"
    if amount < 0:
        return f"deposit: {amount} is invalid"
    
    # 正常に入金する場合
    old_balance = user_manager.users[user_name].get_balance()
    new_balance = user_manager.users[user_name].deposit(amount)
    return f"deposit: {user_name} {old_balance} -> {new_balance}"