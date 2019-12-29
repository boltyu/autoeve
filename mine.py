import os
import time

undock = "700 150"
allviews = "760 400"
stopship = "471 441"

taboregroup = "230 310"
tabore = "230 130"
tabstation = "230 220"

targetlist = ["100 125","100 185","100 235"]
targetwarp = ["330 125","330 185","330 255"]
targetlock = ["330 125","330 185","330 255"]
targetwork = ["430 125","430 185","430 255"]
targetaccs = ["330 235","330 285","330 335"]
lightdrone = "620 565"
laserminer = ["670 565","670 565","670 565"]

menuavatar = "45 45"
menucargo = "268 143"
cargo_shipore = "90 340"
selectallitem = "600 550"
moveitemto = "80 160"
moveitemtostationcargo = "350 150"
closepage = "770 22"
walkto = "327 278"


def click(position,waittime):
    os.system(".。\\adb.exe -e shell input tap " + position)
    time.sleep(waittime)

def doubleclick(position,waittime):
    os.system(".。\\adb.exe -e shell \"input tap " + position + "&sleep 0.3&" + "input tap " + position +"\"")
    time.sleep(waittime)

def warptotarget(index):
    click(targetlist[index],2)
    click(targetwarp[index],40)

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
    warptooregroup(2)
    click(lightdrone,1)
    count = 5
    while(count > 0):
        work3targets()
        work3targets()
        count = count - 1

def returnstation():
    click(tabstation,1)
    warptotarget(0)
    time.sleep(20) # wait docking
    click(menuavatar,2)
    click(menucargo,5)
    click(cargo_shipore,2)
    click(selectallitem,2)
    click(moveitemto,2)
    click(moveitemtostationcargo,20)
    

def leavestation():
    click(closepage,2)
    click(undock,30)

if __name__ == "__main__":
    
    while(1):
        leavestation()
        click(allviews,2)
        mining()
        mining()
        returnstation()
