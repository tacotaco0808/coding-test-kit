# CUIショッピングサイト

## 機能

入力は標準入力から行われる。

複数のエラーの場合は表記の上順から最初に該当するエラーを出力する。

タイムスタンプの形式は `[YYYY-MM-DD]T[hh:mm:ss]` 形式である。

例 `2025-03-05T12:00:00`

入力ファイルの形式は以下のとおりである。

```
N  // 行数
COMMAND_1  // N個の命令（機能）
COMMAND_2
...
COMMAND_N
```

## 基本機能

### ユーザ登録

ユーザを登録する機能。

**入力**

`タイムスタンプ registor {UserName} {Balance}`

**出力**

`registor: {UserName} {Balance}`

**エラー**

- ユーザが登録済み

`registor: {UserName} はすでに登録されています`

- 金額が0未満

`registor: {Balance} 指定された金額は不正です`

### 入金

ユーザが入金する機能。

**入力**

`タイムスタンプ add_balance {UserName} {Balance}`

**出力**

`add_balance: {UserName} {OldBalance} -> {NewBalance}`

**エラー**

- ユーザが存在しない

`add_balance: {UserName} is not exists`

- 金額が0未満

`add_balance: {Balance} 指定された金額は不正です`

### 残高確認

ユーザが残高確認する機能。

**入力**

`タイムスタンプ show_balance {UserName}`

**出力**

`show_balance: {UserName} 残高 {Balance}`

**エラー**

- ユーザが存在しない

`show_balance: {UserName} は存在しません`

### 出品

ユーザが出品する機能。

**入力**

`タイムスタンプ sell {UserName} {ItemName} {Price}`

**出力**

`sell: {UserName} が {ItemName} を {Price} で販売`

**エラー**

- ユーザが存在しない

`show_balance: {UserName} は存在しません`

- 金額が0未満

`show_balance: {Price} 指定された金額は不正です`

### 商品一覧表示

商品一覧を出品されたタイムスタンプ順に表示する機能。何も出品されていない場合は１行目のみを表示する。すでに購入されている商品は表示しない。

**入力**

`タイムスタンプ show_items`

**出力**

```
show_items:
1: {ItemName} {Price} {Seller}
2: {ItemName} {Price} {Seller}
```

**エラー**

なし

### 商品購入

ユーザが商品を購入する機能。

**入力**

`タイムスタンプ purchase {UserName} {ItemName}`

**出力**

`purchase: {ItemName} を購入`

**エラー**

- ユーザが存在しない

`purchase: {UserName} は存在しません`

- 商品が存在しない

`purchase: {ItemName} は存在しません`

- 自分が出品している商品を購入しようとした

`purchase: {ItemName} は自分の商品です`

- 残高が不足している

`purchase: {UserName} の残高が不足しています`

## 応用機能

### 出品済商品一覧表示

ユーザが出品した商品の一覧表示機能。ユーザが何も出品していない場合は１枚目のみ表示する。

**入力**

`タイムスタンプ sell_items {UserName}`

**出力**

```
sell_items:
1: {ItemName} {Price}
2: {ItemName} {Price}
```

**エラー**

- ユーザが存在しない

`sell_items: {UserName} は存在しません`

### 購入済商品一覧表示

ユーザの購入済み商品の一覧表示機能。

**入力**

`タイムスタンプ purchased_items {UserName}`

**出力**

```
purchased_items:
1: {ItemName} {Price}
2: {ItemName} {Price}
```

**エラー**

- ユーザが存在しない

`purchased_items: {UserName} は存在しません`

### 販売履歴表示

ユーザが販売した（購入された）商品の履歴表示機能。

**入力**

`タイムスタンプ sold_items {UserName}`

**出力**

```
sold_items:
1: {ItemName} {Price}
2: {ItemName} {Price}
```

**エラー**

- ユーザが存在しない

`sold_items: {UserName} は存在しません`

### 入金履歴表示

ユーザの入金履歴表示機能。

**入力**

`タイムスタンプ deposit_history {UserName}`

**出力**

```
deposit_history:
1: {Balance}
2: {Balance}
```

**エラー**

- ユーザが存在しない

`deposit_history: {UserName} は存在しません`

### 出品取りやめ
