import os,time,random
import parameter_720_1280
from GenericMethod import *
from __main__ import devicecount,devicename


for i in range(devicecount):
    DisconnectDevice(devicename[i])
    ConnectDevice(devicename[i])
MiningVersion = 1
def MiningAtLocal():
    if MiningVersion == 2:
        for repeats in range(10):
            ExitStation()
            time.sleep(20)
            for miningrepeats in range(18):
                print(miningrepeats)
                click(XY_view_asteroid,1)
                ApproachTo(1)
                time.sleep(5)
                click(XY_miners[0],1)
                click(XY_miners[1],1)
                ApproachTo(0)
                time.sleep(120)
                click(XY_miners[0],1)
                click(XY_miners[1],1)
            Return2Home()
        ExtendPlanet()

    elif MiningVersion == 1:
        for iii in range(50):
            ExitStation()
            click(XY_view_menu,1)
            click(XY_view_asteroid,12)
            ApproachTo(0)
            time.sleep(12)
            click(XY_miners[0],0)
            click(XY_miners[1],0)
            for j in range(21):
                print(j)
                ApproachTo(0)
                time.sleep(30)
            Return2Home()
        #MoveOre3Company()
        ExtendPlanet()

def Start():
    key = input("我们将要?\r\n \
        'y'返回基地  |  'n'出门采矿\r\n \
        's'将当前矿船中矿物移出  |  'm'将仓库中矿物送至第一机库\r\n \
        'e'延长行星开发时效  |  'l'发射行星资源  |  'r'获取行星资源\r\n \
        'c'重连所有设备  |  'ccc'点击三次右上角关闭按钮\r\n ")

    if(key == 'y'):
        Return2Home()
    elif(key == 'n'):
        pass
    elif(key == 'l'):
        LaunchPlanet()
    elif(key == 'm'):
        MoveOre2Company()
    elif(key == 's'):
        StoreOre()
    elif(key == 'r'):
        RetrieveOre()
    elif(key == 'e'):
        ExtendPlanet()
    elif(key == 'c'): # reconnect
        for i in range(devicecount):
            DisconnectDevice(devicename[i])
            ConnectDevice(devicename[i])
    elif(key == 'ccc'):
        click(XY_inventory_close,1)
        click(XY_inventory_close,1)
        click(XY_inventory_close,1)
    else:
        print('未指定动作，将执行采矿')



    try:
        while True:
            MiningAtLocal()
    except KeyboardInterrupt:
        ifreturn = input('终止前返回基地？ y 是, n 否 ')
        if(ifreturn == 'y'):
            Return2Home()
        exit(0)