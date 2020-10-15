import os,time,random
import parameter_720_1280
from GenericMethod import *
from __main__ import devicecount,devicename


for i in devicename:
    os.system(CMD_HOSTADB_GENERAL + "connect " + i)

def MiningAtLocal():
    for iii in range(10):
        ExitStation()
        click(XY_view_asteroid,1)
        ApproachTo(0)
        time.sleep(20)
        click(XY_miners[0],1)
        click(XY_miners[1],1)
        for j in range(21):
            print(j)
            if(j%10==7):
                click(XY_view_asteroid,2)
                click(XY_view_asteroid_cluster,2)
                ApproachTo(2)
                time.sleep(60)
                click(XY_miners[0],1)
                click(XY_miners[1],1)
            click(XY_view_asteroid,2) # changed to asteriod tab
            ApproachTo(0)
            time.sleep(60)
        Return2Home()
    ExtendPlanet()

def Start():
    try:
        key = input("Do we need to return home at first? 'y' for yes, null or 'n' for no\r\n \
            't' for transfer ore\r\n \
            'e' for extend planet life\r\n \
            'l' for launch planet ore\r\n \
            's' for move ore to company\r\n \
            'r' for retrieve planet ore ")

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
        print("user cancel")

    while True:
        MiningAtLocal()