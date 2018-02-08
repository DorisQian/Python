'''
You are given a list of points on a coordinate plane. We need you find the convex hull formed by these points. The convex hull of a set X of points in the Euclidean plane is the smallest convex set that contains X. For instance: when X is a bounded subset of the plane, the convex hull may be visualized as the shape formed by a rubber band stretched around X. If a point lies on edge, it's included.

The points are presented as a list of coordinates [x, y] in which x and y are integers. The result returns as a sequence of indexes of points in the given list; points lie on the convex hull in clockwise order (see the picture). The sequence starts from the bottom leftmost point. Remember: You should return a list of indexes--not the points themselves.

convex-hull

Input: A list of coordinates. Each coordinate is a list of two integers.

Output: The list of indexes of coordinates from the given list.

Example:

checkio([[7, 6], [8, 4], [7, 2], [3, 2], [1, 6], [1, 8], [4, 9]]) == [4, 5, 6, 0, 1, 2, 3]
checkio([[3, 8], [1, 6], [6, 2], [7, 6], [5, 5], [8, 4], [6, 8]]) == [1, 0, 6, 3, 5, 2]

How it is used: Convex hulls have practical applications in pattern recognition, image processing, statistics, GIS and static code analysis by abstract interpretation. The concept also serves as a tool and a building block for a number of other computational-geometric algorithms such as the rotating calipers method for computing the width and diameter of a point set.

Precondition: 
2 < len(coordinates) < 10
all(0 < x < 10 and 0 < x < 10 for x, y in coordinates)

给出一个坐标平面上的点列表。我们需要你找到由这些点形成的凸包。欧几里德平面上的一组点X的凸包是包含X的最小凸包。例如：当X是平面的有界子集时，凸包可以被看成是由拉伸的橡皮筋形成的形状围绕X.如果一个点位于边缘，则包括在内。

点以x和y为整数的坐标列表[x，y]表示。结果作为给定列表中的点的索引序列返回;点按顺时针顺序位于凸包上（见图）。序列从最左下角开始。记住：你应该返回一个索引列表 - 而不是点本身。

凸包

输入：坐标列表。每个坐标是两个整数的列表。
输出：给定列表中的坐标索引列表。


它是如何使用的：凸壳在模式识别，图像处理，统计，GIS和静态代码分析等方面有实际应用。这个概念也可以作为一个工具和一些其他计算几何算法的基础，例如用于计算点集的宽度和直径的旋转卡尺方法。
'''