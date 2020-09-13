import os,time
from auto_parameter_1280_720 import *

devicename = ['127.0.0.1:5605','127.0.0.1:5615','127.0.0.1:5555']#
devicecount = 1


def click(position,waittime):
    for i in range(devicecount):
        os.system(CMD_HOSTADB + devicename[i] + " shell input tap " + position)
    time.sleep(waittime)

def ApproachTo(XY_target):
    click(XY_view_asteroid,1.5) # changed to asteriod tab
    #click(XY_afterburner,1)
    click(XY_targets[XY_target],1.5)
    click(XY_targets_approach[XY_target],1.5)
    #click(XY_afterburner,1)

def WarpTo(XY_target):
    click(XY_view,2)
    click(XY_targets[XY_target],1)
    click(XY_targets_approach[XY_target],30)

def LockTarget(XY_target):
    click(XY_targets[XY_target],1)
    click(XY_targets_lock[XY_target],1.5)

def doubleclick(position,waittime):
    for i in range(devicecount):
        os.system(CMD_HOSTADB + devicename[i] + " shell \"input tap " + position + "&sleep 0.3&" + "input tap " + position +"\"")
    time.sleep(waittime)

def NavigateTo(XY_position):
    click(XY_chat,2)
    click(XY_positions[XY_position],1)
    click(XY_positions_set[XY_position],1)
    click(XY_blank,1)
    click(XY_navigator,1)
    click(XY_navigator_confirm,1)


def StoreOre():
    click(XY_inventory,5)
    click(XY_inventory_orehold,5)
    click(XY_inventory_selectall,5)
    click(XY_inventory_moveto,3)
    click(XY_inventory_moveto_hanger,5)
    click(XY_inventory_close,2)
    click(XY_inventory_close,2)

def ExitStation(target):
    click(XY_exitstation,25)
    click(XY_view,2)
    WarpTo(target)
    print("We are now in Asteroid Cluster")

def Return2Home():
    NavigateTo(0)
    time.sleep(60)
    print("We are arriving at Home")
    StoreOre()
    

def Return2LocalStation():
    
    for i in range(0,2):
        ExitStation(i)
        ApproachTo(1)
        time.sleep(12)
        doubleclick(XY_targets[0],1)
        doubleclick(XY_targets[1],1)
        click(XY_miners[0],0.5)
        click(XY_miners[1],0.5)
        click(XY_miners[2],0.5)
        for j in range(30):
            print(j)
            ApproachTo(1)
            click(XY_view_asteroid,1.5)
            doubleclick(XY_targets[0],1)
            doubleclick(XY_targets[1],1)
            for k in range(3):
                click(XY_targets[k],2)
                click(XY_targets_mine[k],1)
            time.sleep(20)
        Return2Home()

if __name__ == "__main__":
    key = input("Do we need to return home at first? 'y' for yes, others for no\r\n")
    if(key == 'y'):
        Return2Home()
    while True:
        Return2LocalStation()
