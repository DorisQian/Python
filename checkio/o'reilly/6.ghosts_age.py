"""
Nicola takes a moment to study the ghosts. He is trying to think up a new method to determine just how old these ghosts are. He knows that their age is somehow related to their opacity. To measure their opacity Nikola uses a scale of 10000 units to 0 units, where 10000 is a completely opaque newborn ghost (0 years old) and 0 is completely transparent ghost (of an unknown age).

After some experimenting, Nikola thinks he has discovered the law of ghostly opacity. On every birthday, a ghost's opacity is reduced by a number of units equal to its age when its age is a Fibonacci number (Read about this here) or increased by 1 if it is not.

For example:
A newborn ghost -- 10000 units of opacity.
1 year -- 10000 - 1 = 9999 (1 is a Fibonacci number).
2 year -- 9999 - 2 = 9997 (2 is a Fibonacci number).
3 year -- 9997 - 3 = 9994 (3 is a Fibonacci number).
4 year -- 9994 + 1 = 9995 (4 is not a Fibonacci number).
5 year -- 9995 - 5 = 9990 (5 is a Fibonacci number).
Help Nicola write a function which will determine the age of a ghost based on its opacity. You are given opacity measurements as a number ranging from 0 to 10000 inclusively. The ghosts cannot be older than 5000 years as they simply disappear after such a long time (really!).

This is a Halloween task so you should try and write a "magic" or "scary" solution. Please, do not write "regular" solution.

Input: An opacity measurement as an integer.

Output: The age of the ghost as an integer.

Example:

checkio(10000) == 0
checkio(9999) == 1
checkio(9997) == 2
checkio(9994) == 3
checkio(9995) == 4
checkio(9990) == 5

How it is used: This task was made for some spooky fun! We hope to see your funny, tricky and creative solutions!

Precondition:
age < 5000
0 < opacity ≤ 10000

尼古拉花了一些时间研究这些鬼魂。他试图想出一个新方法来确定这些鬼的年龄。他知道他们的年龄与他们的不透明有关。为了测量它们的不透明度，Nikola使用了10000个单位到0个单位的比例，其中10000是一个完全不透明的新生鬼(0岁)，0是完全透明的鬼(一个未知的年龄)。
经过一些实验，尼古拉认为他已经发现了幽灵般的不透明的规律。在每个生日的时候，一个幽灵的不透明度会被一些单位所减少，当它的年龄是一个斐波那契数的时候(在这里读到这个)，或者如果不是的话，它会增加1个。
帮助Nicola编写一个函数，根据它的不透明度确定一个鬼的年龄。你的不透明度测量值从0到10000不等。这些鬼魂不可能超过5000年，因为它们在这么长的时间里消失了(真的!)
这是一个万圣节的任务，所以你应该尝试写一个“魔法”或“可怕的”解决方案。请不要写“常规”的解决方案。

输入:作为整数的不透明度度量。
输出:幽灵的年龄作为一个整数。

如何使用:这个任务是为了一些令人毛骨悚然的乐趣!我们希望看到你的有趣，狡猾和创造性的解决方案!
"""
def checkio(opacity):
    return 0

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(10000) == 0, "Newborn"
    assert checkio(9999) == 1, "1 year"
    assert checkio(9997) == 2, "2 years"
    assert checkio(9994) == 3, "3 years"
    assert checkio(9995) == 4, "4 years"
    assert checkio(9990) == 5, "5 years"