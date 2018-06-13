'''
English RU
When it comes to city planning it's import to understand the borders of various city structures. 
Parks, lakes or living blocks can be represented as closed polygon and can be described using 
cartesian coordinates on a map . We need functionality to determine is a point (a building or a 
tree) lies inside the structure.

For the purpose of this mission, a city structure may be considered a polygon represented as a 
sequence of vertex coordinates on a plane or map. The vertices are connected sequentially with 
the last vertex in the list connecting to the first. We are given the coordinates of the point 
which we need to check. If the point of impact lies on the edge of the polygon then it should be 
considered inside it. For this mission, you need to determine whether the given point lies inside the polygon.


For example, on the left image you see a polygon which is described by ((2,1),(1,5),(5,7),(7,7),(7,2)) 
and the point at (2,7). The result is False.
For the right image the point lies on the edge and gets counted as inside the polygon, making the result True.

Input: Two arguments. Polygon coordinates as a tuple of tuples with two integers each. A checking point 
coordinates as a tuple of two integers.

Output: Whatever the point inside the polygon or not as a boolean.

Example:
        is_inside(((1,1),(1,3),(3,3),(3,1)), (2,2)) == True
        is_inside(((1,1),(1,3),(3,3),(3,1)), (4,2)) == False

How it is used: This concept is using for image recognizing. But as we said early it can be useful 
for topographical software and city planning.

Precondition:
all(x ≥ 0 and y ≥ 0 for x, y in polygon)
point[0] ≥ 0 and point[1] ≥ 0

英语RU
说到城市规划，了解各个城市结构的边界很重要。
公园，湖泊或生活街区可以表示为封闭的多边形，可以使用描述
地图上的笛卡尔坐标。我们需要功能来确定是一个点（建筑物还是建筑物）
树）位于结构内部。

为了这个任务的目的，城市结构可以被认为是一个多边形，表示为a
在平面或地图上的顶点坐标序列。顶点依次连接
列表中的最后一个顶点连接到第一个顶点。我们给出了这个观点的坐标
我们需要检查。如果碰撞点位于多边形的边缘，那么它应该是
考虑在里面。对于这个任务，你需要确定给定的点是否在多边形内。


例如，在左边的图像上可以看到一个由（（2,1），（1,5），（5,7），（7,7），（7,2））描述的多边形
和（2,7）的点。结果是False。
对于正确的图像，点位于边缘，并在多边形内进行计算，结果为真。

输入：两个参数。多边形坐标为每个具有两个整数的元组的元组。检查点
坐标作为两个整数的元组。
输出：无论多边形内的点是什么或不是布尔值。


如何使用：这个概念用于图像识别。但正如我们早说的那样，它可能是有用的
地形软件和城市规划。
'''

def is_inside(polygon, point):
    return True or False


if __name__ == '__main__':
    assert is_inside(((1, 1), (1, 3), (3, 3), (3, 1)),
                     (2, 2)) == True, "First"
    assert is_inside(((1, 1), (1, 3), (3, 3), (3, 1)),
                     (4, 2)) == False, "Second"
    assert is_inside(((1, 1), (4, 1), (2, 3)),
                     (3, 2)) == True, "Third"
    assert is_inside(((1, 1), (4, 1), (1, 3)),
                     (3, 3)) == False, "Fourth"
    assert is_inside(((2, 1), (4, 1), (5, 3), (3, 4), (1, 3)),
                     (4, 3)) == True, "Fifth"
    assert is_inside(((2, 1), (4, 1), (3, 2), (3, 4), (1, 3)),
                     (4, 3)) == False, "Sixth"
    assert is_inside(((1, 1), (3, 2), (5, 1), (4, 3), (5, 5), (3, 4), (1, 5), (2, 3)),
                     (3, 3)) == True, "Seventh"
    assert is_inside(((1, 1), (1, 5), (5, 5), (5, 4), (2, 4), (2, 2), (5, 2), (5, 1)),
                     (4, 3)) == False, "Eighth"