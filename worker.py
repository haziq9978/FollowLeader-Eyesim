#!/usr/bin/env python3
from eye import *
import random
#define SPEED    360
#define ASPEED    45
#define THRES    175
SPEED=360
TERUS=200
THRES=175
SAFE = 3000
LCDMenu("GO","","","END")

while (KEYRead() !=KEY4):
    
    if PSDGet(1)<1000 :
      if PSDGet(1)<300:
        VWStraight(100,150)
        VWWait()
      else:
        VWStraight(100,450)
        VWWait()
    # elif PSDGet(1)<200:
    #   OSWait(40)
    #   VWStraight(100,300)
    else:
      if PSDGet(7)<1000:
        VWTurn(17, 300)
        VWWait()
        VWStraight(100,400)
        VWWait()
      elif PSDGet(8)<1000:
        VWTurn(-17, 300)
        VWWait()
        VWStraight(100,400)
        VWWait()
      else:
        VWStraight(100,150)
        VWWait()
      
    
    