from parameter_720_1280 import *
import os,time,socket,tarfile,random
#from PIL import Image
from __main__ import devicename,oremaster

def click_single(devicename,position):
    os.system(CMD_HOSTADB + devicename + " shell input tap " + position)

