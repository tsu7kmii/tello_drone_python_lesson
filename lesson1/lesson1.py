# Tello Python3 Control Demo 
# # Tello Python3 lesson1
# http://www.ryzerobotics.com/

# 実行は[F5]を押して起動してください
# ファイルの保存：Ctrl + s
import socket

#ドローンとの接続
host = ''
port = 8889
locaddr = (host,port) 
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
tello_address = ('192.168.10.1', 8889)
sock.bind(locaddr)

# 以下実行部分

while True: # 繰り返し
    try:
        msg = str(input("コマンドを入力してください："))
        print("終了の場合、着陸後:[end]")
        if not msg: # 何も入力されずエンターを押した時
            break  
        if 'end' in msg: # [end]と入力したとき終了する
            print ('終了します')
            sock.close() # ドローンとの接続解除
            break
        # ドローンにコマンドを送る
        msg = msg.encode(encoding="utf-8") # 文字コードの変更
        sent = sock.sendto(msg, tello_address) # ドローンにコマンドを送信する
        # ドローンにコマンドを送ったときのレスポンスを表示
        data, server = sock.recvfrom(1518)
        tello_reply = data.decode(encoding="utf-8")
        print("tello:",tello_reply)
    except KeyboardInterrupt: # [Ctrl C]をキャッチして終了
        print ('\n . . .\n')
        sock.close()  
        break
    
    
