#!/usr/bin/env python3

import sys

def Hours():
	minute = int(input())
	try:
		hour = minute // 60
		minute2 = minute % 60
	except ValueError:
		print("ValueError：Input number cannot be negative")
	return hour, minute2
	print(" {} H. {} M".formate(hour, minute2)

if __name__ == '__main__':
	if len(sys.argv) > 2:
		Hours()
	else:
		sys.exit(-1)
	sys.exit(0)
		
