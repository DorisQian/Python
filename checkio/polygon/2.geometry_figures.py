'''
You often work with the different geometrical figures and with their parameters - perimeter, area, volume. You are tired to do this by hand, so you have decided to automate this process. You should write the program for this. In this program you should create the class Figure with some methods:

Figure().perimeter() (returns the perimeter of the figure)
Figure().area() (returns the area of the figure)
Figure().volume() (returns the volume of the figure)

You will work with this figures:
"circle" --> Figure("circle", R), where R is the radius of the circle ( 0.1 <= R <= 1000.0)
"triangle" --> Figure("triangle", a, b, c), where 'a, b, c' are the sides of the triangle ( 0.1 <= a, b, c <= 1000.0)
"rectangle" --> Figure("rectangle", a, b), where 'a, b' are the sides of the rectangle ( 0.1 <= a, b <= 1000.0)
"pentagon" --> Figure("pentagon", a), where 'a' is the side of the equal sided pentagon ( 0.1 <= a <= 1000.0)
"hexagon" --> Figure("hexagon", a), where 'a' is side of the equal sided hexagon ( 0.1 <= a <= 1000.0)
"cube" --> Figure("circle", a), where 'a' is the side of the cube ( 0.1 <= a <= 1000.0)

Every figure except cube has volume = 0.
If the result has no decimal part you should return it as int(), in the other case - round it to 2 decimal sign.
In this mission you can use the Strategy design pattern.

Examples:

Figure("circle", 10).area() == 314.16
Figure("triangle", 3, 4, 5).volume() == 0
Figure("rectangle", 1.5, 2.5).area() == 3.75
Figure("pentagon", 500).perimeter() == 2500
Figure("hexagon", 100.003).perimeter() == 600.02
Figure("cube", 20).volume() == 8000

Input: Statements and expression of the class Figure.
Output: perimeter, area, volume (number).

Hot it is used: For the geometry objects analysis.

Precondition: All data are correct.

您经常使用不同的几何图形和参数 - 周长，面积，体积。您已经厌倦了手动执行此操作，因此您决定自动执行此过程。你应该为此编写程序。在这个程序中，你应该用一些方法创建类图：

图（）。周长（）（返回图的周长）
图（）。area（）（返回图的区域）
图（）。volume（）（返回图的体积）

你将使用这些数字：
“circle” - > Figure（“circle”，R），其中R是圆的半径（0.1 <= R <= 1000.0）
“三角形” - >图（“三角形”，a，b，c），其中'a，b，c'是三角形的边（0.1 <= a，b，c <= 1000.0）
“矩形” - >图（“矩形”，a，b），其中'a，b'是矩形的边（0.1 <= a，b <= 1000.0）
“五边形” - >图（“五边形”，a），其中'a'是等边五边形的边（0.1 <= a <= 1000.0）
“六边形” - >图（“六边形”，a），其中'a'是等边六边形的边（0.1 <= a <= 1000.0）
“立方体” - >图（“圆”，a），其中'a'是立方体的边（0.1 <= a <= 1000.0）

除立方体以外的每个图形都有体积= 0。
如果结果没有小数部分，则应将其作为int（）返回，在另一种情况下 - 将其舍入为2个十进制符号。
在这个任务中你可以使用策略设计模式。

输入：类的语句和表达式
输出：周长，面积，体积（数量）。

它用于热：用于几何对象分析。

先决条件：所有数据都是正确的。
'''

class Figure:
    def __init__(self, name, *args):
        raise NotImplementedError

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing

    assert Figure("circle", 10).area() == 314.16
    assert Figure("triangle", 3, 4, 5).volume() == 0
    assert Figure("rectangle", 1.5, 2.5).area() == 3.75
    assert Figure("pentagon", 500).perimeter() == 2500
    assert Figure("hexagon", 100.003).perimeter() == 600.02
    assert Figure("cube", 20).volume() == 8000
    print("Coding complete? Let's try tests!")