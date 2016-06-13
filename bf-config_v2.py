#!/usr/bin/env python

import xmltodict
from device import Device
import json
import pprint
#from cli import *



def show_bootflash(sw):

    getData = sw.conf('dir bootflash:')

# print getData

    show_bootflash_dict = xmltodict.parse(getData[1])

    #print type(show_bootflash_dict)

    data = show_bootflash_dict['ins_api']['outputs']['output']['body']

    data_dict = json.dumps(data, indent = 4)

    print data_dict

    #print type(data_dict)

    if "static_config" in data_dict:
    	print "Awesome"

   # for key, value in data.iteritems():
    #	print "This is the key: ", key

    #print len(data)
    #pp = pprint.PrettyPrinter(indent = 2, depth = 6)
    #pp.pprint(data)

    #print json.dumps(data, indent=4)


def main():

    switch = Device(ip='172.31.217.134', username='admin', password='cisco123')
    switch.open()

    show_boot_config = show_bootflash(switch)

if __name__ == "__main__":
    main()
