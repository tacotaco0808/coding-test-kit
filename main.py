import sys


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


class TestUser:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        self.purchased_items = []
        self.sell_items = []
        self.balance_log = []

    def add_purchased_item(self, item):
        self.balance -= int(item["price"])
        self.purchased_items.append((item["item"], item["price"], item["seller"]))

    def add_sell_item(self, item):
        self.sell_items.append(item)

    def add_balance(self, balance):
        self.balance += int(balance)
        self.balance_log.append(balance)


class Test():
    def __init__(self):
        self.users = {}
        self.items = []

    def dummy(self, *args):
        return ""

    def registor(self, *args):
        name, balance = args
        user = TestUser(name, int(balance))
        if self.users.get(name):
            return f"registor: {name} already exists"
        if int(balance) < 0:
            return f"registor: {balance} is illigal"
        self.users[name] = user
        return f"registor: {name} {balance}"

    def add_balance(self, *args):
        name, balance = args
        user: TestUser = self.users.get(name)
        if not user:
            return f"add_balance: {name} is not exists"
        if int(balance) < 0:
            return f"add_balance: {balance} is illigal"
        user.add_balance(balance)
        return f"add_balance: {name} {user.balance - int(balance)} -> {user.balance}"

    def show_balance(self, *args):
        name, *_ = args
        user: TestUser = self.users.get(name)
        if not user:
            return f"show_balance: {name} is not exists"
        return f"show_balance: {name}'s balance {user.balance}"

    def sell(self, *args):
        username, itemname, price = args
        user: TestUser = self.users.get(username)
        self.items.append({"item": itemname, "price": price, "seller": username})
        user.add_sell_item({"item": itemname, "price": price, "seller": username})
        if not user:
            return f"sell: {username} is not exists"
        if int(price) < 0:
            return f"sell: {price} is illigal"
        return f"sell: {username} {itemname} {price}"

    def show_items(self, *args):
        result = ["show_items:"]
        for i, iteminfo in enumerate(self.items, 1):
            result.append(f"{i}: {iteminfo['item']} {iteminfo['price']} {iteminfo['seller']}")
        return "\n".join(result)

    def purchase(self, *args):
        name, itemname = args
        user: TestUser = self.users.get(name)
        if not user:
            return f"purchase: {name} is not exists"
        for i, item in enumerate(self.items[:], 0):
            if item["item"] == itemname and user.balance >= int(item["price"]):
                self.items.pop(i)
                user.add_purchased_item(item)
                seller: TestUser = self.users.get(item["seller"])
                if seller:
                    seller.balance += int(item["price"])
        return f"purchase: {itemname}"

    def sell_items(self, *args):
        name, *args = args
        user: TestUser = self.users.get(name)
        if not user:
            return f"sell_items: {name} is not exists"
        result = [f"{name}'s sell_items:"]
        for i, item in enumerate(self.items, 1):
            if item['seller'] == user.name:
                result.append(f"{i}: {item['item']} {item['price']}")
        return "\n".join(result)

    def purchased_items(self, *args):
        name, *_ = args
        user: TestUser = self.users.get(name)
        if not user:
            return f"purchased_items: {name} is not exists"
        result = [f"{name}'s purchased_items:"]
        for i, item in enumerate(user.purchased_items, 1):
            result.append(f"{i}: {item[0]} {item[1]}")
        return "\n".join(result)

    def sold_items(self, *args):
        name, *_ = args
        user: TestUser = self.users.get(name)
        if not user:
            return f"sold_items: {name} is not exists"
        u: TestUser
        result = [f"{name}'s sold_items:"]
        for u in self.users.values():
            count = 0
            for item in u.purchased_items:
                if user.name == item[2]:
                    count += 1
                    result.append(f"{count}: {item[0]} {item[1]}")
        return "\n".join(result)

    def deposit_history(self, *args):
        name, *_ = args
        user: TestUser = self.users.get(name)
        if not user:
            return f"deposit_history: {name} is not exists"
        result = [f"{user.name}'s deposit_history:"]
        for i, log in enumerate(user.balance_log, 1):
            result.append(f"{i}: {log}")
        return "\n".join(result)

class Mapper():
    def __new__(cls):
        test = Test()
        cls.commands = {
            "registor": test.registor,
            "add_balance": test.add_balance,
            "show_balance": test.show_balance,
            "sell": test.sell,
            "show_items": test.show_items,
            "purchase": test.purchase,
            "sell_items": test.sell_items,
            "purchased_items": test.purchased_items,
            "sold_items": test.sold_items,
            "deposit_history": test.deposit_history,
        }
        return cls


if __name__ == "__main__":
    mapper = Mapper()
    command_list = mapper.commands
    for line in readlines():
        timestamp, command, *args = line.split()
        result = command_list.get(command, lambda x: len(x))(*args)
        print(result)
