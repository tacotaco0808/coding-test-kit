from classes.user import UserManager


def handle_register(timestamp: str,user_name: str,balance: int, user_manager: UserManager) -> str:
    """ユーザの登録を行う関数
    parameters:
        timestamp (str): タイムスタンプ (形式[YYYY-MM-DD]T[hh:mm:ss])
        user_name (str): ユーザ名
        balance (int): ユーザの初期残高

    Returns:
        str: 結果メッセージ
    """

    # 例外処理
    if balance <0:
        return f"register: {balance} is invalid"

    if user_manager.is_registered(user_name):
        return f"register: {user_name} is already registered"
    
    
    #　正常にユーザーを登録する場合
    user_manager.add_user(user_name, balance)
    return f"register: {user_name} {balance}"