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


if __name__ == "__main__":
    for line in readlines():
        print(line)
