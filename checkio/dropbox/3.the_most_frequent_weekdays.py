'''
What is your favourite day of the week? Check if it's the most frequent day of the week in the year.

You are given a year as integer (e. g. 2001). You should return the most frequent 
day(s) of the week in that year. The result has to be a list of days sorted by the 
order of days in week (e. g. ['Monday', 'Tuesday']). Week starts with Monday.

Input: Year as an int.

Output: The list of most frequent days sorted by the order of days in week (from Monday to Sunday).

Example:

most_frequent_days(2427) == ['Friday']
most_frequent_days(2185) == ['Saturday']
most_frequent_days(2860) == ['Thursday', 'Friday']

Preconditions: Year is between 1 and 9999. Week starts with Monday.

你最喜欢的一周是哪一天？ 检查一年中是否是一周中最频繁的一天。

你有一整年的时间（例如2001年）。 你应该返回最频繁的
那一年的一周。 结果必须是按日期排序的天数列表
（例如['Monday'，'Tuesday']）。 周从周一开始。

输入：年份为整数。
输出：按星期几（从星期一到星期日）排序的最常见天数列表。

先决条件：年份介于1到9999之间。周从周一开始。
'''

def most_frequent_days(year):
    """
        List of most frequent days of the week in the given year
    """
    return ['Monday'] 

if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert most_frequent_days(2399) ==  ['Friday'], "1st example"
    assert most_frequent_days(1152) == ['Tuesday', 'Wednesday'], "2nd example"
    assert most_frequent_days(56) == ['Saturday', 'Sunday'], "3rd example"
    assert most_frequent_days(2909) == ['Tuesday'], "4th example"