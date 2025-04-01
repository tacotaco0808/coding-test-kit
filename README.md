# CUIショッピングサイト
目次
1. [仕様](#仕様)
1. [基本機能](#基本機能)
1. [応用機能](#応用機能)

## 仕様

* 入力は標準入力から受け取る。
* エラーが複数発生した場合は、エラーテーブルの上にあるものを優先して1つだけ出力する。
* タイムスタンプの形式は [YYYY-MM-DD]T[hh:mm:ss]。
  * 例: 2025-03-05T12:00:00
* 入力ファイルの形式は以下のとおり。

```
N  // 行数
COMMAND_1  // N個の命令（機能）
COMMAND_2
...
COMMAND_N
```

## 基本機能
1. [トップ](#cuiショッピングサイト)
1. [ユーザ登録](#ユーザ登録)
1. [入金](#入金)
1. [残高確認](#残高確認)
1. [出品](#出品)
1. [商品一覧表示](#商品一覧表示)
1. [商品購入](#商品購入)
1. [売上確認](#売上確認)
1. [応用機能](#応用機能)

### ユーザ登録

**入力**

`{timestamp} register {user_name} {balance}`

**出力**

`register: {user_name} {balance}`

**エラー**

|条件|表示項目|
|:--:|:--:|
|ユーザがすでに登録済み|`register: {user_name} is already registered`|
|金額が負の値|`register: {balance} is invalid`|

### 入金

**入力**

`{timestamp} deposit {user_name} {amount}`

**出力**

`deposit: {user_name} {old_balance} -> {new_balance}`

**エラー**

|条件|表示項目|
|:--:|:--:|
|ユーザが存在しない|`deposit: {user_name} does not exist`|
|金額が負の値|`deposit: {amount} is invalid`|

### 残高確認

**入力**

`{timestamp} show_balance {user_name}`

**出力**

`show_balance: {user_name}'s balance {balance}`

**エラー**

|条件|表示項目|
|:--:|:--:|
|ユーザが存在しない|`show_balance: {user_name} does not exist`|

### 出品

**入力**

`{timestamp} sell {user_name} {item_name} {price}`

**出力**

`sell: {user_name} listed {item_name} for {price}`

**エラー**

|条件|表示項目|
|:--:|:--:|
|ユーザが存在しない|`sell: {user_name} does not exist`|
|すでに商品が登録済み|`sell: {item_name} is already listed`|
|金額が負の値|`sell: {price} is invalid`|

### 商品一覧表示

**入力**

`{timestamp} show_items`

**出力**

```
show_items:
1: {item_name} {price} {seller}
2: {item_name} {price} {seller}
...
```

**エラー**

なし

### 商品購入

**入力**

`{timestamp} purchase {user_name} {item_name}`

**出力**

`purchase: {user_name} bought {item_name}`

**エラー**

|条件|表示項目|
|:--:|:--:|
|ユーザが存在しない|`purchase: {user_name} does not exist`|
|商品が存在しない|`purchase: {item_name} does not exist`|
|自分が出品した商品を購入しようとした|`purchase: {item_name} is your own listing`|
|残高不足|`purchase: {user_name} does not have enough balance`|

### 売上確認

**入力**

`{timestamp} show_sales {user_name}`

**出力**

`show_sales: {user_name}'s total sales {total_sales}`

**エラー**

|条件|表示項目|
|:--:|:--:|
|ユーザが存在しない|`show_sales: {user_name} does not exist`|

## 応用機能
1. [トップ](#cuiショッピングサイト)
1. [基本機能](#基本機能)
1. [入金履歴表示](#入金履歴表示)
1. [出品履歴表示](#出品履歴表示)
1. [価格変更](#価格変更)
1. [出品取りやめ](#出品取りやめ)
1. [購入履歴表示](#購入履歴表示)
1. [商品検索](#商品検索)

### 入金履歴表示

**入力**

`タイムスタンプ deposit_history {user_name}`

**出力**

```
{user_name}'s deposit_history:
1: {amount}
2: {amount}
...
```

**エラー**

|条件|表示項目|
|:--:|:--:|
|ユーザが存在しない|`deposit_history: {user_name} does not exist`|

### 出品履歴表示

**入力**

`{timestamp} sold_items {user_name}`

**出力**

```
{user_name}'s sold_items:
1: {item_name} {price}
2: {item_name} {price}
...
```

**エラー**

|条件|表示項目|
|:--:|:--:|
|ユーザが存在しない|`sold_items: {user_name} does not exist`|

### 価格変更

**入力**

`{timestamp} update_price {user_name} {item_name} {new_price}`

**出力**

`update_price: {user_name} changed {item_name} price to {new_price}`

**エラー**

|条件|表示項目|
|:--:|:--:|
|ユーザが存在しない|`update_price: {user_name} does not exist`|
|商品が存在しない|`update_price: {item_name} does not exist`|
|金額が負の値|`update_price: {amount} is invalid`|
|自分の商品でない|`update_price: {item_name} is not your own listing`|
|すでに販売済み|`update_price: {item_name} sold`|

### 出品取りやめ

**入力**

`{timestamp} cancel_listing {user_name} {item_name}`

**出力**

`cancel_listing: {user_name} canceled {item_name}`

**エラー**

|条件|表示項目|
|:--:|:--:|
|ユーザが存在しない|`cancel_listing: {user_name} does not exist`|
|商品が存在しない|`cancel_listing: {item_name} does not exist`|
|自分の商品でない|`cancel_listing: {item_name} is not your own listing`|
|すでに販売済み|`cancel_listing: {item_name} sold`|

### 購入履歴表示

**入力**

`{timestamp} purchased_items {user_name}`

**出力**

```
{user_name}'s purchased_items:
1: {item_name} {price}
2: {item_name} {price}
...
```

**エラー**

|条件|表示項目|
|:--:|:--:|
|ユーザが存在しない|`purchased_items: {user_name} does not exist`|

### 商品検索

**入力**

`{timestamp} search_item {keyword}`

**出力**

```
search_item:
1: {item_name} {price} {seller}
2: {item_name} {price} {seller}
...
```

**エラー**

なし
