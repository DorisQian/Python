"""
On the chest keypad is a grid of numbered dots. The grid is comprised of a square shaped array of dots and contains lines that connect some pairs of adjacent dots. The answer to the code is the number of squares that are formed by these lines. For example, in the figure shown below, there are 3 squares: 2 small squares and 1 medium square.



The dots are marked by the numbers 1 through 16. The endpoints of the lines are represented by lists of two numbers.

Input: A list of lines as a list of list. Each list consists of the two integers.

Output: The quantity of squares formed as an integer.

Example:

checkio([[1, 2], [3, 4], [1, 5], [2, 6], [4, 8], [5, 6], [6, 7],
     [7, 8], [6, 10], [7, 11], [8, 12], [10, 11],
     [10, 14], [12, 16], [14, 15], [15, 16]]) == 3
checkio([[1, 2], [2, 3], [3, 4], [1, 5], [4, 8],
     [6, 7], [5, 9], [6, 10], [7, 11], [8, 12],
     [9, 13], [10, 11], [12, 16], [13, 14], [14, 15], [15, 16]]) == 2

How it is used: This is a simple puzzle that illustrates pattern searching. For complex cases you can improve your program and use it to search for more complex patterns, shapes and objects.

Precondition:
0 < len(lines) ≤ 32

在胸前的键盘上是一个有数字的网格。该网格由一个方形的点组成，其中包含一些连接相邻点的线。代码的答案是由这些行组成的平方数。例如，在下面的图中，有3个正方形:2个小正方形和1个中正方形。
这些点的标记是1到16。行的端点由两个数的列表表示。

输入:作为列表列表的行列表。每个列表由两个整数组成。
输出:作为整数组成的正方形的数量。

如何使用:这是一个简单的拼图，演示了模式搜索。对于复杂的情况，您可以改进程序并使用它来搜索更复杂的模式、形状和对象。
"""
def checkio(lines_list):
    """Return the quantity of squares"""
    return 0


if __name__ == '__main__':
    assert (checkio([[1, 2], [3, 4], [1, 5], [2, 6], [4, 8], [5, 6], [6, 7],
                     [7, 8], [6, 10], [7, 11], [8, 12], [10, 11],
                     [10, 14], [12, 16], [14, 15], [15, 16]]) == 3), "First, from description"
    assert (checkio([[1, 2], [2, 3], [3, 4], [1, 5], [4, 8],
                     [6, 7], [5, 9], [6, 10], [7, 11], [8, 12],
                     [9, 13], [10, 11], [12, 16], [13, 14], [14, 15], [15, 16]]) == 2), "Second, from description"
    assert (checkio([[1, 2], [1, 5], [2, 6], [5, 6]]) == 1), "Third, one small square"
    assert (checkio([[1, 2], [1, 5], [2, 6], [5, 9], [6, 10], [9, 10]]) == 0), "Fourth, it's not square"
    assert (checkio([[16, 15], [16, 12], [15, 11], [11, 10],

