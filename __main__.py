
import sys
global devicename

shiplist = ['venture','retriever']

# print(sys.argv)
# print("Select ship:")
# for i in shiplist:
#     print(str(shiplist.index(i)+1),i)
# print(" ")
try:
    shiptype = sys.argv[1]
    deviceindex = int(sys.argv[2])
except:
    shiptype = "venture"
    deviceindex = 0
devicelist = ['127.0.0.1:5595','127.0.0.1:5645','192.168.1.5:5555','de496248']
devicename = devicelist[deviceindex]
print("Ship:",shiptype)
print("Device:",devicename)

if(shiptype == 'venture'):
    oremaster = 'none'
    import venture3
    venture3.Start()
else:
    oremaster = '127.0.0.1:5555'
    import retriver
    retriver.Start()
    
