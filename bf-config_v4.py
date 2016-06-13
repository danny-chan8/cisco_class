#!/usr/bin/env python

import xmltodict
from device import Device
import json
import pprint
#from cli import *



def copy_bootflash(sw):

    sw.conf('cd bootflash:')

    cp_bootflash = sw.conf('copy bootflash:/testcode/configtest.txt bootflash:')

    print cp_bootflash
    #bootflash_dict = xmltodict.parse(cp_bootflash)

    return cp_bootflash

def main():

    switch = Device(ip='172.31.217.136', username='admin', password='cisco123')
    switch.open()

    show_boot_config = copy_bootflash(switch)
    print show_boot_config
   

if __name__ == "__main__":
    main()
