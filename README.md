# kitakyu_bot_frontend

GoogleのT5（Text-to-Text Transfer Transformer）を用いてLINEで受け取ったメッセージの文章分類を行う．

今回は北九州市立大学オープンキャンパス(2021年7月)に関する質問をカテゴリ毎に分類する。

## Features

### 全体像・フロントエンド部分

<img src="https://user-images.githubusercontent.com/86106572/129190936-a2394ae3-a25f-4ed4-a8df-ecdca36293ca.png" width=50%>

<img src="https://user-images.githubusercontent.com/86106572/129190945-31cdfb23-7404-46cd-885d-4c2f78bc422e.png" width=50%>

LINEとの送受信を可能とするためにLINE Messaging APIを用いる。

受信したメッセージをheroku上で受け取り、ngrokを用いて別ローカルサーバーに送信する。

別サーバーでメッセージの分類をし、その分類ラベルをherokuに返しそのラベルに応じた内容をLINEユーザー側に送信する。

## Requirement

- Python3.9.2

- transformers==4.4.2 変更しようね
- torch==1.7.1+cu110
- torchtext==0.8.0
- torchvision==0.8.2
- neologdn==0.5.1
- pydantic==1.8.2
- fastapi==0.68.0
- pytorch_lightning==1.2.1
- sentencepiece==0.1.96

## Installation

```bash
pip install -r requirements.txt
```

```bash
brew install ngrok
```

## Usage

1. `textdataset.txv`作成後，`T5_text_classification.ipynb'`を実行．
2. `オンライン予測WebAPI`ディレクトリに移動，`uvicorn main:app –reload`でAPIをLANに公開．
3. `ngrok http 8000`でWANに公開（Windowsの場合，`./ngrok http 8000`）．


## Note

`textdataset.tsv`は以下のようにする．

- [共同製作者(バックエンド)のリポジトリ](https://github.com/greentiger0789/AI_LINE_Bot_T5model)

### 紹介ポスター

<img src="https://user-images.githubusercontent.com/86106572/129190922-f74be94b-a714-42a6-8a39-dc3f753463b1.jpg" width=50%>

## Author
- [@IoriKobayashi1998](https://github.com/IoriKobayashi1998)

共同製作者
- [@greentiger0789](https://github.com/greentiger0789)
