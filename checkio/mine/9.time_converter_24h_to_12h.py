'''
You prefer a good old 12-hour time format. But the modern world we live in would rather use the 24-hour format and you see it everywhere. Your task is to convert the time from the 24-h format into 12-h format by following the next rules:
- the output format should be 'hh:mm a.m.' (for hours before midday) or 'hh:mm p.m.' (for hours after midday)
- if hours is less than 10 - don't write a '0' before it. For example: '9:05 a.m.'
Here you can find some useful information about the 12-hour format.

example

Input: Time in a 24-hour format (as a string).

Output: Time in a 12-hour format (as a string).

Example:

time_converter('12:30') == '12:30 p.m.'
time_converter('09:00') == '9:00 a.m.'
time_converter('23:15') == '11:15 p.m.'

How it is used: For work with the different time formats.

Precondition:
'00:00' <= time <= '23:59'

你更喜欢一个很好的12小时时间格式。 但我们生活的现代世界宁愿使用24小时制，而且你到处都可以看到它。 
您的任务是按照以下规则将时间从24小时格式转换为12小时格式：
- 输出格式应该是'hh：mm a.m.' （中午前数小时）或'hh：mm pm。' （中午后数小时）
- 如果小时数小于10，则不要在其前写入“0”。 例如：'9:05 a.m.'
在这里你可以找到一些关于12小时格式的有用信息。
'''

def time_converter(time):
    #replace this for solution
    if int(time.split(':')[0]) < 12:
    	if time.split(':')[0] == '00':
    		result = '12' + ':' + time.split(':')[1] + ' ' + 'a.m.'
    	else:
    		result = time.lstrip('0') + ' ' + 'a.m.'
    elif int(time.split(':')[0]) == 12:
    	result = time + ' ' + 'p.m.'
    else:
    	result = str(int(time.split(':')[0]) - 12) + ':' + time.split(':')[1] + ' ' + 'p.m.'
    return result

if __name__ == '__main__':
    print("Example:")
    print(time_converter('12:30'))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert time_converter('12:30') == '12:30 p.m.'
    assert time_converter('09:00') == '9:00 a.m.'
    assert time_converter('23:15') == '11:15 p.m.'
    assert time_converter('00:12') == '12:12 a.m.'
    print("Coding complete? Click 'Check' to earn cool rewards!")