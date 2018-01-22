"""
You are given the lengths for each side on a triangle. You need to find all three angles for this triangle. 
If the given side lengths cannot form a triangle (or form a degenerated triangle), then you must return 
all angles as 0 (zero). The angles should be represented as a list of integers in ascending order. 
Each angle is measured in degrees and rounded to the nearest integer number (Standard mathematical rounding).

triangle-angles
Input: The lengths of the sides of a triangle as integers.

Output: Angles of a triangle in degrees as sorted list of integers.

Example:

checkio(4, 4, 4) == [60, 60, 60]
checkio(3, 4, 5) == [37, 53, 90]
checkio(2, 2, 5) == [0, 0, 0]

How it is used: This is a classical geometric task. The ideas can be useful in topography and architecture. 
With this concept you can measure an angle without the need for a protractor.

Precondition: 
0 < a,b,c ≤ 1000

三角形的每边都有长度。你需要找到这个三角形的三个角。如果给定的边长度不能形成一个三角形(或者形成一个退化的三角形)，
那么你必须返回所有的角为0(0)。角度应该以升序的整数形式表示。每个角都是用度数来测量的，并四舍五入到最接近的整数
(标准的数学四舍五入)。

triangle-angles
输入:三角形的边长度为整数。

输出:一个三角形的角度，按顺序排列的整数。

如何使用:这是一个经典的几何任务。这些想法可以在地形和建筑方面很有用。有了这个概念，你可以测量一个角度而不需要量角器。
"""

from sympy import *


def checkio(*arg):

	if isinstance(arg[0], list):
		print(arg)
		a = arg[0][0]
		b = arg[0][1]
		c = arg[0][2]
	else:
		a = arg[0]
		b = arg[1]
		c = arg[2]

	if a + b <= c or b + c <= a or a + c <= b:
		return [0, 0, 0] 

	x, y, z,n = symbols('x y z n')
	x = solve(c ** 2 + b ** 2 - a ** 2 - 2 * c  * b * cos(x), x)
	y = solve(a ** 2 + c ** 2 - b ** 2 - 2 * a  * c * cos(y), y)
	z = solve(a ** 2 + b ** 2 - c ** 2 - 2 * a  * b * cos(z), z)
	x = list(j for j in x if j < pi)
	y = list(k for k in y if k < pi)
	z = list(m for m in z if m < pi)
	#print(x,y,z)
	result = []
	for n in (x, y, z):
		result.append(round((180 * n[0] / pi).evalf()))
	print(result)
	return sorted(result, reverse = False)


#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(4, 4, 4) == [60, 60, 60], "All sides are equal"
    assert checkio(3, 4, 5) == [37, 53, 90], "Egyptian triangle"
    assert checkio(2, 2, 5) == [0, 0, 0], "It's can not be a triangle"
    assert checkio(5, 4, 3) == [37, 53, 90], "other"
    assert checkio([10,20,30]) == [0, 0, 0], "0"