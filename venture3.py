
from GenericMethod import *
from ServerMethod import *
from parameter_720_1280 import *
from __main__ import devicecount,devicename
import os


oremaster = 1
ifupload = False

print("connecting to devices...")
for i in range(devicecount):
    os.system(CMD_HOSTADB_GENERAL + "connect " + devicename[i])

def MiningAtLocal():
    global ifupload
    for iii in range(20):
        ExitStation()
        click(XY_view_asteroid,1.5) # changed to asteriod tab
        ApproachTo(1)
        time.sleep(30)
        for j in range(9):
            print(j)
            click(XY_view_asteroid,1) # changed to asteriod tab
            ApproachTo(1)
            ApproachTo(0)
            for k in range(3):
                click(XY_targets[k],1)
                click(XY_targets_mine[k],1)
            doubleclick(XY_targets[0],0)
            doubleclick(XY_targets[1],0)
            doubleclick(XY_targets[2],0)
            time.sleep(60)
            # if(ifupload):
            #     UploadRemote()
            # else:
            #     SyncRemote()
        Return2Home()
    ExtendPlanet()
    MoveOre2Company()
    

def Start():
    try:
        key = input("press Enter for mining, or \r\n \
            'y' for return home \r\n \
            't' for transfer ore\r\n \
            'e' for extend planet life\r\n \
            'l' for launch planet ore\r\n \
            'c' for contract ore\r\n \
            'r' for retrieve planet ore\r\n \
            's' for move ore to company ")
        if(key == 'y'):
            Return2Home()
        elif(key == 'l'):
            LaunchPlanet()
        elif(key == 't'):
            TransferOre(5)
        elif(key == 's'):
            MoveOre2Company()
        elif(key == 'r'):
            RetrieveOre()
        elif(key == 'e'):
            ExtendPlanet()
        else:
            raise KeyboardInterrupt
        exit(0)
    except KeyboardInterrupt:
        pass

    while True:
        MiningAtLocal()