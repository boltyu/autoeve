import os,time
import random
from auto_parameter_1280_720 import *

devicename = ['127.0.0.1:5605','127.0.0.1:5645','127.0.0.1:5555','de496248','192.168.1.187:5555']#
#devicename = ['192.168.1.187:5555']
devicecount = 3

for i in devicename:
    os.system(CMD_HOSTADB_GENERAL + "connect " + i)


def click_single(devicename,position,waittime):
    os.system(CMD_HOSTADB + devicename + " shell input tap " + position)

def click(position,waittime):
    for i in range(devicecount):
        os.system(CMD_HOSTADB + devicename[i] + " shell input tap " + position)
    time.sleep(waittime)

def typetext(textstring,waittime):
    for i in range(devicecount):
        os.system(CMD_HOSTADB + devicename[i] + " shell input text " + textstring)
    time.sleep(waittime)

def ApproachTo(XY_target):
    #click(XY_afterburner,1)
    click(XY_targets[XY_target],2)
    click(XY_targets[XY_target],2)
    click(XY_targets_approach[XY_target],1.5)
    #click(XY_afterburner,1)

def WarpTo():
    click(XY_view,2)
    randomtargets = [0,1,2,3]
    random.shuffle(randomtargets)
    for i in range(devicecount):
        click_single(devicename[i],XY_targets[randomtargets[i]],1)
        click_single(devicename[i],XY_targets_approach[randomtargets[i]],1)
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
        print("transferation " + str(times) + " finished")

XY_planet_item_extend = "1200 125"
XY_planet = "336 93"
XY_planet_items = ["138 166","138 296","138 418","138 510"]
def ExtendPlanet():
    click(XY_planet,5)
    for i in XY_planet_items:
        click(i,2)
        click(XY_planet_item_extend,2) # extend time
        # click("1200 285",2) # launch resource
    click(XY_inventory_close,2)
    click(XY_inventory_close,2)

XY_planet_item_launch = ["1200 285","1200 370","1200 450","1200 530"]
def LaunchPlanet():
    click(XY_planet,5)
    for items in XY_planet_items:
        click(items,2)
        click(XY_planet_item_extend,2)
        for items_launch in range(4):
            click(XY_planet_item_launch[items_launch],2)
            click(XY_planet_item_launch[items_launch],2)
    click(XY_inventory_close,2)
    click(XY_inventory_close,2)

XY_inventory_collapse_tabstation = "125 101"
XY_inventory_currentship = "140 456"
XY_inventory_imicas = "140 493"
XY_inventory_chongfeng = "140 565"
XY_inventory_imicas_active = "45 493"
XY_inventory_chongfeng_active= "45 565"

def RetrieveOre():
    click(XY_inventory,5)
    click(XY_inventory_collapse_tabstation,2)
    click(XY_inventory_imicas,2)
    click(XY_inventory_imicas_active,20)
    click(XY_inventory_close,2)
    click(XY_inventory_close,2)
    for i in [3,2,1,0]:
        click(XY_planet,3)
        click(XY_planet_items[i],3)
        click("1160 650",2)
        click(XY_navigator,2)
        click(XY_navigator_confirm,1)
        click(XY_inventory_close,2)
        click(XY_inventory_close,1)
        if i == 1:
            time.sleep(80)
        elif i == 3:
            time.sleep(50)
        else:
            time.sleep(40)
        click("460 620",2)
    NavigateTo(0)
    time.sleep(120)
    click(XY_inventory,5)
    click(XY_inventory_currentship,2)
    click(XY_inventory_selectall,5)
    click(XY_inventory_moveto,3)
    click(XY_inventory_moveto_hanger,5)
    click(XY_inventory_chongfeng,2)
    click(XY_inventory_chongfeng_active,20)
    click(XY_inventory_close,2)
    click(XY_inventory_close,2)
    click(XY_inventory_close,2)


def ContractOre():
    click("50 35",2)
    click("700 200",3)
    click("145 679",2)
    click("733 392",2)
    click("860 495",3)
    typetext("boltyu",3)
    click("1080 30",2)
    click("1080 30",2)
    click("1153 660",2)
    click("730 200",2)
    click("730 270",2)
    click("1132 206",2)
    click("1055 352",2)
    click("1050 205",2)
    click("1153 660",2)
    click("1153 660",2)
    click("1067 611",2)
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

def ExitStation():
    click(XY_exitstation,25)
    click(XY_view,2)
    WarpTo()
    print("We are now in Asteroid Cluster")

def Return2Home():
    NavigateTo(0)
    time.sleep(60)
    print("We are arriving at Home")
    click(XY_closeads,1)
    click(XY_closeads,1)
    StoreOre()

def Return2LocalStation():
    for iii in range(15):
        ExitStation()
        click(XY_view_asteroid,1.5) # changed to asteriod tab
        ApproachTo(1)
        time.sleep(12)
        doubleclick(XY_targets[0],1)
        doubleclick(XY_targets[1],2)
        click(XY_miners[0],0)
        click(XY_miners[1],0)
        for j in range(15):
            print(j)
            click(XY_view_asteroid,1) # changed to asteriod tab
            ApproachTo(1)
            ApproachTo(0)
            doubleclick(XY_targets[0],1)
            doubleclick(XY_targets[1],0)
            for k in range(3):
                click(XY_targets[k],2)
                click(XY_targets_mine[k],1)
            time.sleep(40)
        Return2Home()
    ExtendPlanet()
    ContractOre()

if __name__ == "__main__":
    try:
        key = input("Do we need to return home at first? 'y' for yes, null or 'n' for no\r\n \
            't' for transfer ore\r\n \
            'e' for extend planet life\r\n \
            'l' for launch planet ore\r\n \
            'c' for contract ore\r\n \
            'r' for retrieve planet ore ")

        if(key == 'y'):
            Return2Home()
        elif(key == 'l'):
            LaunchPlanet()
        elif(key == 't'):
            TransferOre(5)
        elif(key == 'c'):
            ContractOre()
        elif(key == 'r'):
            RetrieveOre()
        elif(key == 'e'):
            ExtendPlanet()
        
        while True:
            Return2LocalStation()
    except KeyboardInterrupt:
        print("user cancel")
        