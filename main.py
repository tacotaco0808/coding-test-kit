import sys

from classes.item import ItemManager
from classes.user import UserManager
from handlers.cancel_listing import handle_cancel_listing
from handlers.deposit import handle_deposit
from handlers.purchase import handle_purchase
from handlers.purchased_items import handle_purchased_items
from handlers.register import handle_register
from handlers.sell import handle_sell
from handlers.show_balance import handle_show_balance
from handlers.show_deposit_history import handle_show_deposit_history
from handlers.show_items import handle_show_items
from handlers.show_sales import handle_show_sales
from handlers.show_sold_items import handle_show_sold_items
from handlers.update_price import handle_update_price


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
            print(f"{output}")

        elif command == "deposit":
            user_name = args[0]
            ammount = int(args[1])
            output = handle_deposit(timestamp, user_name, ammount, user_manager)
            print(f"{output}")

        elif command == "show_balance":
            user_name = args[0]
            output = handle_show_balance(timestamp,user_name,user_manager)
            print(f"{output}")
        
        elif command == "sell":
            user_name = args[0]
            item_name = args[1]
            price = int(args[2])
            output = handle_sell(timestamp, user_name, item_name, price, user_manager, item_manager)
            print(f"{output}")
        
        elif command == "show_items":
            output = handle_show_items(timestamp,item_manager)
            print(f"{output}")

        elif command == "purchase":
            user_name = args[0]
            item_name = args[1]
            output = handle_purchase(timestamp,user_name,item_name,user_manager,item_manager)
            print(f"{output}")

        elif command == "show_sales":
            user_name = args[0]
            output = handle_show_sales(timestamp,user_name,user_manager)
            print(f"{output}")

        elif command == "deposit_history":
            user_name = args[0]
            output = handle_show_deposit_history(timestamp,user_name,user_manager)
            print(f"{output}")

        elif command == "sold_items":
            user_name = args[0]
            output = handle_show_sold_items(timestamp,user_name,user_manager)
            print(f"{output}")
        
        elif command == "update_price":
            user_name = args[0]
            item_name = args[1]
            new_price = int(args[2])
            output = handle_update_price(timestamp,user_name,item_name,new_price,user_manager,item_manager)
            print(f"{output}")

        elif command == "cancel_listing":
            user_name = args[0]
            item_name = args[1]
            output = handle_cancel_listing(timestamp,user_name,item_name,user_manager,item_manager)
            print(f"{output}")

        elif command == "purchased_items":
            user_name = args[0]
            output = handle_purchased_items(timestamp,user_name,user_manager)
            print(f"{output}")
        
        else:
            print(f"Unknown command: {command}")
        

