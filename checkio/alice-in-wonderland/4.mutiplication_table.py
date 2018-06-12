'''
Alice took up the fan and gloves, and, as the hall was very hot, she kept fanning herself 
all the time she went on talking: 'Dear, dear! How queer everything is to-day! And yesterday 
things went on just as usual. I wonder if I've been changed in the night? Let me think: was 
I the same when I got up this morning? I almost think I can remember feeling a little different. 
But if I'm not the same, the next question is, Who in the world am I? Ah, THAT'S the great puzzle!' 
And she began thinking over all the children she knew that were of the same age as herself, to 
see if she could have been changed for any of them.

"I'm sure I'm not Ada," she said, "for her hair goes in such long ringlets, and mine doesn't go 
in ringlets at all; and I'm sure I can't be Mabel, for I know all sorts of things, and she, oh! 
she knows such a very little! Besides, SHE'S she, and I'm I, and--oh dear, how puzzling it all 
is! I'll try if I know all the things I used to know. Let me see: four times five is twelve, 
and four times six is thirteen, and four times seven is--oh dear! I shall never get to twenty 
at that rate! However, the Multiplication Table doesn't signify:...

"Alice's Adventures in Wonderland." Lewis Carroll
After reading "Alice's Adventures in Wonderland," our robots decided to create their own 
"Multiplication table." Stephan would lead this mission (yeah, that probably was a bad idea). 
He forgot how to do multiplication and tried to invent a new method. It’s a rather strange 
method if we may be so blunt.

In Stephan's version of multiplication, we convert numbers to binary representation without 
leading zeroes. Then the first number is written vertically (up to down) and the second 
horizontally (left to right). With that, we fill a table with various binary operations for 
each crossing -- AND, OR, XOR, so we end up with three tables. In each table we convert rows 
to decimal and summarize it, then summarize the results of three tables. Let's look at several examples.

4 x 6 =
AND
X	1	1	0	dec	sum
1	1	1	0	6	6
0	0	0	0	0
0	0	0	0	0
OR
X	1	1	0	dec	sum
1	1	1	1	7	19
0	1	1	0	6
0	1	1	0	6
XOR
X	1	1	0	sum
1	0	0	1	1	13
0	1	1	0	6
0	1	1	0	6
6 + 19 + 13 = 38
2 x 7 =
AND
X	1	1	1	dec	sum
1	1	1	1	7	7
0	0	0	0	0
OR
X	1	1	1	dec	sum
1	1	1	1	7	14
0	1	1	1	7
XOR
X	1	1	1	sum
1	0	0	0	0	7
0	1	1	1	7
7 + 14 + 7 = 28
7 x 2 =
AND
X	1	0	dec	sum
1	1	0	2	6
1	1	0	2
1	1	0	2
OR
X	1	0	dec	sum
1	1	1	3	9
1	1	1	3
1	1	1	3
XOR
X	1	0	sum
1	0	1	1	3
1	0	1	1
1	0	1	1
6 + 9 + 3 = 18
You should help Stephan write a function to calculate this "multiplication". You are given 
two positive integers (n > 0), be careful with order of arguments.

Input: Two arguments as integers.

Output: The result of the Stephan's "multiplication", an integer.

Example:

checkio(4, 6) == 38
checkio(2, 7) == 28
checkio(7, 2) == 18
    
How it is used: In this task we play around with logical binary operations, the basis for 
computer science. Maybe you can find a use for this subject in cryptography?

Precondition: 0 < x < 100
0 < y < 100

爱丽丝拿起扇子和手套，大厅里非常热，她一直在继续说：亲爱的，亲爱的！今天一切都很奇怪！而且昨天
的情况和往常一样。我想知道我是否在夜间换了衣服？让我想想：今天早上起床的时候，我也一样吗？我几
乎认为我可以记得有点不同。但如果我不一样，接下来的问题是，我是谁？啊，这是一个伟大的谜题！她开
始思考所有她认识的和自己年纪相同的孩子，看看她们中的任何一个人是否可以改变。

“我敢肯定，我不是阿达，”她说，“因为她的头发长得很长，我的头发根本不会卷起来，而且我确定我不能成
为梅贝尔，因为我知道各种各样的事情，她，哦，她知道这么少！另外，她是她，我是我，亲爱的，这是多么
令人费解！我会试着如果我知道所有我曾经知道的事情，让我看看：五次四次十二次，四次六次十三次，四次
七次 - 哦，亲爱的，我永远不会达到二十，但乘法表不会， t表示：...

“爱丽丝梦游仙境”刘易斯·卡罗尔
在阅读“爱丽丝梦游仙境”后，我们的机器人决定创建自己的“乘法表”。斯蒂芬会领导这个任务（是的，这可能
是一个坏主意）。他忘了如何做乘法，并试图发明一种新的方法。如果我们这么直截了当，这是一个相当奇怪的方法。

在Stephan的乘法版本中，我们将数字转换为二进制表示而不用前导零。然后第一个数字垂直（从上到下）和第
二个水平（从左到右）写入。这样，我们为每个交叉点填充一个表格，包括各种二进制操作 - AND，OR，XOR，
所以我们最终得到三个表格。在每个表格中，我们将行转换为十进制并汇总，然后总结三个表的结果。我们来看几个例子。


你应该帮助斯蒂芬写一个函数来计算这个“乘法”。你给了两个正整数（n> 0），注意参数的顺序。

输入：两个参数作为整数。

输出：斯蒂芬的“乘法”的结果，一个整数。

如何使用：在这个任务中，我们玩弄逻辑二进制操作，这是计算机科学的基础。也许你可以在密码学中找到这个主题的用法？
'''


def checkio(first, second):
    first = bin(first).split('b')[1]
    second = bin(second).split('b')[1]
    #print(first, second)
    num = 0
    for f in first:
        num_and, num_or, num_xor = '', '', ''
        for s in second:
            num_and += str(int(f) & int(s))
            num_or += str(int(f) | int(s))
            num_xor += str(int(f) ^ int(s))
        num_a = int(num_and, 2)
        num_o = int(num_or, 2)
        num_x = int(num_xor, 2)
        num += num_a + num_o + num_x
    print(num)
    return num


#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(4, 6) == 38
    assert checkio(2, 7) == 28
    assert checkio(7, 2) == 18