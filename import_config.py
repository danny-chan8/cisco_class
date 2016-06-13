#!/usr/bin/env python

import yaml
import xmltodict
from device import Device
from cli import *
#using unicodedata module to convert unicode type to string type in main
import unicodedata

def dir_bootflash(sw):
	getData = sw.show('dir bootflash:')

	show_bootflash_dict = xmltodict.parse(getData[1])

	data = show_bootflash_dict['ins_api']['outputs']['output']['body']

	static_config = 'start-config'

	print json.dumps(data, intdent=4)



