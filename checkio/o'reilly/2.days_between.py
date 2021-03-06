"""
We have prepared a set of Editor's Choice Solutions. You will see them first after 
you solve the mission. In order to see all other solutions you should change the filter.
How old are you in number of days? It's easy to calculate - just subtract your birthday 
from today. We could make this a real challenge though and count the difference between any dates.

You are given two dates as tuples with three numbers - year, month and day. For example: 
19 April 1982 will be (1982, 4, 19). You should find the difference in days between the 
given dates. For example between today and tomorrow = 1 day. The difference will always 
be either a positive number or zero, so don't forget about absolute value.

Input: Two dates as tuples of integers.

Output: The difference between the dates in days as an integer.

Example:

days_diff((1982, 4, 19), (1982, 4, 22)) == 3
days_diff((2014, 1, 1), (2014, 8, 27)) == 238
days_diff((2014, 8, 27), (2014, 1, 1)) == 238
    

How it is used: Python has batteries included, so in this mission you will need to 
learn how to use completed modules so that you don't have to invent the bicycle all over again.

Precondition: Dates between 1 january 1 and 31 december 9999. Dates are correct.

我们已经准备了一套编辑器的选择方案。在你解决了任务之后，你将会看到他们。为了看到所有
其他的解决方案，你应该改变过滤器。
你多少岁了?这很容易计算——只要把你的生日从今天算起就行了。我们可以让这成为一个真正的挑战，
并计算任何日期之间的区别。
你有两个日期作为元组与三个数字-年，月和日。例如:1982年4月19日是(1982年4月19日)。你应该在
规定的日期之间找到不同的日期。例如今天和明天= 1天。差值总是正数或零，所以别忘了绝对值。

输入:两个日期为整数的元组。
输出:日期作为整数的日期之间的差异。

它是如何使用的:Python有电池，所以在这个任务中，你需要学习如何使用完成的模块，这样你就不用再
重新发明自行车了。

先决条件:日期为1月1日至12月31日。日期是正确的。
"""

import datetime
def days_diff(date1, date2):
	def count_leap(year):
		leep_year = []
		for i in range(1, year + 1):
			if i % 100 != 0 and i % 4 == 0:
				leep_year.append(i)
			if i % 100 == 0 and i % 400 == 0:
				leep_year.append(i)
		#print(leep_year, len(leep_year))
		return len(leep_year)
	if date1 > date2:
		a, b = date1, date2
		date1 = b
		date2 = a
	year1, year2= date1[0], date2[0]
	if year1 >= 1000:
		date1 = str(date1[0]) +'-' + str(date1[1]) +'-' + str(date1[2])
		date2 = str(date2[0]) +'-' + str(date2[1]) +'-' + str(date2[2])
		
	if year2 < 1000:
		date1 = str(date1[0] + 999) +'-' + str(date1[1]) +'-' + str(date1[2])
		date2 = str(date2[0] + 999) +'-' + str(date2[1]) +'-' + str(date2[2])

	if year1 < 1000 and year2 >= 1000:
		date1 = str(date1[0] + 999) +'-' + str(date1[1]) +'-' + str(date1[2])
		if year2 <= 9000:
			date2 = str(date2[0] + 999) +'-' + str(date2[1]) +'-' + str(date2[2])
		else:
			date2 = str(date2[0]) +'-' + str(date2[1]) +'-' + str(date2[2])

	d1 = datetime.datetime.strptime(date1, '%Y-%m-%d').date()
	d2 = datetime.datetime.strptime(date2, '%Y-%m-%d').date()
	
	if year2 < 1000:
		y1 = count_leap(year1)
		y2 = count_leap(year2)
		leap1 = y2 - y1
		leap2 = count_leap(year2 + 1000) - count_leap(year1 + 1000)
		return abs((d1 - d2).days) + leap2 - leap1

	elif year2 > 1000 and year1 < 1000:
		if year2 <= 9000:
			leap1 = count_leap(year2) - count_leap(year1)
			leap2 = count_leap(year2 + 1000) - count_leap(year1 + 1000)
			print(abs((d1 - d2).days) + leap2 - leap1)
			return abs((d1 - d2).days) + leap2 - leap1
		else:
			leap1 = count_leap(year1)
			leap2 = count_leap(999 + year1)
			print(abs((d1 - d2).days) + leap2 - leap1 + 999 * 365 )
			return abs((d1 - d2).days) + leap2 - leap1 + 999 * 365 
	else:
		print(abs((d1 - d2).days))
		return abs((d1 - d2).days)
	
	
if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    
    assert days_diff((1982, 4, 19), (1982, 4, 22)) == 3
    assert days_diff((2014, 1, 1), (2014, 8, 27)) == 238
    assert days_diff((2014, 8, 27), (2014, 1, 1)) == 238
    assert days_diff((1,1,1), (9999,12,31)) == 3652058
    assert days_diff((9999,12,31), (1,1,1)) == 3652058
    assert days_diff((696,5,7), (9241,6,27)) == 3121048