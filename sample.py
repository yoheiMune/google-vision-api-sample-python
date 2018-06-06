"""
    A sample for detect face images with Google Vision Api.
"""
import os

# Imports the Google Cloud client library
from google.cloud import vision
from google.cloud.vision import types

# 環境変数に、Googleのサービスアカウントキーへのパスを設定.
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "./my-sevice-account-key.json"

# 画像読み込み.
with open("./face1.jpg", "rb") as f:
    image = f.read()

# GCPクライアントを作成.
client = vision.ImageAnnotatorClient()

# Vision API を実行.
response = client.face_detection(image=types.Image(content=image))
# print(response)

# 笑顔判定結果を取得.
joy_likelihood = response.face_annotations[0].joy_likelihood
print("joy_likelihood:", joy_likelihood)
if joy_likelihood >= 3:  # 3:Possible, 4:Likely, 5:VeryLikely
    print('笑顔です！')
else:
    print("笑顔じゃない.")
