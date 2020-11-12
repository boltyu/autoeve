
import sys
global devicename
global devicecount

shiplist = ['Venture3','Retriever']

# print(sys.argv)
# print("Select ship:")
# for i in shiplist:
#     print(str(shiplist.index(i)+1),i)
# print(" ")
whichship = sys.argv[1]
devicecount = int(sys.argv[2])

if(whichship == 'venture3'):
    devicename = ['192.168.1.172:5555','Y9K0215424009021','de496248','127.0.0.1:5605','192.168.1.187:5555']#
    print("devicelist: ",devicename[:devicecount])
    import venture3
    venture3.Start()
else:
    devicename = ['127.0.0.1:5565','127.0.0.1:5555','192.168.1.3:5555','de496248']
    oremaster = '127.0.0.1:5555'
    print("devicelist: ",devicename[:devicecount])
    import retriver
    retriver.Start()
    
