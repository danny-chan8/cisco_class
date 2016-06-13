#!/usr/bin/env python

import xmltodict
from device import Device
from cli import *


getData = sw.show('dir bootflash:')

show_bootflash_dict = xmltodict.parse(getData[1])

data = show_bootflash_dict['ins_api']['outputs']['output']['body']

static_config = 'start-config'

print json.dumps(data, intdent=4)



