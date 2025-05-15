from classes.user import UserManager


def handle_show_balance(timestamp: str,user_name: str,user_manager: UserManager)-> str:
    # 例外処理
    if(user_manager.is_registered(user_name)==False):
        return f"show_balance: {user_name} does not exist"
    # ユーザーの残高を取得
    balance = user_manager.users[user_name].get_balance()
    return f"show_balance: {user_name}'s balance {balance}"