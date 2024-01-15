# Tello Python3 lesson5
# http://www.ryzerobotics.com/

# 実行は[F5]を押して起動してください
# ファイルの保存：Ctrl + s

######################################
# 今回は、離陸ボタンを押さずに起動してカメラウィンドウが表示されたら
# ドローンを手で動かしてみて静止画がじゃなくてビデオ映像であることを確かめて下さい
# ターミナルに[over_run]などのログが表示された場合、[cap]を以下のようにに変更して試してください。
# cap = cv2.VideoCapture("udp://%s:%s?overrun_nonfatal=1&fifo_size=50000000" % ('192.168.11.7', '11111'))
# 以下の[h264]エラーはドローンとカメラ接続出来たら表示しなくなります。気にしなくて良いです。
# [h264 @ 0000027927e60f80] non-existing PPS 0 referenced
# [h264 @ 0000027927e60f80] decode_slice_header error
# [h264 @ 0000027927e60f80] no frame!
# 以下のエラーは無視して問題ないです。
# [h264 @ 00000279283b02c0] error while decoding MB 55 42, bytestream -8
# ####################################

import socket
import sys
import time
import tkinter
import cv2
import threading

#ドローンとの接続
host = ''
port = 8889
locaddr = (host,port) 
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
tello_address = ('192.168.10.1', 8889)
sock.bind(locaddr)

# 以下実行部分

# カメラを起動する
def tello_movie():
    global btn_photo
    sock.sendto(b'command', tello_address)
    time.sleep(1)
    sock.sendto(b'streamon', tello_address)
    time.sleep(1)
    cap = cv2.VideoCapture("udp:0.0.0.0:11111")
    print('ドローンのカメラ映像が表示されたらボタンを使用可能です')
    while True:
        try:
            ret,frame = cap.read()
            if ret:
                cv2.imshow('TelloCamera',cv2.resize(frame, (500, 300))) # カメラの映像をリサイズして表示
                cv2.waitKey(1)
                if btn_photo ==True:
                    btn_photo =False
                    cv2.imwrite("./lesson5/img5/img_lesson5_0.jpg",frame) # カメラの映像を保存
                    print("写真を撮りました。")
        except KeyboardInterrupt:
            sock.close()
            cv2.destroyAllWindows()
            cap.release()
            print('error and end')
            break              

#実行ボタンがクリックされたら実行
def button_click(): # 実行
    global input_box
    msg = input_box.get() # 入力欄の情報を取得
    print("入力：",msg)
    try:
        if msg=="":
            print("コマンドが入力されていないため、システムを終了します。")
            time.sleep(2)
            root.destroy()
            sock.close()
            #rootとsockやめてるのにsys.exitまでする必要ある？
            sys.exit(0)
        if 'end' in msg:
            print ('終了します')
            sock.close()
            root.destroy()
            sys.exit(0)
        # Send data
        msg = msg.encode(encoding="utf-8")
        sock.sendto(msg, tello_address)
        input_box.delete("0",tkinter.END) # 入力欄の内容をリセットする
    except KeyboardInterrupt:
        print ('\n error\n')
        sock.close()

#ウィンドウの作成
yoko = "700"
tate = "400"
text = "Tello: free command here , can use[end]. \r\nログメッセージはターミナルを見てください。"
root = tkinter.Tk()

root.title("画像認識飛行プログラム")
root.geometry(yoko+"x"+tate)
iconfile = 'icon48.ico'

#入力欄の作成
input_box = tkinter.Entry(width=40)
input_box.place(x=10, y=200)

#ラベルの作成
input_label = tkinter.Label(text=text)
input_label.place(x=10, y=70)



# ボタンを押したときに実行する関数とボタンをウィンドウ上に配置する記述
# 各ボタンが押されたらコマンドを送る処理

def takeoff(): # 離陸
    print("ボタン：離陸する")
    sock.sendto(b'command', tello_address)
    time.sleep(1)
    sock.sendto(b'takeoff',tello_address)

def land(): # 着陸
    print("ボタン：着陸する")
    sock.sendto(b'command', tello_address)
    time.sleep(1)
    sock.sendto(b'land',tello_address)

def forward_30(): # 前進
    print("ボタン：前進する")
    sock.sendto(b'command',tello_address)
    time.sleep(1)
    sock.sendto(b'forward 30',tello_address)
    
def back_30(): # 後退
    print("ボタン：後退する")
    sock.sendto(b'command',tello_address)
    time.sleep(1)
    sock.sendto(b'back 30',tello_address)

btn_photo = False
def take_photo():
    global btn_photo
    print("ボタン：写真を撮る")
    btn_photo =True
    

#ボタンの作成
button = tkinter.Button(text="実行",command=button_click)
button.place(x=10, y=130)

ririku = tkinter.Button(text="離陸",command=takeoff)
ririku.place(x=500, y=60)

chakuriku = tkinter.Button(text="着陸",command=land)
chakuriku.place(x=500, y=100)


mae = tkinter.Button(text="前進",command=forward_30)
mae.place(x=550, y=60)

usiro = tkinter.Button(text="後退",command=back_30)
usiro.place(x=550, y=100)

takephoto = tkinter.Button(text="写真を撮る",command=take_photo)
takephoto.place(x=600,y=140)

#スレッドの作成
movieThread = threading.Thread(target=tello_movie)
movieThread.setDaemon(True)
movieThread.start()

#ウインドウの描画
root.mainloop()