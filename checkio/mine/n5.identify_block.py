'''
This mission uses a 4x4 grid. Each square is numbered from 1 to 16 in row-major order.
You are given 4 numbers (set of integer). These numbers represent the position of 
the square on the grid and one block if all the squares are adjacent.

You have to identify the kind of block. (Refer to the following image or comment 
of initial code for the kind of block).
The answer is an upper case alphabet ('I', 'J', 'L', 'O', 'S', 'T' or 'Z'). If it 
isn't a block then return None.

The block is placed anywhere on the grid and can be rotated (0, 90, 180 or 270 degrees).

Input: 4 numbers (set of integer)

Output: kind of the block (an alphabet or None )

Example:

identify_block({1, 2, 3, 4}) == 'I'
identify_block({1, 2, 3, 6}) == 'T'
identify_block({1, 5, 6, 10}) == 'S'


How it is used:
Creating a tetromino puzzle.

Precondition:
len(input) == 4
all(1 <= num <= 16 for num in input)
output in ('I', 'J', 'L', 'O', 'S', 'T', 'Z', None )

这个任务使用4x4网格。 每个正方形按主要顺序从1到16进行编号。
给你4个数字（一组整数）。 这些数字代表的位置
如果所有的方块都相邻，则网格上的正方形和一个方块。

你必须确定块的类型。 （请参阅下面的图像或评论
的类型的初始代码）。
答案是大写字母（'I'，'J'，'L'，'O'，'S'，'T'或'Z'）。 如果它
不是一个块，然后返回None。

该块放置在网格上的任何位置，并可以旋转（0,90,180或270度）。

输入：4个数字（整数集合）
输出：块的种类（字母或无）

如何使用它：
创建一个tetromino拼图。
'''
