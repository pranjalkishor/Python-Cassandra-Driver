import configparser
from datetime import datetime
import time
import math

# Read astra config
def read_config():
    config = configparser.ConfigParser()
    config.read('/home/automaton/python/conf_zdm.ini')
    return config


### Unix Epoch ms
def current_milli_time():
    timenow = round(time.time() * 1000)
    # print ( "timenow: " + str(timenow) )
    # mstime = datetime.utcnow().isoformat(sep=' ', timespec='milliseconds')
    return timenow

def fromts(myts):
    # TOFIX: This is BUGGY and need to be changed. When ms is 0xx, it trims the first 0 and gives an odd value
    # ie: 2022-04-23 11:12:50.079000 becomes 2022-04-23 11:12:50:79
    tsnow = time.strftime('%Y-%m-%d %H:%M:%S:{}'.format(myts%1000), time.gmtime(myts/1000.0))
    #tsnow = datetime.fromtimestamp(myts/1000)
    #print ( "myts: " + str(myts) + " tsnow: " + str(tsnow) )
    #s = tsnow.isoformat(timespec='milliseconds')
    #print(s)
    return tsnow

### If want to test a value as a power of 10
### Too resource intensive. Better using a list (10/100/1000...)
### DEPRECATED
def isPower10 (num, base):
    if num == 0:
        return False
    elif base in {0, 1}:
        return num == base
    power = int (math.log (num, base) + 0.5)
    return base ** power == num

def dtn():
    tsp = datetime.now()
    return tsp
