'''
To describe a specific position on the surface of the Earth, we must rely on the geographic coordinate system. The geographic coordinate system is a method used to give every possible location on Earth to be specified by a set of numbers or letters. A common choice of coordinates is latitude and longitude. With this information we can calculate a distance between two points along a surface.

For simplicity’s sake, we will suppose that the Earth is a perfect sphere with a radius of 6,371 kilometers (it gives a mistake no more than 0.3%). You are given two point coordinates and you must find the shortest distance between these points on the surface of the Earth, measured along the surface of the Earth.

Coordinates are given as a string with the latitude and longitude separated by comma and/or whitespace. Latitude and longitude are represented in the follow format:

    d°m′s″X

In this example, "d" is degrees, "m" is minutes, "s" is seconds as integers, while "X" is "N" (north) or "S" (south) for a latitude and "W" (west) or "E" (east) for a longitude.

The result should be given as a number in kilometers with a precision of ±0.1 (100 metres).

Input: Two arguments. Coordinates as strings (unicode).

Output: The distance as a number (int or float).

Example:

distance(u"51°28′48″N 0°0′0″E", u"46°12′0″N, 6°9′0″E") == 739.2
distance(u"90°0′0″N 0°0′0″E", u"90°0′0″S, 0°0′0″W") == 20015.1

How it is used: The concepts presented in this mission are the exact sorts of concepts used in navigational software, enabling a ship or plane to understand where it is, where it must go and how far it has gone. Along the same vein, Global Positioning Satellites use similar principles to provide pinpoint accurate locations to GPS receivers for use in navigation.

Precondition: Correct Coordinates.


为了描述地球表面的特定位置，我们必须依靠地理坐标系。地理坐标系是一种用于为地球上的每个可能位置指定一组数字或字母的方法。坐标的常用选择是经度和纬度。有了这些信息，我们就可以计算沿着曲面的两点之间的距离。

为了简单起见，我们假设地球是一个半径6,371公里的完美球体（它给出的误差不超过0.3％）。你有两个点坐标，你必须找到地球表面上这些点之间的最短距离，沿着地球表面测量。

坐标以经度和纬度用逗号和/或空格分隔的字符串形式给出。经度和纬度用以下格式表示：

    d°米的“X

在这个例子中，“d”是度数，“m”是分钟，“s”是整数的秒数，而“X”是纬度的“N”（北）或“S”（南），“W”（西）或“E”（东）的经度。

结果应该以公里为单位给出，精度为±0.1（100米）。

输入：两个参数。坐标作为字符串（unicode）。
输出：距离为数字（int或float）。

如何使用：这项任务中提出的概念是导航软件中使用的确切概念，使船舶或飞机能够理解它在哪里，它必须去哪里以及它走了多远。同样，全球定位卫星也使用类似的原理为GPS接收机提供精确定位以用于导航。

先决条件：正确的坐标。
'''