
#!/usr/bin/env python3
from eye import *
import random
#define SPEED    360
#define ASPEED    45
#define THRES    175
SPEED=360
ASPEED=45
THRES=175
SAFE = 1000
TERUS=500
LCDMenu("GO","","","END")

while (KEYRead() !=KEY4):
    direc = int ((random.random()-0.7) * 3+random.random())  # [-0.5 .. +0.5] * 360
    print(direc)
    VWTurn(direc, 90)
    VWWait()
    VWStraight(100,330)
    VWWait()
    print("PSD")
    print(PSDGet(1))
    if PSDGet(1)<1500:
        VWTurn(60, 80)
        VWWait()
    elif PSDGet(4)>800:
        OSWait(700)
        VWWait()
    else:
        VWStraight(150,330)
        VWWait()

# S4 3500 4000 0 worker.py
# S4 3200 4000 0 worker.py
# S4 2900 4000 0 worker.py


 

       
       