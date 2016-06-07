#!/usr/bin/env python

import router
import sys

if __name__ == "__main__":

	args = sys.argv

	print args

	result1 = router.getRouter(args[1])
	print result1

	result2 = router.getRouter(args[2])
	print result2