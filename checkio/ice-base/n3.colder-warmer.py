'''
Let's play a game of hide and seek. You have been given a map of 10x10 cells and in one of the cells we've hidden your goal. You can move to and from any cell in the field. On each move you'll get informed if the move places you closer or further away from your goal, compared to your previous location. Your function compiles data about previous steps, each step is a list of list, where first and second elements are your coordinates (row and column) and third is the info on how much closer you've gotten (colder or warmer) -- "colder" is -1, "warmer" is 1 and "same" is 0. For your measurement of the distance to the goal you should use the Euclidean distance. At each step you need to return the coordinates for your next step. If your step places you within the goal cell, then you win! You should find the goal within 12 steps.

colder-warmer
Input: Information about previous steps as a list of lists. Each list contains coordinates and status alteration (warm, cold same).

Output: The coordinates of your new move as a list/tuple of two integers.

Example:

checkio([[2, 2, 0]])  # [0, 2]
checkio([[2, 2, 0], [0, 2, -1]])  # [3, 2]
checkio([[2, 2, 0], [0, 2, -1], [3, 2, 1]])  # [4, 1]
checkio([[2, 2, 0], [0, 2, -1], [3, 2, 1], [4, 1, 0]])  # [3, 1]

How it is used: Use this concept to find something with indirect data such as a beeping sound (like a metal detector or rad counter). This is a prediction problem and you can use it in machine learning.

Precondition: |map| = 10x10

让我们玩一个捉迷藏的游戏吧。你已经得到了一个10x10单元格的地图，并在其中一个单元格中隐藏了你的目标。你可以移动到现场的任何一个单元格。在每次移动时，如果移动的位置距离目标的距离比您之前的位置更近或更远，则会通知您。你的函数编译关于前面步骤的数据，每一步都是列表的列表，第一个和第二个元素是你的坐标（行和列），第三个是关于你接近多少（更冷或更暖）的信息 - 更冷“是-1，”温暖“是1，”相同“是0.为了测量到目标的距离，你应该使用欧几里德距离。在每一步中，您都需要返回下一步的坐标。如果你的步骤把你放在目标单元格内，那么你就赢了！你应该在12个步骤内找到目标。

冷回暖
输入：关于前面步骤的信息作为列表的列表。每个列表包含坐标和状态改变（温暖，冷的相同）。
输出：新移动的坐标作为两个整数的列表/元组。


如何使用：使用这个概念找到一些间接数据，如哔哔声（如金属探测器或拉丁计数器）。这是一个预测问题，你可以在机器学习中使用它。
'''