
global devicename
global devicecount

shiplist = ['Venture3','Retriever']

print("Select ship:")
for i in shiplist:
    print(str(shiplist.index(i)+1),i)
print(" ")
whichship = input()

if(whichship == '1'):
    devicename = ['127.0.0.1:5645','127.0.0.1:5555','192.168.1.172:5555','Y9K0215424009021','de496248','127.0.0.1:5605','192.168.1.187:5555']#
    devicecount = 3
    import venture3
    venture3.Start()
elif(whichship == '2'):
    devicename = ['de496248']
    devicecount = 1
    import retriver
    retriver.Start()
    
