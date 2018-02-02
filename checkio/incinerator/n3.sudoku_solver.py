'''
Sudoku is a logic-based number-placement puzzle. The objective is to fill a 
9×9 grid with digits so that each column, each row and each 3×3 sub-grid contains 
all of the digits from 1 to 9. The puzzle creator provides a partially completed 
grid, which typically has a unique solution.

For more information about this game, you should report to this site.

For example, the following grid

initial_grid gives the result: result_grid

A puzzle is represented as a list of lists with digits. A zero value means that 
the value hasn't been set.

Input: The initial 9x9 grid composed by integers as a list of lists.

Output: The result of the sudoku as a list of lists.

Example:

    checkio([[5, 0, 0, 7, 1, 9, 0, 0, 4], 
             [0, 0, 1, 0, 3, 0, 5, 0, 0], 
             [0, 0, 0, 0, 0, 0, 0, 0, 0], 
             [0, 8, 5, 9, 7, 2, 6, 4, 0], 
             [0, 0, 0, 6, 0, 1, 0, 0, 0], 
             [0, 2, 6, 3, 8, 5, 9, 1, 0], 
             [0, 0, 0, 0, 0, 0, 0, 0, 0], 
             [0, 0, 3, 0, 5, 0, 2, 0, 0], 
             [8, 0, 0, 4, 9, 7, 0, 0, 6]]) == [[5, 6, 8, 7, 1, 9, 3, 2, 4], 
                                               [9, 7, 1, 2, 3, 4, 5, 6, 8], 
                                               [2, 3, 4, 5, 6, 8, 7, 9, 1], 
                                               [1, 8, 5, 9, 7, 2, 6, 4, 3], 
                                               [3, 9, 7, 6, 4, 1, 8, 5, 2], 
                                               [4, 2, 6, 3, 8, 5, 9, 1, 7], 
                                               [6, 1, 9, 8, 2, 3, 4, 7, 5], 
                                               [7, 4, 3, 1, 5, 6, 2, 8, 9], 
                                               [8, 5, 2, 4, 9, 7, 1, 3, 6]]
    

How it is used: This is a classic constraint satisfaction problem. CSPs are 
mathematical problems defined as a set of objects whose state must satisfy a number 
of constraints or limitations. CSPs are the subject of intense research in both artificial 
intelligence and operations research, since the regularity in their formulation provides 
a common basis to analyze and solve problems of many unrelated families. 
And of course now you can use this code to help your gramma solve all of the puzzles.

Precondition: Each test case has only one unique solution.
∀ x ∈ puzzle : 0 ≤ x < 10

数独是一个基于逻辑的数字拼图游戏。目标是填补一个
9×9的数字网格，使每列，每行和每个3×3的子网格包含
所有数字从1到9.拼图创建者提供了一个部分完成
网格，通常有一个独特的解决方案。

有关这个游戏的更多信息，你应该报告给这个网站。

例如，下面的网格

initial_grid给出结果：result_grid

一个难题被表示为一个列表与数字。零值意味着
该值尚未设置。

输入：由整数组成的初始9x9网格列表。

输出：作为列表列表的数独的结果。
 
如何使用：这是一个经典的约束满足问题。 CSP是
数学问题定义为一组对象，其状态必须满足一个数字
约束或限制。 CSPs是人工研究的热门课题
情报和行动研究，因为其制定规则提供
一个共同的基础来分析和解决许多不相关的家庭的问题。
当然，现在你可以使用这个代码来帮助你的语法解决所有的难题。

先决条件：每个测试案例只有一个独特的解决方案。
'''