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
5. views.pyを編集する(既成のviews.pyを使用)
6. Herokuにデプロイ

##### git初期化
```
git init
git add .
git commit -m 'first commit'
```
##### herokuにリポジトリを作成
```
heroku create
```
自動作成されたアプリ名を覚えておく。

##### 以下の設定を追加
```
heroku config:set DISABLE_COLLECTSTATIC=1
```
##### 次にsettings.pyを編集
```
ALLOWED_HOSTS = ['127.0.0.1', 'localhost', '「アプリ名」.herokuapp.com']
```
##### settings.pyをコミットする。
```
git add kitakyu_bot_github/settings.py
git commit -m "edit settings.py"
```
##### herokuにデプロイ
```
git push heroku master
```
7. LINE側にherokuのアドレスをセット

LINE Developersの方の「Webhook URL」に、herokuのbot/callbackのアドレスを追加。

8. 質問してみる

「トイレの場所はどこ？」「xxの講義時間」など。

## Note

#### vies.pyの編集において
- LINE DeveropersのアカウントからAccess Tokenを読み取りviews.pyの __ACCESS_TOKEN__ に入力
- 質問テキストから質問のカテコライズをするローカルサーバをngrokを用いて建て、そのngrok numberをviews.pyの __num_ngrok__ に入力

#### 共同製作者
バックエンド側（T5を用いたカテゴライズ）、ngrokの詳細は[共同制作者のリポジトリ](https://github.com/greentiger0789/AI_LINE_Bot_T5model)に公開している。

### 実装画面
<img src="https://user-images.githubusercontent.com/86106572/132164667-6a3bb055-6243-48af-ad1e-a9a816b15d2f.jpg" width=50%>

### 紹介ポスター
<img src="https://user-images.githubusercontent.com/86106572/129190922-f74be94b-a714-42a6-8a39-dc3f753463b1.jpg" width=50%>

## Author
- [@IoriKobayashi1998](https://github.com/IoriKobayashi1998)

__共同製作者__
- [@greentiger0789](https://github.com/greentiger0789)
