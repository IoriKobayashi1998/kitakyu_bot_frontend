# kitakyu_bot_frontend

GoogleのT5（Text-to-Text Transfer Transformer）を用いてLINEで受け取ったメッセージの文章分類を行う。

今回は北九州市立大学オープンキャンパス(2021年7月)に関する質問をカテゴリ毎に分類する。

## Features

### 全体像・フロントエンド部分

<img src="https://user-images.githubusercontent.com/86106572/129190936-a2394ae3-a25f-4ed4-a8df-ecdca36293ca.png" width=50%>

<img src="https://user-images.githubusercontent.com/86106572/129190945-31cdfb23-7404-46cd-885d-4c2f78bc422e.png" width=50%>

LINEとの送受信を可能とするためにLINE Messaging APIを用いる。

受信したメッセージをheroku上で受け取り、ngrokを用いて別ローカルサーバーに送信する。

別サーバーでメッセージの分類をし、その分類ラベルをherokuに返しそのラベルに応じた内容をLINEユーザー側に送信する。

## Requirement

- Python3.9.5

- dj_database_url==0.5.0
- line_bot_sdk==1.19.0
- Django==3.2.4

## Installation

```bash
pip install -r requirements.txt
```

## Usage
[Django+HerokuでLINE Messaging APIのおそ松botを作るまで](https://qiita.com/yakan10/items/b7ad35c2cbba5db81462)を参考にさせてもらって作成した。以下で示す手順はこの参考ページと共に見ていただくことを想定している。
0. Herokuアカウント作成
1. LINE Messaging API登録
2. Installation(requirements.txt)
3. Djangoプロジェクト作成
```bash
django-admin startproject kitakyu_bot_github
```
4. Djangoでbotアプリケーション作成
```bash
python manage.py startapp bot
```
5. d
6.  

## Note

`textdataset.tsv`は以下のようにする．



バックエンド側（T5を用いたカテゴライズ）、ngrokの詳細は[共同制作者のリポジトリ](https://github.com/greentiger0789/AI_LINE_Bot_T5model)に公開している。

### 紹介ポスター

<img src="https://user-images.githubusercontent.com/86106572/129190922-f74be94b-a714-42a6-8a39-dc3f753463b1.jpg" width=50%>


## Author
- [@IoriKobayashi1998](https://github.com/IoriKobayashi1998)

共同製作者
- [@greentiger0789](https://github.com/greentiger0789)
