'''
"Animals and plants can reproduce themselves, but it was only recently shown that 
machines can be made which also reproduce themselves... Other kinds of self-reproducing 
machines will be described, and one simple mechanical model, with no electrical or magnetic 
complications, will be there in working order for the audience to inspect and operate."

-- Edward Forrest Moore

In cellular automata, the Moore neighborhood comprises the eight cells surrounding a central 
cell on a two-dimensional square lattice. The neighborhood is named after Edward F. Moore, 
a pioneer of cellular automata theory. Many board games are played with a rectangular grid 
with squares as cells. For some games, it is important to know about the conditions of 
neighbouring cells for chip (figure, draught etc) placement and strategy.

You are given a state for a rectangular board game grid with chips in a binary matrix, where 
1 is a cell with a chip and 0 is an empty cell. You are also given the coordinates for a cell 
in the form of row and column numbers (starting from 0). You should determine how many chips 
are close to this cell. Every cell interacts with its eight neighbours; those cells that are 
horizontally, vertically, or diagonally adjacent.

example

For the given examples (see the schema) there is the same grid:

((1, 0, 0, 1, 0),
 (0, 1, 0, 0, 0),
 (0, 0, 1, 0, 1),
 (1, 0, 0, 0, 0),
 (0, 0, 1, 0, 0),)

For the first example coordinates of the cell is (1, 2) and as we can see from the schema this 
cell has 3 neighbour chips. For the second example coordinates is (0, 0) and this cell contains 
a chip, but we count only neighbours and the answer is 1.

Input: Three arguments. A grid as a tuple of tuples with integers (1/0), a row number and column 
number for a cell as integers.

Output: How many neighbouring cells have chips as an integer.

Example:

count_neighbours(((1, 0, 0, 1, 0),
                  (0, 1, 0, 0, 0),
                  (0, 0, 1, 0, 1),
                  (1, 0, 0, 0, 0),
                  (0, 0, 1, 0, 0),), 1, 2) == 3
count_neighbours(((1, 0, 0, 1, 0),
                  (0, 1, 0, 0, 0),
                  (0, 0, 1, 0, 1),
                  (1, 0, 0, 0, 0),
                  (0, 0, 1, 0, 0),), 0, 0) == 1

How it is used: As we mentioned in the beginning, this idea can be useful for developing board game 
algorithms. In addition, the same principles it can be useful for navigational software, or geographical 
surveying software.

Precondition:
3 ≤ len(grid) ≤ 10
all(len(grid[0]) == len(row) for row in grid)


“动物和植物可以自我繁殖，但直到最近才显示出来机器可以制作，也可以自我复制......其他类型的自我复制
机器将被描述，并且一个简单的机械模型，没有电或磁并发症，将在那里为观众检查和操作。“

- 爱德华福雷斯特摩尔

在细胞自动机中，摩尔邻域由中心周围的八个细胞组成细胞在二维正方形格子。这个社区以Edward F. Moore命名，
细胞自动机理论的先驱。许多棋盘游戏都使用矩形网格
与正方形作为细胞。对于某些游戏来说，了解游戏的条件非常重要芯片相邻单元（图，草案等）的位置和策略。

你得到一个状态矩阵的棋盘游戏网格与芯片在二进制矩阵，其中1是一个带芯片的单元，0是空单元。你也给了一个单元格的坐标
以行号和列号的形式（从0开始）。你应该确定有多少芯片靠近这个小区。每个细胞都与八个邻居相互作用;那些细胞是
水平地，垂直地或对角地相邻。

例

对于给定的例子（见模式），有相同的网格：

（（1,0,0,1,0），
 （0,1,0,0,0），
 （0,0,1,0,1），
 （1,0,0,0,0），
 （0,0,1,0,0），）

对于单元格的第一个示例坐标是（1，2），正如我们从模式中可以看到的那样
小区有3个相邻的芯片。对于第二个示例，坐标是（0，0），并且此单元格包含一个筹码，但我们只计算邻居，答案是1。

输入：三个参数。一个网格作为元组元组的元组，其中包含整数（1/0），行号和列数字作为整数的单元格。
输出：多少个相邻单元将芯片作为整数。

它是如何使用的：正如我们在开始时提到的，这个想法对开发棋盘游戏很有用
算法。另外，它对导航软件或地理位置可能有用测量软件。
'''

def count_neighbours(grid, row, col):
    longs = len(grid)
    cell = []
    if row == 0:
      if col == 0:
        for i in range(0, 2):
          for j in range(0, 2):
            cell.append(grid[i][j])
      elif col == longs - 1:
        for i in range(0, 2):
          for j in range(longs - 2, longs):
            cell.append(grid[i][j])
      else:
        for i in range(0, 2):
          for j in range(col - 1, col + 2):
            cell.append(grid[i][j])

    if row == longs - 1:
      if col == 0:
        for i in range(row - 1, row + 1):
          for j in range(0, 2):
            cell.append(grid[i][j])
      elif col == longs - 1:
        for i in range(row - 1, row + 1):
          for j in range(col - 1, col + 1):
            cell.append(grid[i][j])
      else:
        for i in range(row - 1, row + 1):
          for j in range(col - 1 , col + 2):
            cell.append(grid[i][j])

    if col == 0:
      if row != 0 and row != longs - 1:
        for i in range(row - 1, row + 2):
          for j in range(0, 2):
            cell.append(grid[i][j])

    if col == longs -1:
      if row != 0 and row != longs - 1:
        for i in range(row - 1, row + 2):
          for j in range(col - 1, col + 1):
            cell.append(grid[i][j])

    if row != 0 and row != longs - 1 and col !=0 and col != longs -1:
      for i in range(row - 1, row + 2):
        for j in range(col - 1, col + 2):
          cell.append(grid[i][j])

    count = cell.count(1)
    if grid[row][col] == 1:
      count -= 1
    return count

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert count_neighbours(((1, 0, 0, 1, 0),
                             (0, 1, 0, 0, 0),
                             (0, 0, 1, 0, 1),
                             (1, 0, 0, 0, 0),
                             (0, 0, 1, 0, 0),), 1, 2) == 3, "1st example"
    assert count_neighbours(((1, 0, 0, 1, 0),
                             (0, 1, 0, 0, 0),
                             (0, 0, 1, 0, 1),
                             (1, 0, 0, 0, 0),
                             (0, 0, 1, 0, 0),), 0, 0) == 1, "2nd example"
    assert count_neighbours(((1, 1, 1),
                             (1, 1, 1),
                             (1, 1, 1),), 0, 2) == 3, "Dense corner"
    assert count_neighbours(((0, 0, 0),
                             (0, 1, 0),
                             (0, 0, 0),), 1, 1) == 0, "Single"
