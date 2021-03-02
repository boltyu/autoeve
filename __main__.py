import os
import sys
global devicename

shiplist = ['venture','retriever']
devicename = ""
deviceindex = -1
try:
    shiptype = sys.argv[1]
    deviceindex = int(sys.argv[2])
except:
    shiptype = "retriever"
    devicename = sys.argv[2]
devicelist = ['127.0.0.1:5555','127.0.0.1:5595','127.0.0.1:5645','192.168.1.5:5555','192.168.1.3:5555','de496248','192.168.1.6:5555']
if deviceindex < 10 and deviceindex >= 0:
    devicename = devicelist[deviceindex]
print("Ship:",shiptype)
print("Device:",devicename)

if(shiptype == 'venture'):
    oremaster = 'none'
    import venture3
    venture3.Start()
else:
    oremaster = 'none'
    import retriver
    retriver.Start()
    
