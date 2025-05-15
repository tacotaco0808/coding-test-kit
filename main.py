import sys

from classes.item import ItemManager
from classes.user import UserManager
from handlers.deposit import handle_deposit
from handlers.register import handle_register
from handlers.sell import handle_sell
from handlers.show_balance import handle_show_balance


def readlines() -> list[str]:
    """標準入力を受け付ける関数

    Raises:
        ValueError: 標準入力の１行目が数値以外のとき送出される
        Exception: 標準入力の読み込み時にエラーが発生したとき送出される

    Returns:
        list[str]: 標準入力から受け取った文字列のリスト
    """
    try:
        N = int(sys.stdin.readline())
        read_lines = []
        for _ in range(N):
            read_lines.append(sys.stdin.readline())
        return read_lines
    except ValueError as e:
        raise e
    except Exception as e:
        raise e


if __name__ == "__main__":
    
    # ユーザを管理するインスタンス
    user_manager = UserManager()
    # アイテムを管理するインスタンス
    item_manager = ItemManager()

    # for n,line in enumerate(readlines()):
    #     print(f"{n}:{line}")
    
    for line in readlines():
        # args以降はそれぞれのコマンドに応じて処理する
        timestamp, command, *args = line.split()
        if command == "register":
            user_name = args[0]
            balance = int(args[1])
            output = handle_register(timestamp, user_name, balance, user_manager)
            print(f"register:{output}")

        elif command == "deposit":
            user_name = args[0]
            ammount = int(args[1])
            output = handle_deposit(timestamp, user_name, ammount, user_manager)
            print(f"deposit:{output}")

        elif command == "show_balance":
            user_name = args[0]
            output = handle_show_balance(timestamp,user_name,user_manager)
            print(f"show_balance:{output}")
        
        elif command == "sell":
            user_name = args[0]
            item_name = args[1]
            price = int(args[2])
            output = handle_sell(timestamp, user_name, item_name, price, user_manager, item_manager)
            print(f"sell:{output}")

        else:
            print(f"Unknown command: {command}")
        

    user_manager.show_users()
