'''
...'And as for YOU,' she went on, turning fiercely upon the Red Queen, whom she considered as the cause of all the 
mischief--but the Queen was no longer at her side--she had suddenly dwindled down to the size of a little doll, and 
was now on the table, merrily running round and round after her own shawl, which was trailing behind her.

At any other time, Alice would have felt surprised at this, but she was far too much excited to be surprised at 
anything NOW. 'As for YOU,' she repeated, catching hold of the little creature in the very act of jumping over a 
bottle which had just lighted upon the table, 'I'll shake you into a kitten, that I will!'


CHAPTER X. Shaking

She took her off the table as she spoke, and shook her backwards and forwards with all her might. The Red Queen 
made no resistance whatever; only her face grew very small, and her eyes got large and green: and still, as Alice 
went on shaking her, she kept on growing shorter--and fatter--and softer--and rounder--and--

CHAPTER XI. Waking

--and it really WAS a kitten, after all.

"Through the Looking-Glass." Lewis Carroll
Doublets, sometimes known as Word ladder, is a word game invented by Charles Dodgson (aka Lewis Carroll). A doublets 
puzzle begins with two words. To solve the puzzle one must find a chain of different words to link the two together 
such that the two adjacent words differ by one letter.

For Example: FLOUR ⇒ FLOOR ⇒ FLOOD ⇒ BLOOD ⇒ BROOD ⇒ BROAD ⇒ BREAD

The Robots like using digits more than letters, so we’ve changed the rules a little. You are given the list of 
numbers with exactly the same length and you must find the shortest chain of numbers to link the first number to the 
last like you would with the words.

For Example. There is a list [123, 991, 323, 321, 329, 121, 921, 125, 999]. The shortest way from the first to the 
last is: 123 ⇒ 121 ⇒ 921 ⇒ 991 ⇒ 999

You should write a function that receives a list of numbers (positive integers) and returns the shortest route as a 
list of numbers.

Input: Numbers as a list of integers.

Output: The shortest chain from the first to the last number as a list of integers.

Example:

checkio([123, 991, 323, 321, 329, 121, 921, 125, 999]) == [123, 121, 921, 991, 999]
checkio([111, 222, 333, 444, 555, 666, 121, 727, 127, 777]) == [111, 121, 127, 727, 777]
checkio([456, 455, 454, 356, 656, 654]) == [456, 454, 654]  # or [456, 656, 654]
    
How it is used: This task is like pathfinding for numbers. It shows how many things in this world can be represented 
with mathematics, even words.

Precondition: Numbers have the same length
∀ x ∈ numbers : 100 ≤ x < 1000


......“至于你，”她继续说道，猛烈地转向她认为是所有恶作剧的原因的红皇后 - 但是女王已经不在她的身边了 - 她突然缩小了，一个小娃娃的大小，
现在在桌子上，高高兴兴地跑过她身后的披肩。

在其他任何时候，爱丽丝都会对此感到惊讶，但对于现在的任何事情，她都非常兴奋。 “至于你，”她重复道，抓住这个小动物跳过刚刚点亮的桌子上的一
个瓶子，“我会把你甩成一只小猫，我会的！


第十章摇晃

她说话的时候，她把她从桌子上拿了下来，全身心地向前和向后摇了摇头。红皇后没有任何抵抗，只有她的脸变得非常小，眼睛变得又大又绿，而且，
当爱丽丝继续摇着她的时候，她仍然越来越矮，越来越胖，越来越柔软，圆润，

第十一章。醒来

毕竟它真的是一只小猫

“通过镜子”。刘易斯·卡罗尔
Doublets，有时被称为Word梯，是Charles Dodgson（又名Lewis Carroll）发明的文字游戏。双拼难题从两个单词开始。为了解决这个难题，
必须找到一连串不同的单词将两者联系在一起，使得两个相邻的单词相差一个字母。

例如：FLOUR⇒FLOOR⇒FLOOD⇒BLOOD⇒BROOD⇒BROAD⇒BREAD

机器人喜欢使用数字而不是字母，所以我们已经改变了一些规则。你给出了完全相同长度的数字列表，你必须找到最短的数字链，把第一个数字和最后一个
数字链接到最后一个数字。

例如。有一个清单[123,991,323,321,329,121,921,125,999]。从第一个到最后一个最短的路是：123⇒121⇒921⇒991⇒999

你应该写一个函数，接收一个数字列表（正整数），并返回最短路径作为数字列表。

输入：数字作为整数列表。
输出：从第一个到最后一个数字的最短链，作为一个整数列表。

如何使用：这个任务就像寻找数字一样。它显示了这个世界上有多少事物可以用数学，甚至文字来表示。
'''


def checkio(numbers):
    return []

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio([123, 991, 323, 321, 329, 121, 921, 125, 999]) == [123, 121, 921, 991, 999], "First"
    assert checkio([111, 222, 333, 444, 555, 666, 121, 727, 127, 777]) == [111, 121, 127, 727, 777], "Second"
    assert checkio([456, 455, 454, 356, 656, 654]) == [456, 454, 654], "Third, [456, 656, 654] is correct too"
