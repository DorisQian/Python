'''
Biologists use bacteria to clone DNA for sequencing. These bacteria are then 
injected with the DNA that needs to be cloned and allowed to reproduce on a large 
plate. As these bacteria reproduce, they begin to form colonies. Only bacteria from 
healthy colonies will be used for sequencing. And here bioinformatics take the game 
and use technologies to automate these process.

Let's represent a plate snapshot as a pixel grid. You are given this grid as a binary 
matrix where 1 is bacteria cell and 0 is empty. Our goal is find the largest healthy 
bacteria colony which has grown uniformly. Bacteria can grow in four adjacent cells 
and bacteria colony is a set of bacterias that are connected. The healthy colonies look 
similar to the images represented below.

healthy
Next, we can see that unhealthy colonies are marked with an orange color. Remember that 
a single cell is not a colony, so it cannot be counted as healthy colony.

example
Your mission is to find the largest healthy colony and return the coordinates of the center 
cell. The top-left cell has coordinates (0, 0). If on the plate no a healthy colony, then 
return (0, 0) (or [0, 0]). If on the plate several largest colonies with the same size, 
then return any of them.

Input: A grid as a tuple of tuples with integers 1/0.

Output: The coordinates of the largest colony as a list or a tuple of two integers.

Example:

healthy(((0, 1, 0),
         (1, 1, 1),
         (0, 1, 0),))
How it is used: This mission presents a mix of modeling, pattern recognition and data 
structure programing in addition to presenting some ideas for how to use it in 
bioinformatics. That is assuming of course that bioinformatics can be useful for classical biology.

Precondition:
5 ≤ len(grid) ≤ 20
all(5 ≤ len(row) ≤ 20 for row in grid)

生物学家利用细菌克隆DNA进行测序。那么这些细菌呢
注入需要克隆的DNA，并允许大量繁殖
盘子。随着这些细菌繁殖，它们开始形成菌落。只有细菌从
健康的菌落将被用于测序。这里的生物信息学就是这个游戏
并使用技术来自动化这些过程。

我们将一个板快照表示为一个像素网格。你给这个网格作为一个二进制
矩阵，其中1是细菌细胞，0是空的。我们的目标是找到最大的健康
细菌菌落生长均匀。细菌可以在四个相邻的细胞中生长
而细菌菌落是一组相连的细菌。健康的殖民地看起来
类似于下面的图像。

健康
接下来，我们可以看到，不健康的殖民地标有橙色。请记住
单细胞不是一个殖民地，所以它不能算作健康的殖民地。

例
你的任务是找到最大的健康殖民地，并返回中心的坐标
细胞。左上角的单元格有坐标（0，0）。如果在盘子上没有一个健康的殖民地，那么
返回（0，0）（或[0，0]）。如果在盘子上有几个同样大小的最大的殖民地，
然后返回其中的任何一个。

输入：一个网格作为元素的元组的元组，其中元素为1/0。

输出：最大殖民地的坐标作为一个列表或两个整数的元组。


如何使用：除了介绍如何在生物信息学中使用它，此任务还提供了建模，模式识别和数据结构编程的组合。
这当然假定生物信息学可以用于经典生物学。
'''

def healthy(grid):
    return 0, 0


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    def check(result, answers):
        return list(result) in answers

    check(healthy(((0, 1, 0),
                   (1, 1, 1),
                   (0, 1, 0),)), [[1, 1]])
    check(healthy(((0, 0, 1, 0, 0),
                   (0, 1, 1, 1, 0),
                   (0, 0, 1, 0, 0),
                   (0, 0, 0, 0, 0),
                   (0, 0, 1, 0, 0),)), [[1, 2]])
    check(healthy(((0, 0, 1, 0, 0),
                   (0, 1, 1, 1, 0),
                   (0, 0, 1, 0, 0),
                   (0, 0, 1, 0, 0),
                   (0, 0, 1, 0, 0),)), [[0, 0]])
    check(healthy(((0, 0, 0, 0, 0, 0, 1, 0),
                   (0, 0, 1, 0, 0, 1, 1, 1),
                   (0, 1, 1, 1, 0, 0, 1, 0),
                   (1, 1, 1, 1, 1, 0, 0, 0),
                   (0, 1, 1, 1, 0, 0, 1, 0),
                   (0, 0, 1, 0, 0, 1, 1, 1),
                   (0, 0, 0, 0, 0, 0, 1, 0),)), [[3, 2]])
    check(healthy(((0, 0, 0, 0, 0, 0, 2, 0),
                   (0, 0, 0, 2, 2, 2, 2, 2),
                   (0, 0, 1, 0, 0, 0, 2, 0),
                   (0, 1, 1, 1, 0, 0, 2, 0),
                   (1, 1, 1, 1, 1, 0, 2, 0),
                   (0, 1, 1, 1, 0, 0, 2, 0),
                   (0, 0, 1, 0, 0, 0, 2, 0),
                   (0, 0, 0, 1, 0, 0, 2, 0),
                   (0, 0, 1, 1, 1, 0, 2, 0),
                   (0, 1, 1, 1, 1, 1, 0, 0),
                   (0, 0, 1, 1, 1, 0, 0, 0),
                   (0, 0, 0, 1, 0, 0, 0, 0),)), [[4, 2], [9, 3]])
