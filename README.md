# Google Vision API with python.

## VisionAPIの有効化.
https://cloud.google.com/vision/docs/before-you-begin

## クレデンシャルの取得.
Get Service Account Key from:  
https://cloud.google.com/vision/docs/libraries#installing_the_client_library  
then, save to `./my-sevice-account-key.json`

## 対象バージョン.
Python3.6+

## モジュールのインストール.
```
pip3 install --upgrade google-cloud-vision
```

## 実行.
```
python3 sample.py
```

## 参照リンク.
- [顔検出のチュートリアル](https://cloud.google.com/vision/docs/face-tutorial)
- [Vision API Client Libraries](https://cloud.google.com/vision/docs/libraries#installing_the_client_library)
- [API Reference](https://google-cloud-python.readthedocs.io/en/latest/vision/index.html)
- [API Reference(enum)](https://cloud.google.com/vision/docs/reference/rest/v1/images/annotate)
