'''
Our Robo-Trio need to train for future journeys and treasure hunts. Stephan has built a special flat 
model of a pyramid. Now the robots can train for speed gold running. They start at the top of the pyramid 
and must collect gold in each room, choose to take the left or right path and continue down to the next level. 
To optimise their gold runs, Stephan need to know the maximum amount of gold that can be collected in one run.

Consider a tuple of tuples in which the first tuple has one integer and each consecutive tuple has one more 
integer then the last. Such a tuple of tuples would look like a triangle. You should write a program that 
will help Stephan find the highest possible sum on the most profitable route down the pyramid. All routes down 
the pyramid involve stepping down and to the left or down and to the right.

Tips: Think of each step down to the left as moving to the same index location or to the right as one index 
location higher. Be very careful if you plan to use recursion here.

sum-in-triangles

Input: A pyramid as a tuple of tuples. Each tuple contains integers.

Output: The maximum possible sum as an integer.

Example:

count_gold((
    (1,),
    (2, 3),
    (3, 3, 1),
    (3, 1, 5, 4),
    (3, 1, 3, 1, 3),
    (2, 2, 2, 2, 2, 2),
    (5, 6, 4, 5, 6, 4, 3)
)) == 23
count_gold((
    (1,),
    (2, 1),
    (1, 2, 1),
    (1, 2, 1, 1),
    (1, 2, 1, 1, 1),
    (1, 2, 1, 1, 1, 1),
    (1, 2, 1, 1, 1, 1, 9)
)) == 15
count_gold((
    (9,),
    (2, 2),
    (3, 3, 3),
    (4, 4, 4, 4)
)) == 18

 it is used: This is a classical problem which shows you how to use dynamic programming. This concept is a core component of many optimisation tasks.

Precondition: 0 < len(pyramid) ≤ 20
all(all(0 < x < 10 for x in row) for row in pyramid)

我们的机器人三重奏组需要训练未来的旅程和寻宝。 Stephan已经建造了一个特殊的公寓
金字塔的模型。现在机器人可以训练速度黄金跑步。他们从金字塔的顶端开始
并且必须在每个房间收集黄金，选择走向左侧或右侧的路径并继续下一级。
为了优化他们的黄金运行，斯蒂芬需要知道可以在一次运行中收集的最大黄金量。

考虑一个元组的元组，其中第一个元组有一个整数，每个连续的元组又有一个元组
整数然后是最后一个。这样的元组元组看起来像一个三角形。你应该写一个程序
将帮助斯蒂芬在金字塔下最有利可图的路线上找到最高的总和。所有的路线下降
金字塔涉及向下，向左或向下向右。

提示：将每一步向左移动到相同的索引位置或向右移动一个索引
位置较高。如果您打算在这里使用递归，请非常小心。

总和功能于三角形

输入：金字塔作为元组的元组。每个元组都包含整数。
输出：作为整数的最大可能和。

 它被使用：这是一个经典问题，向您展示如何使用动态编程。这个概念是许多优化任务的核心组件。
'''

def count_gold(pyramid):
    result = list(pyramid[-1])
    for line in pyramid[-2:: -1]:
        for i, val in enumerate(line):
            result[i] = val + max(result[i], result[i + 1])
        result.pop()
    return result[0]


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert count_gold((
        (1,),
        (2, 3),
        (3, 3, 1),
        (3, 1, 5, 4),
        (3, 1, 3, 1, 3),
        (2, 2, 2, 2, 2, 2),
        (5, 6, 4, 5, 6, 4, 3)
    )) == 23, "First example"
    assert count_gold((
        (1,),
        (2, 1),
        (1, 2, 1),
        (1, 2, 1, 1),
        (1, 2, 1, 1, 1),
        (1, 2, 1, 1, 1, 1),
        (1, 2, 1, 1, 1, 1, 9)
    )) == 15, "Second example"
    assert count_gold((
        (9,),
        (2, 2),
        (3, 3, 3),
        (4, 4, 4, 4)
    )) == 18, "Third example"