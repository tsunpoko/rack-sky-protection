import os
import time
import tweepy
import random
####
import config

CONSUMER_KEY = CONSUMER_SECRET = ACCESS_TOKEN = ACCESS_TOKEN_SECRET = ''
DIR_NAME = "/var/lib/motion/"
#DIR_NAME = "./tmp/"

def postTweet(image_path):
    print("[+] postTweet() is called")
    print(image_path)

    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

    api = tweepy.API(auth)

    #image_path = "./tmp/output.gif"

    # mkv to gif
    image_path_gif = image_path.replace("mkv", "gif")

    os.system("ffmpeg -i " + image_path + " -r 10 " + image_path_gif)

    text_list = [
    "沖縄高専 光輝け",
    "しんどすぎて振動するオタク",
    "陰スタグラム",
    "えん（；＿；）",
    "にんにん",
    "草オブ草",
    "自我を保てないんよ\n#自我の崩壊",
    "skrr skrr",
    "ストロングゼロで流しそうめんせん？",
    "はやく退学したい",
    "夏にはチンポポの花が咲くんよ",
    #"突然2億円の借金を背負って死ぬ",
    "今日も一日",
    "はやくこれになりたい",
    "男女の友情は成立しません",
    "順吉が実は童貞ではないという事実、家系ラーメンより好き",
    "職業 : へのじい",
    "「chill」って言葉と共にストーリー投稿しておけばインスタグラマーっぽい",
    "オタク息しとる？",
    "お願い🙏シンデレラ👠夢は夢で終われない👊動き始めてる🏃輝く日のために✨ウリャ！オイ！ウリャ！オイ！ウリャ！オイ！ウリャ！オイ！ ア～～～ッシャアイグゾー！！🙋ピノキオ！👺プーさん！🐻ミッキー！🐭スティッチ！👽バンビ！👶ドナルド！🐧シンデレラー！👗",
    "やば❗笑 田所のツイートめっちゃ伸びてるやん！学校では陰キャなのにTwitterでは人気なんやな笑 また学校来いよ❔✊ みんなで遊ぼうぜ😁👊",
    "ぽなかしゅいた...",
    "ダメです",
    "このアカウントが橋本環奈の裏アカということがバレるのも時間の問題だな...",
    "#安倍政権を許すな",
    ".@YouWatanabeEins"
    ]

    api.update_with_media(filename = image_path_gif, status = text_list[random.randint(0, len(text_list) - 1)])
    #api.update_status(status = text)

    ls =  os.listdir(DIR_NAME)

    if len(ls) > 0:
        for i in ls:
            os.remove(DIR_NAME + i)

def detect():
    print("[+] detect() is called.")

    ls =  os.listdir(DIR_NAME)

    if len(ls) != 1:
        return

    postTweet(DIR_NAME + ls[0])

if __name__ == "__main__":

    # initialize
    CONSUMER_KEY = config.CONSUMER_KEY
    CONSUMER_SECRET = config.CONSUMER_SECRET
    ACCESS_TOKEN = config.ACCESS_TOKEN
    ACCESS_TOKEN_SECRET = config.ACCESS_TOKEN_SECRET

    ls =  os.listdir(DIR_NAME)

    if len(ls) > 0:
        for i in ls:
            os.remove(DIR_NAME + i)

    print("[+] Initialized!")


    while True:
        detect()
        time.sleep(3)
        #time.sleep(30)
