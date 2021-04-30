import os,time,random
import parameter_720_1280
from GenericMethod2 import *
from GenericMethod import click_single as originclick
from __main__ import devicename,oremaster
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout

def MiningAtLocal():
    ExitStation() # ExitStation and ReturnHome should not touch the view category
    time.sleep(45)
    click(XY_view_menu,1)
    click(XY_view_onlyasteroid,1)
    for j in range(40): 
        print(j)
        if j%10 == 0:   # 0==>Station to AsteroidCluster   123..==>AsteroidCluster to AsteroidCluster
            click(XY_view_menu,2)
            click(XY_view_onlyasteroid,1)
            WarpTo()
            time.sleep(25)
            click(XY_view_menu,3)
            click(XY_view_asteroidandcluster,3)
            originclick(XY_miners[0],2)
            originclick(XY_miners[1],2)
        else:
            time.sleep(30)
        ApproachTo(0)
    Return2Home()
    
    
def User1():
    SwitchUser(0)
def User2():
    SwitchUser(1)
def User3():
    SwitchUser(2)    
    
    
def Start():
    mingingcount = 0
    DisconnectDevice(devicename)
    ConnectDevice(devicename)
    
    app = QApplication([])
    window = QWidget()
    layout = QVBoxLayout()
    btn_return2home = QPushButton('返回基地')
    btn_return2home.clicked.connect(Return2Home)
    btn_launchplanet = QPushButton('发射开发材料')
    btn_launchplanet.clicked.connect(LaunchPlanet)
    btn_getplanet = QPushButton('获取开发材料')
    btn_getplanet.clicked.connect(RetrieveOre)
    btn_extentplanet = QPushButton('延长开发时间')
    btn_extentplanet.clicked.connect(ExtendPlanet)
    btn_user1 = QPushButton('用户1')
    btn_user1.clicked.connect(User1)
    btn_user2 = QPushButton('用户2')
    btn_user2.clicked.connect(User2)
    btn_user3 = QPushButton('用户3')
    btn_user3.clicked.connect(User3)
    btn_list = [btn_return2home, btn_launchplanet, btn_getplanet, btn_extentplanet, btn_user1, btn_user2, btn_user3]
    for i in btn_list:
        layout.addWidget(i)
    window.setLayout(layout)
    window.show()
    app.exec()    
    print("end")
    # try:
        # while True:
            # MiningAtLocal()
            # mingingcount+=1
            # print("mingingcouont",mingingcount)
    # except KeyboardInterrupt:
        # print("mingingcouont",mingingcount)
        # ifreturn = input('终止前返回基地？ y 是, n 否 ')
        # if(ifreturn == 'y'):
            # Return2Home()