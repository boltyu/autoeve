import os,time,random
import parameter_720_1280
from GenericMethod2 import *
from __main__ import devicename,oremaster


DisconnectDevice(devicename)
ConnectDevice(devicename)

def MiningAtLocal():
    for iii in range(10):
        ExitStation() # ExitStation and ReturnHome should not touch the view category
        time.sleep(50)
        click(XY_miners[0],1)
        click(XY_miners[1],1)
        click(XY_view_menu,1)
        click(XY_view_onlyasteroid,1)
        for j in range(20):
            if j%4 == 0:
                click(XY_view_menu,1)
                click(XY_view_asteroidandcluster,1)
                WarpTo([1,2,3,3])
                time.sleep(15)
                click(XY_miners[0],0)
                click(XY_miners[1],0)
                time.sleep(20)
                click(XY_view_menu,0)
                click(XY_view_onlyasteroid,0)
                click(XY_miners[0],0)
                click(XY_miners[1],0)
            ApproachTo(0)
            print(j)
            time.sleep(25)
        Return2Home()
def Start():
    mingingcount = 0
    while True:
        key = input("我们将要?\r\n \
            'y'返回基地\r\n \
            's'将当前矿船中矿物移出  |  'm'将仓库中矿物送至第一机库\r\n \
            'e'延长行星开发时效  |  'l'发射行星资源  |  'r'获取行星资源\r\n \
            'c'重连所有设备  |  'ccc'点击三次右上角关闭按钮\r\n ")
        if(key == 'y'):
            Return2Home()
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
            break
    try:
        while True:
            MiningAtLocal()
            mingingcount+=1
            print("mingingcouont",mingingcount)
    except KeyboardInterrupt:
        print("mingingcouont",mingingcount)
        ifreturn = input('终止前返回基地？ y 是, n 否 ')
        if(ifreturn == 'y'):
            Return2Home()