# Tello Python3 lesson2
# http://www.ryzerobotics.com/

# 実行は[F5]を押して起動してください
# ファイルの保存：Ctrl + s
import socket
import time

#ドローンとの接続
host = ''
port = 8889
locaddr = (host,port) 
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
tello_address = ('192.168.10.1', 8889)
sock.bind(locaddr)

# 以下実行部分

# コマンドを書いたテキストファイルを開き、command_listに格納する
command_list = []
with open("./lesson2/send_command.txt", 'r') as f: # send_command.txtのファイルを開く
    command = f.readlines()  # send_command.txtに書いてある内容を読み込み、commandに格納する
    print(command)  # 適時コメントアウトする
    # 今のままでは改行コード[\n]が含まれているので削除してcommand_listに格納する
    # それぞれのコマンドから改行コードを削除するためcommandからそれぞれのコマンドをforで取り出す
    command_list = [cmd.strip() for cmd in command] 
print("これからtelloに送るコマンド",command_list)

# command_listから順番にコマンドを出して、ドローンに指示する
for msg in command_list:
    print("これから実行するコマンド",msg)
    if 'end' in msg: # endの時終了する
        print ('終了します')
        sock.close()  
        break 
    # ドローンにコマンドを送る
    msg = msg.encode(encoding="utf-8") 
    sock.sendto(msg, tello_address)    
    time.sleep(5) # 命令を上書きさせないため、5秒待機する  
    # ドローンにコマンドを送ったときのレスポンスを表示
    data, server = sock.recvfrom(1518)
    tello_reply = data.decode(encoding="utf-8")
    print("tello:",tello_reply)

