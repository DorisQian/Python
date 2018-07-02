'''
Stephan works with simple forms when constructing something, and he need some programming tools to calculate his expenses. Let's take a trip back to our school days and pull out some simple geometry for this.

You should write a function to calculate the area of simple figures: circles, rectangles and triangles. You are give an arbitrary number of arguments and depending on this, the function calculates area for the different figures.

One argument -- The diameter of a circle and you need calculate the area of the circle.
Two arguments -- The side lengths of a rectangle and you need calculate the area of the rectangle.
Three arguments -- The lengths of each side on a triangle and you need calculate the area of the triangle.
simple-areas

The result should be given with two digits precision as ±0.01.

Tips: Think about how to work with an arbitrary number of arguments.

Input: One, two or three arguments as floats or as integers.

Output: The area of the circle, the rectangle or the triangle as a float.

Example:

simple_areas(3) == 7.07
simple_areas(2, 2) == 4
simple_areas(2, 3) == 6
simple_areas(3, 5, 4) == 6
simple_areas(1.5, 2.5, 2) == 1.5
    
How it is used: Python can be an useful tool for mathematics and science. You can easily implement any formulas or math algorithm with this simple and readable programming language.

Precondition:
0 < len(args) ≤ 3
all(0 < x ≤ 1000 for x in args)
For "triangle" cases the sum of the lengths of any two sides always exceeds the length of the third side.

Stephan在构建某些东西时用简单的形式工作，他需要一些编程工具来计算他的开销。让我们回到我们的上学时间，
为此抽出一些简单的几何图形。

你应该编写一个函数来计算简单数字的面积：圆形，矩形和三角形。您可以提供任意数量的参数，并根据此参数计算不同数字的面积。

一个参数 - 圆的直径，您需要计算圆的面积。
两个参数 - 矩形的边长，您需要计算矩形的面积。
三个参数 - 三角形各边的长度，您需要计算三角形的面积。
简单区

结果应以±0.01的两位数字精度给出。

提示：考虑如何使用任意数量的参数。

输入：一个，两个或三个参数作为浮点数或整数。
输出：圆的面积，矩形或三角形的浮点数。
 
如何使用它：Python可以成为数学和科学的有用工具。您可以使用这种简单易读的编程语言轻松实现任何公式或数学算法。
'''
import math
def simple_areas(*args):
    length = len(args)
    if length == 1:
        return (args[0] / 2) ** 2 * math.pi
    elif length == 2:
        return args[0] * args[1]
    else:
        p = (args[0] + args[1] + args[2]) / 2
        return math.sqrt((p * (p - args[0])*(p-args[1])*(p-args[2])))

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    def almost_equal(checked, correct, significant_digits=2):
        precision = 0.1 ** significant_digits
        return correct - precision < checked < correct + precision

    assert almost_equal(simple_areas(3), 7.07), "Circle"
    assert almost_equal(simple_areas(2, 2), 4), "Square"
    assert almost_equal(simple_areas(2, 3), 6), "Rectangle"
    assert almost_equal(simple_areas(3, 5, 4), 6), "Triangle"
    assert almost_equal(simple_areas(1.5, 2.5, 2), 1.5), "Small triangle"