'''
We have prepared a set of Editor's Choice Solutions. You will see them first 
after you solve the mission. In order to see all other solutions you should change the filter.
abacus
For the Robots the decimal format is inconvenient. If they need to count to "1", 
their computer brains want to count it in the binary representation of that number. 
You can read more about binary here.

You are given a number (a positive integer). You should convert it to the binary 
format and count how many unities (1) are in the number spelling. For example: 5 = 0b101 
contains two unities, so the answer is 2.

Input: A number as a positive integer.

Output: The quantity of unities in the binary form as an integer.

Example:

checkio(4) == 1
checkio(15) == 4
checkio(1) == 1
checkio(1022) == 9

How it is used: How to convert a number to the binary form. It can be useful for Computer 
Science purposes.

Precondition: 0 < number ≤ 232

Guido van Rossum, the author of Python, is one of our most famous player. He is writing some 
really wonderful code reviews for our player solutions.

我们编写了一套编辑选择解决方案。 你会先看到他们
你解决任务后 为了看到所有其他的解决方案，你应该改变过滤器。
算盘
对于机器人来说，十进制格式不方便。 如果他们需要数到“1”，
他们的计算机大脑想把它算在这个数字的二进制表示中。
你可以在这里阅读更多关于二进制。

给你一个数字（一个正整数）。 你应该把它转换成二进制
格式并统计数字拼写中有多少统一体（1）。 例如：5 = 0b101
包含两个统一，所以答案是2。

输入：一个数字作为正整数。
输出：二进制形式的统一的数量作为一个整数。

如何使用：如何将数字转换为二进制形式。 它可以用于计算机科学目的。

Python的作者Guido van Rossum是我们最着名的玩家之一。 他正在写一些
我们的播放器解决方案真的很棒
'''

def checkio(number):
    return bin(number).count('1')

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(4) == 1
    assert checkio(15) == 4
    assert checkio(1) == 1
    assert checkio(1022) == 9
