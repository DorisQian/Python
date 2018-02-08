'''
An enormous puppy was looking down at her with large round eyes, and feebly stretching out one paw, trying to touch her. "Poor little thing!" said Alice, in a coaxing tone, and she tried hard to whistle to it; but she was terribly frightened all the time at the thought that it might be hungry, in which case it would be very likely to eat her up in spite of all her coaxing.

Hardly knowing what she did, she picked up a little bit of stick, and held it out to the puppy; whereupon the puppy jumped into the air off all its feet at once, with a yelp of delight, and rushed at the stick, and made believe to worry it; then Alice dodged behind a great thistle, to keep herself from being run over; and the moment she appeared on the other side, the puppy made another rush at the stick, and tumbled head over heels in its hurry to get hold of it; then Alice, thinking it was very like having a game of play with a cart-horse, and expecting every moment to be trampled under its feet, ran round the thistle again; then the puppy began a series of short charges at the stick, running a very little way forwards each time and a long way back, and barking hoarsely all the while, till at last it sat down a good way off, panting, with its tongue hanging out of its mouth, and its great eyes half shut.

"Alice's Adventures in Wonderland." Lewis Carroll
A stick I found that weighed two pound:
I sawed it up one day
In pieces eight of equal weight!
How much did each piece weigh?
(Everybody says “a quarter of a pound”, which is wrong.)

"Puzzles from Wonderland." Lewis Carroll
The robots want to saw the stick in several pieces. The length of the stick is N inches. We should help our robots saw the stick. All of the parts should have integer lengths (1, 2, 3 .. inches, but not 1.2). As we love the numerical series and especially the Triangular numbers (read more about Triangular numbers on Wikipedia), you should saw the stick so that the lengths form the consecutive fragment of the Triangular numbers series with the maximum quantity (fragment's length). The parts should have different lengths (no repeating). For example: 64 should divided at 15, 21, 28, because 28, 36 is shorter and 1, 3, 15, 45 is not a consecutive fragment.

You are given a length of the stick (N). You should return the list of lengths (integers) for the parts in ascending order. If it's not possible and the problem does not have a solution, then you should return an empty list.

sawing
Input: A length of the stick as an integer.

Output: A fragment of the Triangular numbers as a list of integers (sorted in ascending order) or an empty list.

Example:

checkio(64) == [15, 21, 28]
checkio(371) == [36, 45, 55, 66, 78, 91]
checkio(225) == [105, 120]
checkio(882) == []
    
How it is used: In this task you will learn about triangular numbers. A triangular number or triangle number counts the objects that form an equilateral triangle. This is an interesting sequence which has various applications.
Here’s a real world application: In a competitive tournament format that uses a round-robin group stages, the number of matches that need to be played between n teams is equal to the triangular number Tn−1. For example, a group stage with 4 teams requires 6 matches, and a group stage with 8 teams requires 28 matches.

Precondition: 0 < length < 1000

一只巨大的小狗用大圆的眼睛低头看着她，伸出一只爪子，试图触摸她。 “可怜的小东西！” “爱丽丝哄哄地说，努力地吹口哨。但是她一直以为自己可能肚子饿的时候非常害怕，在这种情况下，尽管她全身都是哄骗，但很可能会把她吃掉。

她几乎不知道她做了什么，拿起一根棍子，把它拿出来给小狗。于是小狗一下子跳了起来，一下子高兴起来，冲到了棍子上，相信让它担心起来。艾丽丝躲在一只大蓟后躲避，以防止自己被碾压;而当她出现在另一边的那一刻，小狗又匆匆地舔了一下，又匆匆忙忙地把头靠过来抓住它;然后爱丽丝觉得这很像是用马车玩游戏，期待每一刻都被踩在脚下，再次绕过蓟;然后小狗在棍子上开了一连串短暂的冲锋，每次往前走一段很长的路，然后嘶哑地吠叫，直到最后它用舌头坐下来，喘气挂在嘴边，大眼睛半闭着。

“爱丽丝梦游仙境”刘易斯·卡罗尔
我发现一根棍子重达两磅：
有一天我看到了它
在等重的八件！
每件重量多少？
（大家都说“四分之一磅”，这是错误的。）

“仙境的困惑”刘易斯·卡罗尔
机器人想要看到几根棒子。棒的长度是N英寸。我们应该帮助我们的机器人看到棍子。所有的部分应该有整数长度（1，2，3 ..英寸，但不是1.2）。因为我们喜欢数字系列，特别是三角形数字（阅读更多关于维基百科的三角形数字），所以您应该看到这个长条形成三角形数列系列中连续片段的最大数量（片段长度）。部件应该有不同的长度（不重复）。例如：64应分15,21,28，因为28,36更短，1,3,15,45不是连续的片段。

你得到一个棒（N）的长度。您应该按照升序返回零件的长度（整数）列表。如果这是不可能的，并且问题没有解决方案，那么你应该返回一个空的列表。

锯切
输入：棒的长度作为整数。
输出：三角形数字的一个片段作为整数列表（按升序排序）或空列表。

    
如何使用：在这个任务中，你将学习三角数字。三角形数字或三角形数字组成等边三角形的物体。这是一个有趣的序列，有不同的应用。
这里是一个真实世界的应用程序：在使用循环赛小组赛的比赛形式中，需要在n个小组之间进行比赛的次数等于三角形数Tn-1。例如，一个四队的小组赛需要6场比赛，而一个八场比赛的小组赛需要28场比赛。
'''


def checkio(number):
    return [number // 2, number - number // 2]

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(64) == [15, 21, 28], "1st example"
    assert checkio(371) == [36, 45, 55, 66, 78, 91], "1st example"
    assert checkio(225) == [105, 120], "1st example"
    assert checkio(882) == [], "1st example"