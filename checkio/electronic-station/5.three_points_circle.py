"""
Nicola discovered a calliper inside a set of drafting tools he received as a gift. Seeing the caliper, he has decided to learn how to use it.

Through any three points that do not exist on the same line, there lies a unique circle. The points of this circle are represented in a string with the coordinates like so:

    "(x1,y1),(x2,y2),(x3,y3)"

Where x1,y1,x2,y2,x3,y3 are digits.

You should find the circle for three given points, such that the circle lies through these point and return the result as a string with the equation of the circle. In a Cartesian coordinate system (with an X and Y axis), the circle with central coordinates of (x0,y0) and radius of r can be described with the following equation:

    "(x-x0)^2+(y-y0)^2=r^2"

where x0,y0,r are decimal numbers rounded to two decimal points. Remove extraneous zeros and all decimal points, they are not necessary. For rounding, use the standard mathematical rules.

three_points_circle
Input: Coordinates as a string..

Output: The equation of the circle as a string.

Example:

checkio("(2,2),(6,2),(2,6)") == "(x-4)^2+(y-4)^2=2.83^2"
checkio("(3,7),(6,9),(9,7)") == "(x-6)^2+(y-5.75)^2=3.25^2"

How it is used: This equation, also known as Equation of the Circle, comes from the Pythagorean theorem when applied to any point on a circle: the radius is the hypotenuse of a right-angled triangle whose other sides are of length x − a and y − b. Of course you can use this concept for you mathematics software, but we just want to remind about how awesome circles are.

Precondition: All three given points do not lie on one line.
0 < xi, yi, r < 10

尼古拉在他收到的一套绘图工具内发现了一个书法家。看到了卡尺，他决定学习如何使用它。
在同一直线上的任何三个点，都存在一个独特的圆。这个圆的点用一个像这样的坐标表示:
”(x1,y1),(x2,y2),(x3,y3)”
(x1,y1,x2,y2,x3,y3位数。
你应该找到三个给定的点的圆，这样圆就在这些点上，并以圆的方程返回结果。在笛卡尔坐标系(X和Y轴)中，可以用下面的方程描述(x0,y0)和r半径的圆:
”(x-x0)^ 2 +(y-y0)^ 2 = r ^ 2”
其中，x0,y0,r是十进制数，四舍五入到小数点。删除无关的零和所有小数点，它们是不必要的。对于四舍五入，使用标准的数学规则。
three_points_circle

输入:以字符串形式的坐标。
输出:圆的方程为字符串。

如何使用它:这个方程,也被称为圆的方程,来自勾股定理在应用到任意点在一个循环:半径是一个直角三角形的斜边长度的其他方面x和y−−b。当然,你可以使用这个概念你数学软件,但我们只是想提醒如何了不起的圈子。

先决条件:所有三个给定的点都不在一条线上。
"""

def checkio(data):

    #replace this for solution
    return ""

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio("(2,2),(6,2),(2,6)") == "(x-4)^2+(y-4)^2=2.83^2"
    assert checkio("(3,7),(6,9),(9,7)") == "(x-6)^2+(y-5.75)^2=3.25^2"