#!/usr/bin/env python3

import sys

def Hours():
	minute = int(sys.argv[1])
	try:
		if minute > 0:
			hour = minute // 60
			minute2 = minute % 60
			print("{} H, {} M".format(hour,minute2))
		else:
			raise ValueError
	except ValueError:
		print("ValueError：Input number cannot be negative")

if __name__ == '__main__':
	try:
		if len(sys.argv) > 1:
			Hours()
		else:
			raise ValueError
	except ValueError:
		print("缺少参数")		
		sys.exit(-1)
	sys.exit(0)
		
