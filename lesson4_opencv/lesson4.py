# openCV (cv2) Python3 lesson4 

# please install openCV
# ターミナルの[PS c:\tello_python_lesson>]のところに[pip install opencv-python]と入力し実行してください

# 実行は[F5]を押して起動してください
# ファイルの保存：Ctrl + s

import cv2
image = cv2.imread("./lesson4/img4/img_0.jpg") #画像パス
cv2.imshow("picture",image)
cv2.waitKey(0)