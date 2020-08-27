import os,time

XY_targets = ["1100 90","1100 160","1100 230","1100 300"]
XY_targets_lock = ["850 90","850 160","850 230","850 300"]
XY_targets_approach = ["850 160","850 230"]
XY_afterburner = "1230 575"
XY_stopship = "470 600"
XY_blank = "660 30"
XY_view = "1230 400"
XY_miners = ["1120 660","1230 660"]
XY_view_asteroid_cluster = "1255 145"
XY_view_asteroid = "1255 85"
XY_chat = "175 695"
XY_positions = ["435 150","435 260"] # Index 0 is home, 1 is ore
XY_positions_set = ["300 155","300 260"]
XY_navigator = "30 150"
XY_navigator_confirm = "1160 550"
XY_inventory = "63 100"
XY_inventory_orehold = "136 552"
XY_inventory_selectall = "980 650"
XY_inventory_moveto = "150 150"
XY_inventory_moveto_hanger = "500 150"
XY_inventory_close = "1235 40"
XY_exitstation = "1160 240"

# XY_targets = ["1677 127","1685 229","1100 230","1100 300"]
# XY_targets_lock = ["1280 127","1280 229","850 230","850 300"]
# XY_targets_approach = ["1288 275","1280 372"]
# XY_afterburner = "1870 860"
# XY_stopship = "737 894"
# XY_blank = "1065 30"
# XY_view = "1854 619"
# XY_miners = ["1725 993","1850 1000"]
# XY_view_asteroid_cluster = "1880 235"
# XY_view_asteroid = "1875 137"
# XY_chat = "368 1013"
# XY_positions = ["627 226","435 260"] # Index 0 is home, 1 is ore
# XY_positions_set = ["416 223","300 260"]
# XY_navigator = "50 231"
# XY_navigator_confirm = "1160 550"
# XY_inventory = "126 158"
# XY_inventory_orehold = "215 638"
# XY_inventory_selectall = "1490 987"
# XY_inventory_moveto = "250 220"
# XY_inventory_moveto_hanger = "800 257"
# XY_inventory_close = "1855 36"
# XY_exitstation = "1797 350"

def click(position,waittime):
    os.system("..\\adb.exe -e shell input tap " + position)
    time.sleep(waittime)

def ApproachTo(XY_target):
    click(XY_view_asteroid,1.5) # changed to asteriod tab
    click(XY_afterburner,1)
    click(XY_targets[XY_target],1.5)
    click(XY_targets_approach[XY_target],30)
    click(XY_afterburner,1)

def WarpTo(XY_target):
    click(XY_view,2)
    click(XY_targets[XY_target],1)
    click(XY_targets_approach[XY_target],30)

def LockTarget(XY_target):
    click(XY_targets[XY_target],1)
    click(XY_targets_lock[XY_target],1.5)

def doubleclick(position,waittime):
    os.system("..\\adb.exe -e shell \"input tap " + position + "&sleep 0.3&" + "input tap " + position +"\"")
    time.sleep(waittime)

def NavigateTo(XY_position):
    click(XY_chat,2)
    click(XY_positions[XY_position],1)
    click(XY_positions_set[XY_position],1)
    click(XY_blank,1)
    click(XY_navigator,1)
    click(XY_navigator_confirm,1)


def StoreOre():
    click(XY_inventory,4)
    click(XY_inventory_orehold,4)
    click(XY_inventory_selectall,4)
    click(XY_inventory_moveto,4)
    click(XY_inventory_moveto_hanger,4)
    click(XY_inventory_close,2)
    click(XY_inventory_close,2)
    click(XY_inventory_close,2)
    click(XY_inventory_close,2)

def ExitStation():
    click(XY_exitstation,20)
    click(XY_view,2)
    WarpTo(1)
    print("We are now in Asteroid Cluster")

def Return2Home():
    NavigateTo(0)
    time.sleep(50)
    print("We are arriving at Home")
    StoreOre()
    

def Return2LocalStation():

    ExitStation()
    
    ApproachTo(0)
    LockTarget(0)
    LockTarget(1)
    LockTarget(2)
    LockTarget(3)
    click(XY_miners[0],1)
    click(XY_miners[1],1)
    click(XY_stopship,1)
    for i in range(40):
        print(i*30,'s')
        doubleclick(XY_targets[1],1)
        time.sleep(30)
    Return2Home()


while True:
    #Return2Home()
    Return2LocalStation()
