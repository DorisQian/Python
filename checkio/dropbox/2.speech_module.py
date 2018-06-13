'''
Stephen's speech module is broken. This module is responsible for his number pronunciation. 
He has to click to input all of the numerical digits in a figure, so when there are big numbers 
it can take him a long time. Help the robot to speak properly and increase his number processing 
speed by writing a new speech module for him. All the words in the string must be separated by 
exactly one space character. Be careful with spaces -- it's hard to see if you place two spaces instead one.

Input: A number as an integer.

Output: The string representation of the number as a string.

Example:

checkio(4)=='four'
checkio(143)=='one hundred forty three'
checkio(12)=='twelve'
checkio(101)=='one hundred one'
checkio(212)=='two hundred twelve'
checkio(40)=='forty'

How it is used: This concept may be useful for the speech synthesis software or automatic reports
 systems. This system can also be used when writing a chatbot by assigning words or phrases 
 numerical values and having a system retrieve responses based on those values.

Precondition: 0 < number < 1000

斯蒂芬的讲话模块被打破了。 这个模块负责他的数字发音。
他必须点击才能输入数字中的所有数字，所以当数字很大时
这可能需要很长时间。 帮助机器人正确说话并增加他的号码处理
通过为他写一个新的语音模块来提高速度。 字符串中的所有单词都必须用“。”隔开
恰好一个空格字符。 小心空格 - 很难看到是否放置两个空格而不是一个空格。

输入：一个数字作为整数。
输出：数字的字符串表示形式，以字符串形式表示。

如何使用：这个概念可能对语音合成软件或自动报告有用
 系统。 通过分配单词或短语来编写聊天机器人时，也可以使用该系统
  数值，并有一个系统根据这些值检索响应。
'''

FIRST_TEN = ["one", "two", "three", "four", "five", "six", "seven",
             "eight", "nine"]
SECOND_TEN = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen",
              "sixteen", "seventeen", "eighteen", "nineteen"]
OTHER_TENS = ["twenty", "thirty", "forty", "fifty", "sixty", "seventy",
              "eighty", "ninety"]
HUNDRED = "hundred"


def checkio(number):

    #replace this for solution
    return 'string representation of n'

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(4) == 'four', "1st example"
    assert checkio(133) == 'one hundred thirty three', "2nd example"
    assert checkio(12) == 'twelve', "3rd example"
    assert checkio(101) == 'one hundred one', "4th example"
    assert checkio(212) == 'two hundred twelve', "5th example"
    assert checkio(40) == 'forty', "6th example"
    assert not checkio(212).endswith(' '), "Don't forget strip whitespaces at the end of string"
