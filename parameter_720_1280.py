import os

XY_targets = ["1100 90","1100 160","1100 230","1100 300"]
XY_targets_lock = ["850 90","850 160","850 230","850 300"]
XY_targets_mine = ["680 90","680 160","680 230","680 300"]
XY_targets_approach = ["850 160","850 230","850 300","850 380"]
XY_afterburner = "1230 575"
XY_stopship = "470 600"
XY_blank = "660 30"
XY_view = "1229 402"
XY_miners = ["1120 660","1230 660","1060 660"]
XY_view_menu = "1043 28"
XY_view_asteroidandcluster = "1043 125"
XY_view_onlyasteroid = "1043 200"
XY_chat = "175 695"
XY_chat_positions = ["435 150","435 260"] # Index 0 is home, 1 is ore
XY_chat_positions_set = ["300 155","300 260"]
XY_navigator = "30 150"
XY_navigator_confirm = "1160 550"
XY_company = "185 100"
XY_company_setnav = "410 655"
XY_inventory = "63 100"
XY_inventory_filter = "1100 655"
XY_inventory_filter_ore = "1100 495"
XY_inventory_orehold = "136 552"
XY_inventory_selectall = "980 650"
XY_inventory_moveto = "150 150"
XY_inventory_moveto_c1 = "530 400"
XY_inventory_moveto_hostcargo = "500 150"
XY_inventory_close = "1235 40" # global close
XY_inventory_hostcargo = "125 195"
XY_inventory_item1 = "415 195"
XY_inventory_item1_moveto = "1120 100"
XY_inventory_item1_moveto_subtab ="1255 315"
XY_inventory_item1_moveto_subtab_orecargo = "1170 90"
XY_inventory_item1_moveto_setmax = "1240 265"
XY_inventory_item1_moveto_setmax_confirm = "1200 625"
XY_inventory_item1_moveto_shipcargo = "1025 340"
XY_inventory_shipcargo = "140 460"
XY_closeads = "1090 113"
XY_exitstation = "1160 240"
XY_planet_item_extend = "1200 125"
XY_planet = "254 114"
XY_planet_items = ["138 166","138 296","138 418","138 510","138 630","138 710"]
XY_planet_reject_autonav = "932 550"
XY_planet_item_launch = ["1200 285","1200 370","1200 450","1200 530"]
XY_inventory_collapse_tabstation = "125 101"
XY_inventory_currentship = "140 456"
XY_inventory_imicas = "140 493"
XY_inventory_chongfeng = "140 565"
XY_inventory_imicas_active = "45 493"
XY_inventory_chongfeng_active= "45 565"
CMD_HOSTADB = "adb.exe -s "
CMD_HOSTADB_GENERAL = "adb.exe "
if os.system("uname") == 0:
	CMD_HOSTADB = "./adb -s "
	CMD_HOSTADB_GENERAL = "./adb "

    

# rr = vars(XY_POS_1280_720)
# listsome = ['1','2']
# for i in rr:
#     if('__' not in i):
#         if(type(rr[i]) == type("str")):
#             vv = rr[i].split()
#             print(i,'=',"'"+str(int(int(vv[0])/0.666))+" "+str(int(int(vv[1])/0.666))+"'")
#          XY_view = "1230 400"   pass
#         elif(type(rr[i]) == type(listsome)):
#             tmpstr = ''
#             for j in rr[i]:
#                 vv = j.split()
#                 tmpstr = tmpstr + "'"+str(int(int(vv[0])/0.666))+" "+str(int(int(vv[1])/0.666))+"',"
#             print(i,'=','[' + tmpstr + ']')
#             pass
    
