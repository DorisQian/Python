'''
8-puzzle-pic 8 puzzle is a sliding puzzle that consists of a frame of randomly ordered, numbered square tiles with one missing tile. The object of the puzzle is to place the tiles in the right order (see picture) by using sliding moves to utilize the empty space. You can read more about this kind of puzzle on Wikipedia.

Our puzzle is presented as a 3x3 matrix with numbers from 1 to 8. Zero is the empty cell. You can "move" the empty cell in four directions: up--"U", down--"D", left--"L", and right--"R". You need to return a sequence of moves to solve the puzzle. The solution is presented as string of symbols ("UDLR") describing your moves.

8-puzzle

Input: A matrix with numbers from 1 to 8 as a list of lists with integers.

Output: The route of the empty cell as a string.

Example:

checkio([[1, 2, 3],
         [4, 6, 8],
         [7, 5, 0]]) == "ULDR"

How it is used: The most obvious usage for the concepts in this task lie in creating a bot to solve slide puzzles; however, this task also is a fun way to learn something new because the n-puzzle is a classical problem for modeling algorithms involving heuristics.

Precondition:
len(puzzle) == 3
all(len(row) == 3 for row in puzzle)

8-puzzle-pic 8益智游戏是一个滑动的益智游戏，由一个随机排列，编号为正方形的瓷砖和一个缺失的瓷砖组成。拼图的目的是通过使用滑动移动来利用空的空间以正确的顺序（参见图片）放置拼贴。你可以在Wikipedia上看到更多关于这种谜题的信息。

我们的难题是以1到8的数字表示的3×3矩阵。零是空单元格。您可以在四个方向上“移动”空单元格：向上 - “U”，向下 - “D”，向左 - “L”，向右 - “R”。你需要返回一系列的动作来解决这个难题。解决方案以描述您的移动的符号字符串（“UDLR”）呈现。

8拼图

输入：数字从1到8的矩阵，作为整数列表。
输出：空单元的路由作为一个字符串。

如何使用：这个任务中概念最明显的用法在于创建一个机器人来解决幻灯片拼图;然而，这个任务也是一个有趣的方式来学习新的东西，因为n-puzzle是一个涉及启发式的建模算法的经典问题。

'''


def checkio(puzzle):
    """
    Solve the puzzle
      U - up
      D - down
      L - left
      R - right
    """
    return "ULDR"


if __name__ == '__main__':
    #This part is using only for self-checking and not necessary for auto-testing
    GOAL = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]

    MOVES = {'U': (-1, 0), 'D': (1, 0), 'L': (0, -1), 'R': (0, 1)}

    def check_solution(func, puzzle):
        size = len(puzzle)
        route = func([row[:] for row in puzzle])
        goal = GOAL
        x = y = None
        for i, row in enumerate(puzzle):
            if 0 in row:
                x, y = i, row.index(0)
                break
        for ch in route:
            swap_x, swap_y = x + MOVES[ch][0], y + MOVES[ch][1]
            if 0 <= swap_x < size and 0 <= swap_y < size:
                puzzle[x][y], puzzle[swap_x][swap_y] = puzzle[swap_x][swap_y], 0
                x, y = swap_x, swap_y
        if puzzle == goal:
            return True
        else:
            print("Puzzle is not solved")
            return False

    assert check_solution(checkio, [[1, 2, 3],
                                    [4, 6, 8],
                                    [7, 5, 0]]), "1st example"
    assert check_solution(checkio, [[7, 3, 5],
                                    [4, 8, 6],
                                    [1, 2, 0]]), "2nd example"