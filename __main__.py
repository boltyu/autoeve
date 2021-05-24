import os
import sys
global devicename

devicename = ""
deviceindex = -1

try:
    devicename = sys.argv[1]
except:
    devicename = ""

if(devicename == ""):
    devicelist = ['127.0.0.1:5555','de496248','192.168.43.1:5555','add new']
    for i in range(0,4):
        print(i,":",devicelist[i])
    deviceindex = int(input("choose one device: "))

    if deviceindex < 3 and deviceindex >= 0:
        devicename = devicelist[deviceindex]
    elif deviceindex == 3:
        devicename = input()
        
print("Device:",devicename)
oremaster = 'none'
import retriver
retriver.Start()
    
