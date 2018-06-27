'''
Our robots like games that require the ability to calculate equations. Mission control 
recently sent them the new game to occupy their time while flying from one Island to the 
next. This game is called "Numbered Triangles". Players take 6 chips from the pile, each 
chip is made of an equilateral triangle with three numbers one on each edge. You can move, 
rotate and flip the chips so they form a hexagon. The hexagon is only legal if the adjacent 
edges for each triangle have matching numbers.

The score for a legal hexagon is the sum of the numbers on the outside six edges. The player's 
goal is to find the highest score that can be achieved with the given six chips.

numbered-triangles
Each chip is represented as a list with three positive numbers. You should help the robots find 
the highest score for the given chips and return the score as a number. If you cannot form legal 
hexagon from the chips, then return a score of 0.

Input: The chip info as a list of lists. Each list contain three integers.

Output: The highest possible score as an integer.

Example:

checkio([[1, 4, 20], [3, 1, 5], [50, 2, 3],
         [5, 2, 7], [7, 5, 20], [4, 7, 50]]) == 152
checkio([[1, 10, 2], [2, 20, 3], [3, 30, 4],
         [4, 40, 5], [5, 50, 6], [6, 60, 1]]) == 210
checkio([[1, 2, 3], [2, 1, 3], [4, 5, 6],
         [6, 5, 4], [5, 1, 2], [6, 4, 3]]) == 21
checkio([[5, 9, 5], [9, 6, 9], [6, 7, 6],
         [7, 8, 7], [8, 1, 8], [1, 2, 1]]) == 0

How it is used: This concept is used in optimization systems; you have constraints but you should 
work to get the most with these constraints. Of course this algorithm can be useful for the realisation 
of gameplay mechanics.

Precondition:
len(chips) == 6
all(all(0 < x < 100 for x in ch) for ch in chips)

我们的机器人需要能够计算方程式的游戏。任务控制
最近给他们新的游戏，以占领他们的时间，同时从一个岛屿飞往美国
下一个。这个游戏被称为“编号三角形”。玩家从堆中拿下6个筹码
芯片由等边三角形制成，每边有三个数字。你可以移动，
旋转并翻转芯片以形成六边形。只有相邻的六边形才合法
每个三角形的边缘都有匹配的数字。

法定六边形的分数是外部六个边上的数字的总和。玩家们
目标是找到用给定的六个筹码可以实现的最高分数。

编号，三角形
每个芯片都以三个正数表示。你应该帮助机器人找到
给定筹码的最高分数并将分数作为数字返回。如果你不能形成合法的
从筹码中取出六角形，然后返回0分。

输入：芯片信息作为列表的列表。每个列表包含三个整数。
输出：可能的最高分数为整数。

如何使用：这个概念用于优化系统;你有限制，但你应该
努力最大限度地利用这些限制。当然，这个算法对于实现可能是有用的
的游戏机制。

前提：
len（筹码）== 6
全部（全部（对于芯片中的ch，0 <x <100））
参照其他github
'''
import itertools
def check(chips, chip_order, rotation_order):
    total = 0
    for i in range(len(chips)):
        chip = chips[chip_order[i]]
        rotation = rotation_order[i]
        pre_chip = chips[chip_order[i-1]]
        pre_rotation = rotation_order[i-1]
        if chip[rotation[0]] != pre_chip[pre_rotation[1]]:
            return 0
        total += chip[rotation[2]]
    return total

def checkio(chips):
    per = set(r if r[0] < r[-1] else r[::-1] for r in itertools.permutations(range(1, 6), 5))
    chip_orders = [[0] + list(r) for r in per]

    rotation = itertools.permutations(range(3), 3)
    rotation_orders = list(itertools.product(rotation, repeat=6))

    return max(check(chips, chip_order, rotation_order) for chip_order in chip_orders for rotation_order in rotation_orders)

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(
        [[1, 4, 20], [3, 1, 5], [50, 2, 3],
         [5, 2, 7], [7, 5, 20], [4, 7, 50]]) == 152, "First"
    assert checkio(
        [[1, 10, 2], [2, 20, 3], [3, 30, 4],
         [4, 40, 5], [5, 50, 6], [6, 60, 1]]) == 210, "Second"
    assert checkio(
        [[1, 2, 3], [2, 1, 3], [4, 5, 6],
         [6, 5, 4], [5, 1, 2], [6, 4, 3]]) == 21, "Third"
    assert checkio(
        [[5, 9, 5], [9, 6, 9], [6, 7, 6],
         [7, 8, 7], [8, 1, 8], [1, 2, 1]]) == 0, "Fourth"
