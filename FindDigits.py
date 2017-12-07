#!/usr/bin/env python3

str_context = open('./String.txt')
str1 = str_context.read()
newstr = []

for i in str1:
	if i.isdigit():
		newstr.append(i)
	else:
		 continue
finalstr = "".join(newstr)
print(finalstr)

