import os,sys,random,time
from parameter_720_1280 import *
devicename = "192.168.43.1:5555"
def click(position,waittime):
    x,y = position.split(' ')
    x = str(int(x) + random.randrange(-4,4)) + '.' + str(random.randrange(0,9))
    y = str(int(y) + random.randrange(-4,4)) + '.' + str(random.randrange(0,9))
    os.system(CMD_HOSTADB + devicename + " shell input tap " + x + ' ' + y)
    time.sleep(waittime+random.randrange(0,4))
lockcount = 0
while(True):
    if(lockcount < 3):
        lockcount += 1
        click(XY_battle_lockall,random.randrange(20,40))
        for i in range(3):
            click(XY_miners[i],1);
    else:
        lockcount = 0
        click(XY_battle_target1,1)
        click(XY_battle_fire1,1)
    