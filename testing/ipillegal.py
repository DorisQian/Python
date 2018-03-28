# !/usr/bin/env python3
# -*- coding=utf-8 -*-

import re

def ip_judge(ip):
	ip_legal = re.compile('^((25[0-5]|2[0-4]\d|[1]?\d\d?)\.){3}(25[0-5]|2[0-4]\d|[1]?\d\d?)$')
	if ip_legal.match(ip):
		return True
	else:
		return False


def ip_judge2(ip):
	if '.' not in ip:
		return False
	elif ip.count('.') != 3:
		return False
	else:
		number = ip.split('.')
		for n in number:
			if n.isdigit() is False:
				return False
			elif int(n) < 1 or int(n) > 255:
				return False
	return True

if __name__ == '__main__':
	ip = '172.17.1.9df'
	print(ip_judge(ip))
	print(ip_judge2(ip))	

