"""
In the CheckiO mission Roman Numerals you have to convert a decimal number into its representation as a roman number.
Here you have to do the same but the other way around.

You are given a roman number as a string and your job is to convert this number into its decimal representation.

A valid roman number, in the context of this mission, will only contain roman numerals as per the below table and follows the rules of the substractive notation.
Check this Wikipedia article for more details about how to form roman numerals.

Numeral	Value
I	1 (unus)
V	5 (quinque)
X	10 (decem)
L	50 (quinquaginta)
C	100 (centum)
D	500 (quingenti)
M	1,000 (mille)
Input: A roman number as a string.

Output: The decimal representation of the roman number as an int.

Example:

reverse_roman('VI') == 6
reverse_roman('LXXVI') == 76
reverse_roman('CDXCIX') == 499
reverse_roman('MMMDCCCLXXXVIII') == 3888

Precondition:
len(roman_string) > 0
all(char in "MDCLXVI" for char in roman_string) == True
0 < reverse_roman(roman_string) < 4000

在CheckiO任务罗马数字中，你必须把一个十进制数转换成一个罗马数字。

这里你要做同样的事，但是反过来。
你得到一个罗马数字作为一个字符串，你的工作是把这个数字转换成它的十进制表示。
在这个任务的范围内，一个有效的罗马数字只包含罗马数字，按照下表的规定，并遵循substractive的规则。
查阅维基百科的这篇文章，了解如何形成罗马数字的更多细节。


数值
我1(一份)
5 v(quinque)
x 10(十的)
l 50(quinquaginta)
c 100(百)
d 500(quingenti)
m 1,000(千)

输入:一个罗马数字作为字符串。
输出:罗马数字的十进制表示形式。
"""
def reverse_roman(roman_string):

    #replace this for solution
    return 0

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert reverse_roman('VI') == 6, '6'
    assert reverse_roman('LXXVI') == 76, '76'
    assert reverse_roman('CDXCIX') == 499, '499'
    assert reverse_roman('MMMDCCCLXXXVIII') == 3888, '3888'
