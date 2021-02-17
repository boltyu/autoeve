from parameter_720_1280 import *
import os,time,socket,tarfile,random
#from PIL import Image
from __main__ import devicename,oremaster

def click(position,waittime):
    x,y = position.split(' ')
    x = str(int(x) + random.randrange(-4,4)) + '.' + str(random.randrange(0,9))
    y = str(int(y) + random.randrange(-4,4)) + '.' + str(random.randrange(0,9))
    os.system(CMD_HOSTADB + devicename + " shell input tap " + x + ' ' + y)
    time.sleep(waittime+random.randrange(0,4))

def doubleclick(position,waittime):
    x,y = position.split(' ')
    x = str(int(x) + random.randrange(-4,4)) + '.' + str(random.randrange(0,9))
    y = str(int(y) + random.randrange(-4,4)) + '.' + str(random.randrange(0,9))
    interval = str(random.randrange(0,5))
    os.system(CMD_HOSTADB + devicename + " shell \"input tap " + position + "&sleep 0."+ interval + "&" + "input tap " + position +"\"")
    time.sleep(waittime+random.randrange(0,4))

def DisconnectDevice(devicename):
    if devicename.find(':') != -1:
        os.system(CMD_HOSTADB_GENERAL + " disconnect " + devicename)

def ConnectDevice(devicename):
    if devicename.find(':') != -1:
        os.system(CMD_HOSTADB_GENERAL + " connect " + devicename)

def typetext(textstring,waittime):
    os.system(CMD_HOSTADB + devicename + " shell input text " + textstring)
    time.sleep(waittime+random.randrange(0,4))

def ApproachTo(XY_target):
    click(XY_targets[XY_target],0)
    click(XY_targets_approach[XY_target],1)

def WarpTo(randomtargets):
    randomtargets = random.randrange(0,3)
    click(XY_view,2)
    click(XY_targets[randomtargets],2)
    click(XY_targets_approach[randomtargets],3)

def LockTarget(XY_target):
    click(XY_targets[XY_target],1)
    click(XY_targets_lock[XY_target],1)

def NavigateToChatpos(XY_position):
    click(XY_chat,2)
    click(XY_chat_positions[XY_position],1)
    click(XY_chat_positions_set[XY_position],1)
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
            click(XY_inventory_moveto_hostcargo,2)
        TransferDestinition("137 391")
        NavigateToChatpos(0)
        time.sleep(420)
        #print("transferation " + str(times) + " finished")

def ExtendPlanet():
    click(XY_planet,5)
    for i in XY_planet_items:
        click(i,2)
        click(XY_planet_item_extend,2) # extend time
        # click("1200 285",2) # launch resource
    click(XY_inventory_close,2)
    click(XY_inventory_close,2)

def LaunchPlanet():
    click(XY_planet,5)
    for items in XY_planet_items:
        click(items,2)
        click(XY_planet_item_extend,2)
        for items_launch in range(4):
            click(XY_planet_item_launch[items_launch],2)
            click(XY_planet_item_launch[items_launch],2)
            click(XY_planet_reject_autonav,1)
    click(XY_inventory_close,2)
    click(XY_inventory_close,2)


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
        click(XY_inventory_close,2)
        click(XY_inventory_close,2)
        click(XY_navigator,2)
        click(XY_navigator_confirm,1)
        if i == 1:
            time.sleep(80)
        elif i == 3:
            time.sleep(50)
        else:
            time.sleep(40)
        click("460 620",2)
    Return2Home()
    time.sleep(120)
    click(XY_inventory,4)
    click(XY_inventory_chongfeng,2)
    click(XY_inventory_chongfeng_active,20)
    click(XY_inventory_close,2)
    click(XY_inventory_close,2)
    click(XY_inventory_close,2)

''' 在军团产业中无需使用合同功能
def ContractOre():
    click("185 100",5)
    click("145 679",3)
    click("733 392",3)
    click("860 495",3)
    typetext("boltyu",3)
    click("1080 30",3)
    click("1080 30",3)
    click("1153 660",3)
    click("730 200",3)
    click("730 270",3)
    click("1132 206",3)
    click("1055 352",3)
    click("1050 205",3)
    click("1153 660",3)
    click("1153 660",3)
    click("1067 611",3)
    click(XY_inventory_close,2)
    click(XY_inventory_close,2)
'''

def MoveOre2Company():
    click(XY_inventory,5)
    click(XY_inventory_hostcargo,2)
    click(XY_inventory_filter,2)
    click(XY_inventory_filter_ore,3)
    click(XY_inventory_selectall,2)
    click(XY_inventory_selectall,2)
    click(XY_inventory_moveto,2)
    click(XY_inventory_moveto_c1,10)
    click(XY_inventory_hostcargo,3)
    click(XY_inventory_close,2)
    click(XY_inventory_close,2)


def StoreOre():
    click(XY_inventory,8)
    click(XY_inventory_orehold,5)
    click(XY_inventory_selectall,3)
    click(XY_inventory_moveto,2)
    click(XY_inventory_moveto_c1,5)
    click(XY_inventory_hostcargo,2)
    click(XY_inventory_close,1)
    click(XY_inventory_close,2)

def ExitStation():
    click(XY_exitstation,60)
    click(XY_view_menu,1) 
    click(XY_view_onlyasteroid,2)
    WarpTo([0,1,2,3])
    #print("We are now in Asteroid Cluster")

def Return2Home():
    
    #NavigateTo(0)
    click(XY_company,12)
    click(XY_company_setnav,2)
    click(XY_inventory_close,13)
    click(XY_navigator,3)
    click(XY_view_menu,2)
    click(XY_view_onlyasteroid,2)
    time.sleep(45)
    click(XY_closeads,2)
    click(XY_closeads,2)
    StoreOre()