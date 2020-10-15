import socket
from parameter_720_1280 import *
import os,tarfile
from PIL import Image

def SyncRemote():
    global devicecount
    self_socket = socket.socket()
    try:
        self_socket.connect(("122.51.67.162",18181))
        self_socket.send(bytes("onlinenotify",encoding="utf-8"))
        cmd = self_socket.recv(1024).decode('utf-8')
        #print(cmd)
        if(cmd == 'cap'):
            for i in range(devicecount):
                newname = "cap" + str(i) + ".png"
                os.system(CMD_HOSTADB + devicename[i] + " shell screencap /sdcard/tmp.png")
                os.system(CMD_HOSTADB + devicename[i] + " pull /sdcard/tmp.png " + newname)
                image = Image.open(newname)
                image.resize((640,360)).save(newname,"png")
            pictar = tarfile.open('./cap.tar','w')
            pictar.add("./cap0.png")
            pictar.add("./cap1.png")
            pictar.add("./cap2.png")
            pictar.close()
            ifupload = True
        elif(cmd == "poweroff"):
            os.system(CMD_HOSTADB + devicename[2] + " shell reboot -p")
            devicecount = 2
        elif(cmd[1:6] == "shell"):
            os.system(CMD_HOSTADB + devicename[int(cmd[0:1])] + " " + cmd[1:])
        elif(cmd == "shutdown"):
            os.system("shutdown -p")
        #print("sync success")
    except:
        pass
    self_socket.close()

def UploadRemote():
    self_socket = socket.socket()
    try:
        self_socket.connect(("122.51.67.162",18181))
        pictar = open('./cap.tar','rb')
        tardata = pictar.read(1024000)
        #print(len(tardata))
        pictar.close()
        self_socket.send(tardata)
        ifupload = False
    except:
        pass
    self_socket.close()