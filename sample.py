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


""" Full Response.

face_annotations {
  bounding_poly {
    vertices {
      x: 118
    }
    vertices {
      x: 722
    }
    vertices {
      x: 722
      y: 545
    }
    vertices {
      x: 118
      y: 545
    }
  }
  fd_bounding_poly {
    vertices {
      x: 214
      y: 24
    }
    vertices {
      x: 667
      y: 24
    }
    vertices {
      x: 667
      y: 477
    }
    vertices {
      x: 214
      y: 477
    }
  }
  landmarks {
    type: LEFT_EYE
    position {
      x: 373.78289794921875
      y: 172.21920776367188
      z: 0.0023655928671360016
    }
  }
  landmarks {
    type: RIGHT_EYE
    position {
      x: 546.8156127929688
      y: 158.1598358154297
      z: 48.51563262939453
    }
  }
  landmarks {
    type: LEFT_OF_LEFT_EYEBROW
    position {
      x: 307.3804626464844
      y: 140.09153747558594
      z: -1.3121565580368042
    }
  }
  landmarks {
    type: RIGHT_OF_LEFT_EYEBROW
    position {
      x: 430.2786865234375
      y: 129.4232635498047
      z: -24.052600860595703
    }
  }
  landmarks {
    type: LEFT_OF_RIGHT_EYEBROW
    position {
      x: 511.93133544921875
      y: 123.91395568847656
      z: -0.10662923753261566
    }
  }
  landmarks {
    type: RIGHT_OF_RIGHT_EYEBROW
    position {
      x: 602.7743530273438
      y: 112.3797607421875
      z: 79.63102722167969
    }
  }
  landmarks {
    type: MIDPOINT_BETWEEN_EYES
    position {
      x: 476.9587707519531
      y: 162.73968505859375
      z: -12.48060131072998
    }
  }
  landmarks {
    type: NOSE_TIP
    position {
      x: 495.8747863769531
      y: 270.8262939453125
      z: -57.073768615722656
    }
  }
  landmarks {
    type: UPPER_LIP
    position {
      x: 486.47064208984375
      y: 333.64068603515625
      z: -11.938819885253906
    }
  }
  landmarks {
    type: LOWER_LIP
    position {
      x: 488.053955078125
      y: 402.4744873046875
      z: 5.506862163543701
    }
  }
  landmarks {
    type: MOUTH_LEFT
    position {
      x: 389.22906494140625
      y: 350.38592529296875
      z: 20.536226272583008
    }
  }
  landmarks {
    type: MOUTH_RIGHT
    position {
      x: 558.6113891601562
      y: 338.10687255859375
      z: 61.75973892211914
    }
  }
  landmarks {
    type: MOUTH_CENTER
    position {
      x: 485.9228515625
      y: 362.95477294921875
      z: 2.9842123985290527
    }
  }
  landmarks {
    type: NOSE_BOTTOM_RIGHT
    position {
      x: 530.05322265625
      y: 277.77557373046875
      z: 26.292861938476562
    }
  }
  landmarks {
    type: NOSE_BOTTOM_LEFT
    position {
      x: 435.1253356933594
      y: 287.53680419921875
      z: -2.188866376876831
    }
  }
  landmarks {
    type: NOSE_BOTTOM_CENTER
    position {
      x: 489.20635986328125
      y: 302.001220703125
      z: -14.898569107055664
    }
  }
  landmarks {
    type: LEFT_EYE_TOP_BOUNDARY
    position {
      x: 379.12420654296875
      y: 163.17738342285156
      z: -12.203067779541016
    }
  }
  landmarks {
    type: LEFT_EYE_RIGHT_CORNER
    position {
      x: 417.064697265625
      y: 178.53004455566406
      z: 11.53059196472168
    }
  }
  landmarks {
    type: LEFT_EYE_BOTTOM_BOUNDARY
    position {
      x: 375.2385559082031
      y: 185.38389587402344
      z: -0.4762172996997833
    }
  }
  landmarks {
    type: LEFT_EYE_LEFT_CORNER
    position {
      x: 333.22686767578125
      y: 179.15078735351562
      z: 7.390031814575195
    }
  }
  landmarks {
    type: LEFT_EYE_PUPIL
    position {
      x: 375.582763671875
      y: 175.7420654296875
      z: -5.112864971160889
    }
  }
  landmarks {
    type: RIGHT_EYE_TOP_BOUNDARY
    position {
      x: 553.8519287109375
      y: 148.4358367919922
      z: 36.719181060791016
    }
  }
  landmarks {
    type: RIGHT_EYE_RIGHT_CORNER
    position {
      x: 584.5592651367188
      y: 157.4542236328125
      z: 76.17935180664062
    }
  }
  landmarks {
    type: RIGHT_EYE_BOTTOM_BOUNDARY
    position {
      x: 551.5645141601562
      y: 169.4289093017578
      z: 48.395938873291016
    }
  }
  landmarks {
    type: RIGHT_EYE_LEFT_CORNER
    position {
      x: 518.9324951171875
      y: 168.65855407714844
      z: 40.76214599609375
    }
  }
  landmarks {
    type: RIGHT_EYE_PUPIL
    position {
      x: 554.934814453125
      y: 160.6417236328125
      z: 45.07041931152344
    }
  }
  landmarks {
    type: LEFT_EYEBROW_UPPER_MIDPOINT
    position {
      x: 370.97894287109375
      y: 111.71439361572266
      z: -26.671504974365234
    }
  }
  landmarks {
    type: RIGHT_EYEBROW_UPPER_MIDPOINT
    position {
      x: 560.515625
      y: 95.80352783203125
      z: 26.41659164428711
    }
  }
  landmarks {
    type: LEFT_EAR_TRAGION
    position {
      x: 201.92274475097656
      y: 268.6761474609375
      z: 195.9960479736328
    }
  }
  landmarks {
    type: RIGHT_EAR_TRAGION
    position {
      x: 607.6787109375
      y: 230.4249725341797
      z: 303.4122009277344
    }
  }
  landmarks {
    type: FOREHEAD_GLABELLA
    position {
      x: 472.98822021484375
      y: 124.08467102050781
      z: -19.10523796081543
    }
  }
  landmarks {
    type: CHIN_GNATHION
    position {
      x: 487.76385498046875
      y: 476.538330078125
      z: 33.993316650390625
    }
  }
  landmarks {
    type: CHIN_LEFT_GONION
    position {
      x: 256.85736083984375
      y: 381.3194885253906
      z: 133.56549072265625
    }
  }
  landmarks {
    type: CHIN_RIGHT_GONION
    position {
      x: 616.1009521484375
      y: 350.6595764160156
      z: 234.28517150878906
    }
  }
  roll_angle: -3.8365638256073
  pan_angle: 15.617439270019531
  tilt_angle: -3.5509212017059326
  detection_confidence: 0.9894479513168335
  landmarking_confidence: 0.785702645778656
  joy_likelihood: VERY_LIKELY
  sorrow_likelihood: VERY_UNLIKELY
  anger_likelihood: VERY_UNLIKELY
  surprise_likelihood: VERY_UNLIKELY
  under_exposed_likelihood: VERY_UNLIKELY
  blurred_likelihood: VERY_UNLIKELY
  headwear_likelihood: VERY_UNLIKELY
}
"""
