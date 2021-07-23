# -*- encoding: utf-8 -*-
from django.http.response import HttpResponse
import json
import re
import urllib
import urllib.parse
import urllib.request

from linebot import LineBotApi
from linebot.models import TextSendMessage
from linebot.models import ImageSendMessage

REPLY_ENDPOINT = 'https://api.line.me/v2/bot/message/reply'
ACCESS_TOKEN = '' # Your access token
HEADER = {
    "Authorization": "Bearer " + ACCESS_TOKEN
}

# Create your views here.
def index(request): # httpで確認する用
    return HttpResponse("This is bot api.")

def callback(request):
    http_response = "Calling callback"
    request_json = json.loads(request.body.decode('utf-8'))  # requestの情報をdict形式で取得
    line_api = LineBotApi(ACCESS_TOKEN)

    # 受け取ったJSONファイルの読み取り(LINE Messaging APIから)
    for e in request_json['events']:
        message_type = e['message']['type']   # typeの取得
        user_id = e['source']['userId']

        if message_type == 'text':
            text_Line = e['message']['text']    # 受信メッセージの取得

    # ローカルサーバ連携・送信JSONファイルの作成
    num_ngrok = "" # Your ngrok number
    url_local = "http://" + num_ngrok + ".ngrok.io/prediction/online"
    jsonData_Line = {
        "data": [
            {
                "text": text_Line
            }
        ]
    }
    headers={
        'Content-Type': 'application/json',
        'accept': 'application/json'
        }
    
    # LINEから受け取ったテキスト(JSONファイル)のローカルサーバへの送信
    req = urllib.request.Request(url_local, json.dumps(jsonData_Line).encode('utf-8'), headers)
    with urllib.request.urlopen(req) as res:
        #受け取ったJSONファイルの読み取り(ローカルサーバから)
        body = res.read()
        deco_body=body.decode('utf-8')
        label = re.sub(r"\D", "", deco_body)

    # 推定ラベルによる条件文
    if label == '0': # 0 イベントスケジュール画像の表示
        url_img='https://drive.google.com/uc?id=1IuRTuQ6z3cE9JOKFqh0Px8EHNIQOxsBT'
        reply_label = "イベントの時間と教室がわかるスケジュール表を送信しますね！\n\n場所が分からないときは\n構内マップが見たい！と聞いてね！"
    elif label == '1': # 1 エリアマップの表示
        url_img='https://drive.google.com/uc?id=1eZhe46vD0aSwkT2BAAxbvYB3sLXNyEZc'
        reply_label = "キャンパス周辺の地図を表示しますね！"
    elif label == '2': # 2 構内地図と企画実施場所画像の表示
        url_img='https://drive.google.com/uc?id=1WRHQ4EahR6pyTOeYkM8KIWPlSPQFRxxv'
        reply_label = "構内の地図を表示します！\nイベントや講義がどこで行われているかもわかるよ！"
    elif label == '3': # 3 バス案内画像の表示
        url_img='https://drive.google.com/uc?export=view&id=1sehd8zDA33e8YJ8Moenfjt3cqSfh0oH0'
        reply_label = "折尾駅と大学を結ぶバスの時刻表を送ります！\nバスの運賃は230円です！\n安全に移動しましょう！"
    elif label == '4': # 4 感染症対策の情報表示
        reply_label = "このオープンキャンパスではこのような感染症対策を\n行っているよ！\n① 体調のすぐれない方は、ご来場をお控えください。\n② 本学HPからダウンロードした健康チェックシート.docxに必要事項を記載の上、必ずご持参ください。\n③ 必ずマスクの着用をお願いします。（フェイスシールドやマウスシールドのみは不可。）\n鼻と口を確実に覆い、隙間がないように顎まで覆い、正しいマスクの着用をお願いします。\n④ 会場入館時や各教室の入退室の際など、こまめに手指消毒をお願いします。\n⑤ 会場内では、大声での私語はお控えください。\n⑥ 入館などで並ぶ際には、必ず前後１ｍ程度の距離を保ってください。\n⑦ 教室の座席は、ソーシャルディスタンスのため座れない席があります。\n「×」印のある座席には着席しないでください。\n\nみんなで感染症を防ぎましょう！"
    elif label == '5': # 5 開場時間,入館方法に関する情報表示
        reply_label = "開催時間は\n午前の部　10:00~12:30\n午後の部　13:30~16:00\n受付は開催時間のそれぞれ30分前からです！\n\n受付場所はN棟1階入り口！\n場所が分らないときは\n受付場所はどこ？ってわたしに聞いてね♪"
    elif label == '6': # 6 飲食に関する情報表示
        reply_label = "食事できる場所は感染症対策のため閉館しています。。。\n飲み物は大丈夫だよ！\n休憩場所は2階情報ギャラリーを使ってね！\n自動販売機もあるよ！"
    
    # LINEへの送信部 label=0~3までは画像・テキスト送信
    if label == '0' or label == '1' or label == '2' or label == '3':
        image_message = ImageSendMessage(
            original_content_url=url_img,
            preview_image_url=url_img
        )
        line_api.push_message(user_id,TextSendMessage(text=reply_label))
        line_api.push_message(user_id,image_message)
    elif label == '4' or label == '5' or label == '6':
        line_api.push_message(user_id,TextSendMessage(text=reply_label))

    return HttpResponse(http_response)  # テスト用