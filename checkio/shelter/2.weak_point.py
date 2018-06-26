'''
While traveling, the spaceship endures quite a lot of stress. As a result, an important 
part of the maintenance is to check the outer hull. Stephan uses a digital durabilitimeter 
for this task. The device scans a portion of the spaceships hull and gives a durability map 
that is divided by small square fragments with measurements. Sometimes Stephan does not have 
much time and he can patch only couple points, so we need an algorithm to find the weak points.

The durability map is represented as a matrix with digits. Each number is the durability 
measurement for the cell. To find the weakest point we should find the weakest row and column. 
The weakest point is placed in the intersection of these rows and columns. Row (column) durability 
is a sum of cell durability in that row (column). You should find coordinates of the weakest point 
(row and column). The first row (column) is 0th row (column). If a section has several equal weak 
points, then choose the top left point.


Input: A durability map as a list of lists with integers.

Output: The coordinates of the weak point as a list (tuple) of integers.

Example:

weak_point([[7, 2, 7, 2, 8],
            [2, 9, 4, 1, 7],
            [3, 8, 6, 2, 4],
            [2, 5, 2, 9, 1],
            [6, 6, 5, 4, 5]]) == [3, 3]
weak_point([[7, 2, 4, 2, 8],
            [2, 8, 1, 1, 7],
            [3, 8, 6, 2, 4],
            [2, 5, 2, 9, 1],
            [6, 6, 5, 4, 5]]) == [1, 2]

How it is used: Matrices (2D array) are an often used data structure and it will be helpful to sharpen your skills with them.

Precondition:
0 < len(matrix) ≤ 10
all(len(row) == len(matrix) for row in matrix)
all(all(0 < x < 10 for x in row) for row in matrix)

在旅行时，太空船承受着相当大的压力。因此，一个重要的
部分维修工作是检查外壳。斯蒂芬使用数字Durabilitimeter
为此任务。该设备扫描船体的一部分，并给出耐久性图
这是由具有测量的小方块分割的。有时斯蒂芬没有
很多时间，他只能修补几个点，所以我们需要一个算法来找出薄弱点。

耐久性图表用带数字的矩阵表示。每个数字都是耐久性
测量细胞。要找到最薄弱的地方，我们应该找到最弱的行和列。
最薄弱的部分放在这些行和列的交叉处。行（列）耐久性
是该行（列）中单元格耐久性的总和。你应该找到最弱点的坐标
（行和列）。第一行（列）是第0行（列）。如果一个部分有几个相等的弱
点，然后选择左上角的点。

输入：持久性地图作为整数列表的列表。
输出：弱点的坐标作为整数列表（元组）。

如何使用它：矩阵（二维数组）是一个经常使用的数据结构，它将有助于提高你的技能。

前提：
0 <len（矩阵）≤10
all（len（row）== len（矩阵）用于矩阵中的行）
全部（矩阵中的所有行（对于x行，0 <x <10））
'''

def weak_point(matrix):
    row_v = dict()
    col_v = dict()
    for i, k in enumerate(matrix):
        row_v[i] = sum(k)

    min_row = min(row_v.values())
    row = [i for i, v in row_v.items() if v == min_row]

    for i, k in enumerate(zip(*matrix)):
        col_v[i] = sum(k)

    min_col = min(col_v.values())
    col = [i for i, v in col_v.items() if v == min_col]
    
    return(min(row), min(col))



if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    #assert isinstance(weak_point([[1]]), (list, tuple)), "The result should be a list or a tuple"
    assert list(weak_point([[7, 2, 7, 2, 8],
                            [2, 9, 4, 1, 7],
                            [3, 8, 6, 2, 4],
                            [2, 5, 2, 9, 1],
                            [6, 6, 5, 4, 5]])) == [3, 3], "Example"
    assert list(weak_point([[7, 2, 4, 2, 8],
                            [2, 8, 1, 1, 7],
                            [3, 8, 6, 2, 4],
                            [2, 5, 2, 9, 1],
                            [6, 6, 5, 4, 5]])) == [1, 2], "Two weak point"
    assert list(weak_point([[1, 1, 1],
                            [1, 1, 1],
                            [1, 1, 1]])) == [0, 0], "Top left"
