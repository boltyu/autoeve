
from GenericMethod2 import *
from parameter_720_1280 import *
from __main__ import devicename,oremaster
import os

DisconnectDevice(devicename)
ConnectDevice(devicename)

def MiningAtLocal():
    for iii in range(20):
        ExitStation()
        click(XY_view_menu,2)
        click(XY_view_asteroidandcluster,1.5) # changed to asteriod tab
        for j in range(5):
            print(j)
            click(XY_view_menu,2)
            click(XY_view_onlyasteroid,2) # changed to asteriod tab
            click(XY_view_menu,2)
            click(XY_view_asteroidandcluster,2) # changed to asteriod tab
            ApproachTo(2)
            ApproachTo(1)
            for k in range(6):
                click(XY_targets[k%3],0)
                click(XY_targets_mine[k%3],1)
            time.sleep(30)
        Return2Home()
    print(iii)
    ExtendPlanet()
    #MoveOre2Company()
    

def Start():
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
    except KeyboardInterrupt:
        ifreturn = input('终止前返回基地？ y 是, n 否 ')
        if(ifreturn == 'y'):
            Return2Home()