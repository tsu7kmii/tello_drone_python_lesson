# Tello Python3 lesson2
# http://www.ryzerobotics.com/

# 実行は[F5]を押して起動してください
# ファイルの保存：Ctrl + s
import socket
import sys
import time
import tkinter

#ドローンとの接続
host = ''
port = 8889
locaddr = (host,port) 
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
tello_address = ('192.168.10.1', 8889)
sock.bind(locaddr)

# 以下実行部分

#実行ボタンがクリックされたら実行
def button_click(): # 実行
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
            root.destroy()
            sock.close()
            sys.exit(0)
        # ドローンにコマンドを送りレスポンスを表示する
        msg = msg.encode(encoding="utf-8")
        sock.sendto(msg, tello_address)
        data, server = sock.recvfrom(1518)
        tello_reply = data.decode(encoding="utf-8")
        print("tello:",tello_reply)               
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




#ウインドウの描画
root.mainloop()