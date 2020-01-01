import os
import time

undock = "700 150"
allviews = "760 400"
stopship = "471 441"

taboregroup = "230 310"
tabore = "230 130"
tabstation = "230 220"

targetlist = ["100 125","100 185","100 235","100 290"]
targetwarp = ["330 125","330 185","330 235","330 290"]
targetlock = ["330 125","330 185","330 235"]
targetwork = ["430 125","430 185","430 235"]
targetaccs = ["330 235","330 285","330 335"]
speedup = "520 560"
shiledenhence = "560 560"
middledrone1 = "620 560"
middledrone2 = "670 560"
miner = ["720 565","770 565"]

menuavatar = "45 45"
menucargo = "268 143"
cargo_shipore = "90 340"
selectallitem = "600 550"
moveitemto = "80 160"
moveitemtostationcargo = "350 150"
closepage = "770 22"
walkto = "327 278"


def click(position,waittime):
    os.system("..\\adb.exe -e shell input tap " + position)
    time.sleep(waittime)

def doubleclick(position,waittime):
    os.system("..\\adb.exe -e shell \"input tap " + position + "&sleep 0.3&" + "input tap " + position +"\"")
    time.sleep(waittime)

def warptotarget(index):
    click(targetlist[index],2)
    click(targetwarp[index],50)

def warptooregroup(index):
    click(taboregroup,1)
    warptotarget(index)

def locktarget(index):
    click(targetlist[index],2)
    doubleclick(targetlist[index],2)

def worktarget(index):
    click(targetlist[index],2)
    click(targetwork[index],4)

def walktotarget(index):
    click(targetlist[index],2)
    click(targetaccs[index],2)

def work3targets():
    click(tabore,1)
    walktotarget(0)
    locktarget(0)
    locktarget(1)
    locktarget(2)
    worktarget(0)
    worktarget(1)
    worktarget(2)

def mining():
    warptooregroup(3)
    click(shiledenhence,1)
    click(middledrone1,1)
    click(middledrone2,1)
    click(miner[0],1)
    click(miner[1],1)
    click(tabore,1)
    count = 7
    while(count > 0):
        click(speedup,1)
        walktotarget(0)
        time.sleep(5)
        click(speedup,1)
        time.sleep(30)
        

def returnstation():
    click(tabstation,1)
    warptotarget(0)
    time.sleep(20) # wait docking
    click(menuavatar,3)
    click(menucargo,5)
    click(cargo_shipore,3)
    click(selectallitem,3)
    click(moveitemto,3)
    click(moveitemtostationcargo,15)
    

def leavestation():
    click(closepage,2)
    click(undock,30)

if __name__ == "__main__":
    
    while(1):
        leavestation()
        click(allviews,2)
        mining()
        mining()
        mining()
        mining()
        returnstation()
