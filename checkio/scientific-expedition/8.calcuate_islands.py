"""
The Robots have found a chain of islands in the middle of the Ocean. They would like to explore these islands and have asked for your help calculating the areas of each island. They have given you a map of the territory. The map is a 2D array, where 0 is water, 1 is land. An island is a group of land cells surround by water. Cells are connected by their edges and corners. You should calculate the areas for each of the islands and return a list of sizes (quantity of cells) in ascending order. All of the cells outside the map are considered to be water.

calculate-islands
Input: A map as a list of lists with 1 or 0.

Output: The sizes of island as a list of integers.

Example:

checkio([
    [0, 0, 0, 0, 0],
    [0, 0, 1, 1, 0],
    [0, 0, 0, 1, 0],
    [0, 1, 0, 0, 0],
    [0, 0, 0, 0, 0]]) == [1, 3]
checkio([
    [0, 0, 0, 0, 0],
    [0, 0, 1, 1, 0],
    [0, 0, 0, 1, 0],
    [0, 1, 1, 0, 0]]) == [5]
checkio([
    [0, 0, 0, 0, 0, 0],
    [1, 0, 0, 1, 1, 1],
    [1, 0, 0, 0, 0, 0],
    [0, 0, 1, 1, 1, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 1, 1, 1, 1, 0],
    [0, 0, 0, 0, 0, 0]]) == [2, 3, 3, 4]

How it is used: This task is an example of a disjoint-set data structure. Disjoint-set data structures model the partitioning of a set; for example, it helps with keeping track of the connected components in an undirected graph (networks).

Precondition: 0 < len(land_map) < 10
all(len(land_map[0]) == len(row) for row in land_map)
any(any(row) for row in land_map)

机器人在海洋中间发现了一连串的岛屿。他们想要探索这些岛屿，并要求你们帮助计算每个岛屿的面积。他们给了你这片领土的地图。地图是一个二维数组，0是水，1是陆地。岛屿是一群被水环绕的陆地细胞。细胞的边缘和棱角连接在一起。您应该计算每个岛屿的区域，并返回一个按升序排列的大小(单元格数量)列表。地图外的所有细胞都被认为是水。
calculate-islands

输入:以1或0为列表的列表。
输出:作为整数列表的岛屿的大小。
如何使用:这个任务是一个分离集数据结构的示例。分离集数据结构模型的划分;例如，它有助于在无向图(网络)中跟踪连接的组件。
"""

def checkio(land_map):

    return [1]

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio([[0, 0, 0, 0, 0],
                    [0, 0, 1, 1, 0],
                    [0, 0, 0, 1, 0],
                    [0, 1, 0, 0, 0],
                    [0, 0, 0, 0, 0]]) == [1, 3], "1st example"
    assert checkio([[0, 0, 0, 0, 0],
                    [0, 0, 1, 1, 0],
                    [0, 0, 0, 1, 0],
                    [0, 1, 1, 0, 0]]) == [5], "2nd example"
    assert checkio([[0, 0, 0, 0, 0, 0],
                    [1, 0, 0, 1, 1, 1],
                    [1, 0, 0, 0, 0, 0],
                    [0, 0, 1, 1, 1, 0],
                    [0, 0, 0, 0, 0, 0],
                    [0, 1, 1, 1, 1, 0],
                    [0, 0, 0, 0, 0, 0]]) == [2, 3, 3, 4], "3rd example"