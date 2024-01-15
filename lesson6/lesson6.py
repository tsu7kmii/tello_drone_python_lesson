# Tello Python3 opencv cascade lesson6

# 実行は[F5]を押して起動してください
# ファイルの保存：Ctrl + s
# カスケードの作成、サンプルコード
# https://www.pc-koubou.jp/magazine/21280
# サンプルコード、分かりやすい解説
# https://qiita.com/FukuharaYohei/items/ec6dce7cc5ea21a51a82

import cv2

# 以下の画像パスを各自変更する
img = cv2.imread('./lesson6/img/img_lesson6_1.jpg')
            
grayimg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            
custom_cascade = cv2.CascadeClassifier('./lesson6/img_xml/haarcascade_frontalface_default.xml')
            
custom_rect = custom_cascade.detectMultiScale(grayimg,scaleFactor=1.1, minNeighbors=2,minSize=(50, 50))
# つまりこれがカスケードから認識してるやつ
            
print(custom_rect)# これが認識した画像サイズ,lenで数えたら人の数
print(len(custom_rect))            
if len(custom_rect) > 1:
    print("2 human face")
    for rect in custom_rect: #暴発チェック、認識した場所かこう
        cv2.rectangle(img, tuple(rect[0:2]), tuple(rect[0:2]+rect[2:4]), (0, 0, 255), thickness=3)
elif len(custom_rect) >0:
    print("1 human face")
    for rect in custom_rect:
        cv2.rectangle(img, tuple(rect[0:2]), tuple(rect[0:2]+rect[2:4]), (0, 0, 255), thickness=3)
else:
    print("no human face")

#わりかし顔じゃないところ顔っていうかもしれないので、見つけたか見つけてないかじゃないときついカモしれない

cv2.imshow('where is human face', img)        
cv2.waitKey(0)
cv2.destroyAllWindows()