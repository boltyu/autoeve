import os,time
import random
from auto_parameter_1280_720 import *

devicename = ['192.168.1.187:5555','127.0.0.1:5605','127.0.0.1:5615','de496248','127.0.0.1:5555']#
devicecount = 1

def click_single(devicename,position,waittime):
    os.system(CMD_HOSTADB + devicename + " shell input tap " + position)

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
    for i in range(devicecount):
        tindex = random.randrange(0,3)
        click_single(devicename[i],XY_targets[tindex],1)
        click_single(devicename[i],XY_targets_approach[tindex],1)
    time.sleep(30)

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

def TransferDestinition(target):
    click("150 680",5)
    click(target,3)
    click("366 656",3)
    click("721 620",1)
    click(XY_navigator,2)
    click(XY_navigator_confirm,2)


def TransferOre(expecttimes):
    for times in range(expecttimes):
        click(XY_inventory_close,1)
        click(XY_inventory_close,1)
        click(XY_inventory,2)
        for i in range(2):
            click(XY_inventory_hostcargo,2)
            click(XY_inventory_item1,1)
            click(XY_inventory_item1_moveto,1)
            if i == 1:
                click(XY_inventory_item1_moveto_shipcargo,1)
            else:
                click(XY_inventory_item1_moveto_subtab,1)
                click(XY_inventory_item1_moveto_subtab_orecargo,1)
            click(XY_inventory_item1_moveto_setmax,1)
            click(XY_inventory_item1_moveto_setmax_confirm,1)
        TransferDestinition("137 497")
        time.sleep(420)
        click(XY_inventory_close,1)
        click(XY_inventory_close,1)
        click(XY_inventory,2)
        for i in range(2):
            if(i == 1):
                click(XY_inventory_shipcargo,2)
            else:
                click(XY_inventory_orehold,2)
            click(XY_inventory_selectall,2)
            click(XY_inventory_moveto,1)
            click(XY_inventory_moveto_hanger,2)
        TransferDestinition("137 391")
        NavigateTo(0)
        time.sleep(420)

planet_items = ["138 166","138 296","138 418","138 510"]
def ExtendPlant():
    click("336 93",5)
    for i in planet_items:
        click(i,2)
        click("1200 125",2) # extend time
        # click("1200 285",2) # launch resource
    click(XY_inventory_close,2)
    click(XY_inventory_close,2)


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

    ExitStation(random.randrange(0,3))
    ApproachTo(1)
    time.sleep(12)
    doubleclick(XY_targets[0],1)
    doubleclick(XY_targets[1],1)
    click(XY_miners[0],0.5)
    click(XY_miners[1],0.5)
    click(XY_miners[2],0.5)
    for j in range(18):
        print(j)
        ApproachTo(1)
        click(XY_view_asteroid,1.5)
        doubleclick(XY_targets[0],1)
        doubleclick(XY_targets[1],1)
        for k in range(3):
            click(XY_targets[k],2)
            click(XY_targets_mine[k],1)
        time.sleep(40)
    Return2Home()

if __name__ == "__main__":
    key = input("Do we need to return home at first? 'y' for yes, null or 'n' for no\r\n \
        't' for transfer ore \
        'e' for extend planet life \
        'y' for \)
    if(key == 'y'):
        Return2Home()
        
    elif(key == 't'):
        TransferOre(5)
    elif(key == 'e'):
        ExtendPlant()
    
    while True:
        Return2LocalStation()