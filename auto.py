import os,time
from auto_param_1920_1080 import *

def click(position,waittime):
    os.system(CMD_HOSTADB + " input tap " + position)
    time.sleep(waittime)

def ApproachTo(XY_target):
    click(XY_view_asteroid,1.5) # changed to asteriod tab
    #click(XY_afterburner,1)
    click(XY_targets[XY_target],1.5)
    click(XY_targets_approach[XY_target],1.5)
    #click(XY_afterburner,1)

def WarpTo(XY_target):
    click(XY_view,2)
    click(XY_targets[XY_target],2)
    click(XY_targets_approach[XY_target],30)

def LockTarget(XY_target):
    click(XY_targets[XY_target],1)
    click(XY_targets_lock[XY_target],1.5)

def doubleclick(position,waittime):
    os.system(CMD_HOSTADB + " \"input tap " + position + "&sleep 0.3&" + "input tap " + position +"\"")
    time.sleep(waittime)

def NavigateTo(XY_position):
    click(XY_chat,2)
    click(XY_positions[XY_position],1)
    click(XY_positions_set[XY_position],1)
    click(XY_blank,1)
    click(XY_navigator,1)
    click(XY_navigator_confirm,1)


def StoreOre():
    click(XY_inventory,3)
    click(XY_inventory_orehold,3)
    click(XY_inventory_selectall,3)
    click(XY_inventory_moveto,3)
    click(XY_inventory_moveto_hanger,3)
    click(XY_inventory_close,2)
    click(XY_inventory_close,2)

def ExitStation(target):
    click(XY_exitstation,20)
    click(XY_view,2)
    WarpTo(target)
    print("We are now in Asteroid Cluster")

def Return2Home():
    NavigateTo(0)
    time.sleep(50)
    print("We are arriving at Home")
    StoreOre()
    

def Return2LocalStation():

    for i in range(0,2):
        ExitStation(i)
        for j in range(22):
            ApproachTo(0)
            print(j)
            doubleclick(XY_targets[0],1.5)
            doubleclick(XY_targets[1],1.5)
            doubleclick(XY_targets[2],1.5)
            for k in range(3):
                click(XY_targets[k],2)
                click(XY_targets_mine[k],1)
            time.sleep(16)
        Return2Home()


while True:
    #Return2Home()
    Return2LocalStation()
