'''
Sometimes humans build weird things. Our Robots have discovered and wish to use 
an ancient circular cannon loading system. This system looks like numbered pipes 
arranged in a circular manner. There is a rotating mechanism behind these pipes, 
and the cannons are attached to the end. This system is incredibly ancient and some 
of the cannons are broken. The loading automaton has a program with the pipe numbers 
which indicate where it should place cannonballs. These numbers cannot be changed 
as they are engraved into the pipes. We can, however, rotate the backend mechanism 
to change the correspondence between pipes and cannons. We should find each combination 
that we can rotate the backend mechanism so that all loaded cannonballs will be loaded 
into the still-working cannons. The loading automaton will load all of the balls simultaneously.

The pipes are numbered from 0 to N-1. The initial positions of the backend mechanism 
are represented as an array with 1 and/or 0. Each element describes a cannon behind the 
pipe; the 0th element describe 0th pipe. 1 is a working cannon and 0 is a broken cannon.

You know the pipe numbers where the automaton will load cannonballs (sometimes it loads 
several cannonballs into one cannon). Your goal is to find all the combinations that you 
can rotate the backend mechanism in a clockwise manner so that all of the cannonballs 
will be loaded into the working cannons. Rotation is described as an integer - how many 
units you should rotate clockwise. The result should be represented as a list of integers 
(variants) in the ascending order. The case when you don't need to rotate are described 
as 0 (but don't forget about other variants). If it's not possible to find a solution, then return [].

For example, the initial state is [1,0,0,0,1,1,0,1,0,0,0,1] and pipes numbers are [0,1]. 
If you rotate the mechanism by 1 or 8 units, then all balls which are be placed in the 0th 
and 1st pipes will be in cannons.

floor
Input: Two arguments.

A initial state as a list with 1 and/or 0
Pipe numbers for cannonballs as a list of integers
Output: The rotating variants as a list of integers or an empty list.

Example:

rotate([1, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 1], [0, 1]) == [1, 8]
rotate([1, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 1], [0, 1, 2]) == []
rotate([1, 0, 0, 0, 1, 1, 0, 1], [0, 4, 5]) == [0]
rotate([1, 0, 0, 0, 1, 1, 0, 1], [5, 4, 5]) == [0, 5]
    
How it is used: This concept will acquaint you with circular data structures.

Precondition:
3 ≤ len(state) < 100
all(0 ≤ n < len(state) for n in pipe_numbers)

有时人类会造出奇怪的东西。我们的机器人已经发现并希望使用
一个古老圆形大炮装载系统。这个系统看起来像编号管道
以循环方式排列。这些管子后面有一个旋转机构，
大炮连接到最后。这个系统是非常古老的和一些
大炮被打破了。加载自动机有一个管道编号的程序
这表明它应该在哪里放置炮弹。这些数字不能改变
因为它们被刻在管道中。但是，我们可以旋转后端机制
改变管道和大炮之间的对应关系。我们应该找到每个组合
我们可以旋转后端机制，以便加载所有加载的炮弹
进入仍在运作的大炮。加载自动机将同时加载所有的球。

管道编号从0到N-1。后端机制的初始位置
被表示为1和/或0的数组。每个元素描述了后面的一个炮
管;第0个元素描述第0个管道。 1是一个工作的大炮，0是一个破的大炮。

你知道自动机将加载炮弹的管道号码（有时会加载
几个炮弹变成一个大炮）。你的目标是找到你所有的组合
可以顺时针旋转后端机构，使所有的炮弹
将被装入工作大炮。旋转被描述为一个整数 - 多少个
你应该顺时针旋转单位。结果应该被表示为一个整数列表
（变体）按升序排列。描述了不需要旋转的情况
作为0（但不要忘记其他变体）。如果找不到解决方案，则返回[]。

例如，初始状态是[1,0,0,0,1,1,0,1,0,0,0,1]，管道编号是[0,1]。
如果您将机构旋转1或8个单位，则将所有球放置在0号
第一管将在大炮。

地板
输入：两个参数。

初始状态为1和/或0的列表
炮弹的管道号码作为整数列表
输出：旋转变体作为整数列表或空列表。

如何使用：这个概念将使您了解循环数据结构。
'''

def rotate(state, pipe_numbers):
    return []


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert rotate([1, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 1], [0, 1]) == [1, 8], "Example"
    assert rotate([1, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 1], [0, 1, 2]) == [], "Mission impossible"
    assert rotate([1, 0, 0, 0, 1, 1, 0, 1], [0, 4, 5]) == [0], "Don't touch it"
    assert rotate([1, 0, 0, 0, 1, 1, 0, 1], [5, 4, 5]) == [0, 5], "Two cannonballs in the same pipe"