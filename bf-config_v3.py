#!/usr/bin/env python

import xmltodict
from device import Device
import json
import pprint
#from cli import *



def copy_bootflash(sw):

	
    cp_bootflash = sw.conf('copy bootflash:start-config bootflash:/scripts/start-config_pytest15')
    #print ret_dict



# print getData

    show_bootflash_dict = xmltodict.parse(getData[1])

    #print type(show_bootflash_dict)

    data = show_bootflash_dict['ins_api']['outputs']['output']['body']

    data_dict = json.dumps(data, indent = 4)

   # print data_dict

    #print type(data_dict)

    #static_config = "start-config'\n'"

    data_dict.strip('\n')
    data_dict.replace('\n','')

    if "start-config" in data_dict:
    	print "Awesome"


    #print len(data)
    #pp = pprint.PrettyPrinter(indent = 2, depth = 6)
    #pp.pprint(data)

    #print json.dumps(data, indent=4)


def main():

    switch = Device(ip='172.31.217.134', username='admin', password='cisco123')
    switch.open()

    show_boot_config =  copy_bootflash(switch)

if __name__ == "__main__":
    main()
