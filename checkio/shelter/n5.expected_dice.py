'''
For this task, you'll be playing some classic tabletop games. Or rather, you're going 
to be, but first you'd like to know more about the probabilities involved in dice rolling.

Many board games fall under the category of "roll and move" games. In these games, you 
roll some dice and move that many spaces forward. You might then move forward or backwards 
a number of spaces depending on which space you land on.

Given a description of the board and the dice used, you want to work out what the expected 
number of moves would be to reach a target square. For this task, all the boards under 
consideration are circular and when moving off one end you simply continue from the other. 
A board is represented as a list of integers. Each cell number means how many cells to move 
(positive for forward, negative for backwards) after landing on that cell. You always start 
from the first cell (index 0) and the starting and target squares will not require any further 
movement after landing on them.

For example: If we have one 4-sided die, the simple board [0,0,0,0] and any target square, 
then you have a 1/4 chance of reaching the target on every roll, so on average it will take 
4 rolls. The result should be given with one digit precision as ±0.1.

Input: A number of dice to roll as an integer, the number of sides on each die as an integer, 
a target space as an integer and a board as a list of integers.

Output: The expected number of moves needed to reach the target space starting from space 0, 
correct to 1 digit after the decimal place. If it takes 33 1/3 moves, you should return 33.3. 
All test cases have a finite expected number of moves.

Example:

expected(1, 4, 3, [0, 0, 0, 0]) == 4.0   # On these first three, you have a 1/4 chance of reaching the target
expected(1, 4, 1, [0, 0, 0, 0]) == 4.0   # on every roll, so on average it will take 4 rolls.
expected(1, 4, 3, [0, -1, -2, 0]) == 4.0
expected(1, 4, 3, [0, 2, 1, 0]) == 1.3   # You have a 3/4 chance of reaching the exit and 1/4 
chance of ending up where you started
expected(1, 6, 1, [0] * 10) == 8.6
expected(2, 6, 1, [0] * 10) == 10.2

How it is used: Some of the methods for solving this task can be used to tackle a wide variety of other problems.

Preconditions:
1 ≤ dice_number ≤ 3
2 ≤ sides ≤ 10
0 < target < len(board)
4 ≤ len(board) ≤ 30
board[0] == 0
board[target] == 0
all(board[(i + board[i]) % len(board)] == 0 for i in range(len(board)))

为了这个任务，你会玩一些经典的桌面游戏。或者说，你要走了
是，但首先你想更多地了解骰子滚动涉及的概率。

许多棋盘游戏属于“滚动和移动”游戏类别。在这些游戏中，你
滚动一些骰子并向前移动那么多空间。你可能会前进或后退
取决于您登陆的空间有多个空间。

鉴于董事会和所使用的骰子的描述，你想弄清楚什么是预期的
移动次数将达到目标广场。对于这个任务，所有的委员会
考虑是循环的，当你离开一端时，你只需从另一端继续。
董事会被表示为一个整数列表。每个单元格编号意味着要移动多少个单元格
（前向为正向，后向为负向）。你总是开始
从第一个单元格（索引0）开始，目标方格将不再需要
运动后登陆他们。

例如：如果我们有一个4面模具，简单的板[0,0,0,0]和任何目标方格，
那么你在每次掷骰时都有1/4的机会达到目标，所以平均来说它会占用
4卷。结果应以±0.1的一位数字精度给出。

输入：多个骰子以整数形式滚动，每个骰子上的边数为整数，
一个目标空间作为一个整数，一个棋盘作为一个整数列表。

输出：从空间0开始到达目标空间所需的移动的预期数量，
纠正小数点后1位数字。如果它需要33次1/3的移动，你应该返回33.3。
所有测试用例的移动次数都是有限的。


它是如何使用的：解决这个任务的一些方法可以用来解决各种各样的其他问题。

前提条件：
1≤dice_number≤3
2≤边≤10
0 <目标<len（板）
4≤len（板）≤30
板[0] == 0
板[目标] == 0
所有（board [（i + board [i]）％len（board）] == 0我在范围内（len（board）））
'''