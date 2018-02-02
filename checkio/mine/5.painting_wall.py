'''
Nicola has built a simple robot for painting of the wall. The wall is marked 
at each meter and the robot has a list of painting operations. Each operation 
describes which part of wall it needs to paint as a range from place to place, 
inclusively. For example: the operation [1, 5] means to paint the sections 
from 1 to 5 meters including sections 1 and 5. Operations are executed in the 
order they are placed in the list of operations. If the range of various operations 
are overlapped, then they must be counted once.

Stephan has prepared a list of operations, but we need to check it before the robot 
executes its painting plan. You are given the number of meters on the walls which 
need painting, (the painted zones can be separated by non painted parts) and the 
list of operations prepared by Stephan, you should determine the number of operations 
from this list required to paint the designated length of the wall. If it's 
impossible to paint that length with the given operations, then return -1.

painting-wall
Input: Two arguments.

The required length of the wall that should be painted, as integer.
A list of the operations that contains the range (inclusive) as a list of two 
integers.
Output: The minimum number of operations. If you cannot paint enough of the 
length with the given operations, return -1.

Example:

checkio(5, [[1,5], [11,15], [2,14], [21,25]]) == 1 # The first operation will paint 5 meter long.
checkio(6, [[1,5], [11,15], [2,14], [21,25]]) == 2 # The second operation will paint 5 meter long. The sum is 10.
checkio(11, [[1,5], [11,15], [2,14], [21,25]]) == 3 # After the third operation, the range 1-15 will be painted.
checkio(16, [[1,5], [11,15], [2,14], [21,25]]) == 4 # Note the overlapped range must be counted only once.
checkio(21, [[1,5], [11,15], [2,14], [21,25]]) == -1 # There are no ways to paint for 21 meters from this list.

checkio(1000000011,[[1,1000000000],[11,1000000010]]) == -1 # One of the huge test cases.
    
Hint: To handle the beginning-end of the list, you could try running a binary search.

How it is used: This skillset is often used in computer simulations.

Precondition:
0 < len(operations) ≤ 30
all(0 < x < 2 * 10 ** 18 and 0 < y < 2 * 10 ** 18 for x, y in operations)
0 < required < 2 * 10 ** 18

尼古拉已经建立了一个简单的机器人绘画的墙壁。墙上有标记
在每个米和机器人有一个绘画操作列表。每个操作
描述了它需要将哪个部分的墙绘成一个范围从一个地方到另一个地方，
包含边界。例如：操作[1,5]意味着绘制部分
从1到5米，包括第1和第5部分
为了将它们放在操作列表中。如果各种操作的范围
重叠，那么他们必须计算一次。

斯蒂芬已经准备好了一个操作列表，但是我们需要在机器人之前检查它
执行其绘画计划。你给了墙上的米数
需要绘画，（被绘的区域可以由非被绘的部分分开）和
Stephan准备的操作列表，你应该确定操作次数
从这个列表中需要绘制指定长度的墙。如果它是
不可能用给定的操作绘制该长度，然后返回-1。

画壁
输入：两个参数。

应该绘制的墙壁所需的长度，如整数。
包含范围（包含）的操作列表为两个列表
整数。
输出：最小操作数。如果你不能足够的油漆
给定操作的长度，返回-1。

提示：要处理列表的开始，可以尝试运行二分查找。
如何使用：这个技能组通常用于计算机模拟。
'''

def checkio(required, operations):
    return -1


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(5, [[1, 5], [11, 15], [2, 14], [21, 25]]) == 1, "1st"
    assert checkio(6, [[1, 5], [11, 15], [2, 14], [21, 25]]) == 2, "2nd"
    assert checkio(11, [[1, 5], [11, 15], [2, 14], [21, 25]]) == 3, "3rd"
    assert checkio(16, [[1, 5], [11, 15], [2, 14], [21, 25]]) == 4, "4th"
    assert checkio(21, [[1, 5], [11, 15], [2, 14], [21, 25]]) == -1, "not enough"
    assert checkio(1000000011, [[1, 1000000000], [11, 1000000010]]) == -1, "large"
