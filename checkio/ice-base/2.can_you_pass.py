'''
If you have solved the "How to find friends" mission, then you already know how to 
check for the existence of a path in graphs. Let's try to add something more to that problem.

You are given a matrix (2D array) and the coordinates (row and column) of two cells 
with the same value. The matrix consists of digits. You may move to neighbouring cells 
either horizontally or vertically provided the values of the origin and destination 
cells are equal. You should determine if a path exists between two given cells.

A matrix is represented as a tuple of tuples with digits. Coordinates are represented 
as a tuple with two numbers: row and column. The result should be any value which can 
be converted into a boolean. If a path exists, then return True. Return False if there is none.

can-you-jump-through

Input: Three arguments. A matrix as a tuple of tuples with integers, first and second 
cell coordinates as tuples of two integers.

Output: The existence of a path between two given cells as a boolean or a value that can 
be converted to boolean.

Example:
can_pass(((0, 0, 0, 0, 0, 0),
          (0, 2, 2, 2, 3, 2),
          (0, 2, 0, 0, 0, 2),
          (0, 2, 0, 2, 0, 2),
          (0, 2, 2, 2, 0, 2),
          (0, 0, 0, 0, 0, 2),
          (2, 2, 2, 2, 2, 2),),
         (3, 2), (0, 5)) == True, 'First example'
can_pass(((0, 0, 0, 0, 0, 0),
          (0, 2, 2, 2, 3, 2),
          (0, 2, 0, 0, 0, 2),
          (0, 2, 0, 2, 0, 2),
          (0, 2, 2, 2, 0, 2),
          (0, 0, 0, 0, 0, 2),
          (2, 2, 2, 2, 2, 2),),
         (3, 3), (6, 0)) == False,

How it is used: Sometimes we don't need the full pathfinding algorithms implementation and 
can use simplified realisation of these algorithms. It can be an useful skill to find a simple ways.

Precondition:
1 < len(matrix) ≤ 10
all(1 < len(row) ≤ 10 for row in matrix)
all(all(0 ≤ x < 10 for x in row) for row in matrix)
matrix[first[0]][first[1]] == matrix[second[0]][second[1]]
first != second

如果你已经解决了“如何找到朋友”的使命，那么你已经知道如何检查图中是否存在路径。让我们尝试
添加更多的东西来解决这个问题。

给你一个矩阵（二维数组）和坐标（行和列）具有相同值的两个单元格。矩阵由数字组成。如果原始
和目标单元格的值相等，则可以水平或垂直移动到相邻的单元格。您应该确定两个给定单元格之间是否存在路径。

矩阵被表示为具有数字的元组的元组。坐标被表示为一个具有两个数字的元组：行和列。结果应该是
可以转换成布尔值的任何值。如果存在路径，则返回True。如果没有，则返回假。

可以，你跳通

输入：三个参数。一个矩阵作为元组的元组，第一个和第二个单元坐标是两个整数的元组。
输出：两个给定单元格之间的路径作为布尔值或可以转换为布尔值的值的存在。

如何使用：有时我们不需要完整的寻路算法实现，并可以使用这些算法的简化实现。找到一个简单的
方法可能是一个有用的技巧。
'''


def can_pass(matrix, first, second):
    value = matrix[first[0]][first[1]]
    points = []
    for i in range(len(matrix)):
      for j in range(len(matrix[0])):
        if matrix[i][j] == value:
          points.append((i,j))
    #print(points)

    relate = {}
    for p1 in points:
      for p2 in points:
        if p2[1] == p1[1]:
          if p2[0] - 1 == p1[0] or p2[0] + 1 == p1[0]:
            re_set = set(relate.get(p1, tuple()))
            re_set.add(p2)
            relate[p1] = re_set
        elif p2[0] == p1[0]:
          if p2[1] - 1 == p1[1] or p2[1] + 1 == p1[1]:
            re_set = set(relate.get(p1, tuple()))
            re_set.add(p2)
            relate[p1] = re_set
    print(relate)

    key = relate.keys()
    if first not in key:
      return False

    opn = [first]
    closed = []
    while len(opn):
      now = opn[0]
      opn.remove(now)
      closed.append(now)
      friend = relate[now]
      for f in friend:
        if f not in closed and f not in opn:
          opn.append(f)

    if second in closed:
      return True
    else:
      return False

if __name__ == '__main__':
  
    assert can_pass(((0, 0, 0, 0, 0, 0),
                     (0, 2, 2, 2, 3, 2),
                     (0, 2, 0, 0, 0, 2),
                     (0, 2, 0, 2, 0, 2),
                     (0, 2, 2, 2, 0, 2),
                     (0, 0, 0, 0, 0, 2),
                     (2, 2, 2, 2, 2, 2),),
                    (3, 2), (0, 5)) == True, 'First example'
  
assert can_pass(((0, 0, 0, 0, 0, 0),
                     (0, 2, 2, 2, 3, 2),
                     (0, 2, 0, 0, 0, 2),
                     (0, 2, 0, 2, 0, 2),
                     (0, 2, 2, 2, 0, 2),
                     (0, 0, 0, 0, 0, 2),
                     (2, 2, 2, 2, 2, 2),),
                    (3, 3), (6, 0)) == False, 'First example'

assert can_pass(((1,9),(9,1)), (0,1), (1,0)) == False

assert can_pass(((1,7,8,0,5),(7,7,8,5,7),(4,6,5,4,0),(4,6,8,4,7),(1,8,2,1,1),(3,0,4,7,4)), (5,2), (5,4)) == False