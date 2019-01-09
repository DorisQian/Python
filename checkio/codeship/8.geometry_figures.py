'''
You often work with the different geometrical figures and with their parameters - the perimeter, area, and volume. 
You are tired of doing it manually, so you’ve decided to automate this process, and therefore you need to write a 
particular program. In this program you should create the class Parameters which will choose one of the few figures 
(the circle, right triangle, square, right pentagon, right hexagon, cube) using the choose_figure() method and will 
count the perimeter, area, and volume with the help of the following methods:

perimeter() - returns the perimeter of the figure;
area() - returns the area of the figure;
volume() - returns the volume of the figure.

Also you have to create a class for each figure and use the Strategy design pattern to solve this mission.
此外，您还必须为每个图形创建一个类，并使用策略设计模式来解决此任务。
Every figure, except the cube, has the volume = 0.
If the result has no decimal places, you should return it as int(), in other case - round it to the 2 decimal points.

Examples:

figure = Parameters(10)
    
figure.choose_figure(Circle())
figure.area() == 314.16

figure.choose_figure(Triangle())
figure.perimeter() == 30

figure.choose_figure(Square())
figure.area() == 100

figure.choose_figure(Pentagon())
figure.perimeter() == 50

figure.choose_figure(Hexagon())
figure.perimeter() == 60

figure.choose_figure(Cube())
figure.volume() == 1000

Input: Statements and expressions of the classes.

Output: The perimeter, area, and volume (number).

Hot it is used: For the geometrical object analysis.

Precondition: All data is correct.

您经常使用不同的几何图形及其参数 - 周长，面积和体积。 您已厌倦手动执行此操作，因此您决定自动执行此过程，
因此您需要编写特定程序。 在这个程序中你应该创建类参数，它将使用choose_figure（）方法选择少数几个图形（圆形，
直角三角形，正方形，右五边形，右六边形，立方体）之一，并计算周长，面积和体积 借助以下方法：


from math import pi, sqrt


class Circle:
	def __init__(self, *args):
		self.args = args

	def get_area(self):
		return pi * self.args[0] ** 2

	def get_perimeter(self):
		return 4 * pi * self.args

	def get_volume(self):
		return 0


class Triangle(Circle):
	def get_area(self):
		a, b, c = self.args
		p = (a + b + c) / 2
		return sqrt(p * (p - a) * (p - b) * (p - c))

	def get_perimeter(self):
		return self.args[0] + self.args[1] + self.args[2]



class Rectangle(Circle):
	def get_area(self):
		return self.args[0] * self.args[1]

	def get_perimeter(self):
		return 2 * (self.args[0] + self.args[1])


class Pentagon(Circle):
	#def get_area(self):
	def get_perimeter(self):
		return 5 * self.args[0]


class Hexagon(Circle):
	def get_perimeter(self):
		return 6 * self.args[0]


class Cube(Circle):
	def get_area(self):
		return 0

	def get_perimeter(self):
		return 0

	def get_volume(self):
		return self.args[0] ** 3

class Figure:
	def __init__(self, name, *args):
		#raise NotImplementedError
		self.name = name
		self.args = args
		self.choose_figure(self.name)

	def choose_figure(self, geometry):
		if geometry == 'circle':
			self.geometry = Circle(*self.args)
		elif geometry == 'triangle':
			self.geometry = Triangle(*self.args)
		elif geometry == 'rectangle':
			self.geometry = Rectangle(*self.args)
		elif geometry == 'pentagon':
			self.geometry = Pentagon(*self.args)
		elif geometry == 'hexagon':
			self.geometry = Hexagon(*self.args)
		elif geometry == 'cube':
			self.geometry = Cube(*self.args)

	def area(self):
		area = self.geometry.get_area()
		if type(area) == int:
			return area
		else:
			if str(area).split('.')[1] == 0:
				return int(area)
			else:
				return round(area, 2)

	def volume(self):
		volume = self.geometry.get_volume()
		if type(volume) == int:
			return volume
		else:
			if str(volume).split('.')[1] == 0:
				return int(volume)
			else:
				return round(volume, 2)

	def perimeter(self):
		perimeter =  self.geometry.get_perimeter()
		if type(perimeter) == int:
			return perimeter
		else:
			if str(perimeter).split('.')[1] == 0:
				return int(perimeter)
			else:
				return round(perimeter, 2)
'''
from math import sqrt, pi


class Circle:
	def get_area(self, args):
		return pi * args ** 2

	def get_perimeter(self, args):
		return 2 * pi * args

	def get_volume(self,args):
		return 0


class Triangle(Circle):
	def get_area(self, args):
		return sqrt(3) * args ** 2 / 4

	def get_perimeter(self, args):
		return args * 3


class Square(Circle):
	def get_area(self, args):
		return args ** 2

	def get_perimeter(self, args):
		return 4 * args


class Pentagon(Circle):
	def get_area(self, args):
		return args ** 2 * sqrt(25 + 10 * sqrt(5)) / 4

	def get_perimeter(self, args):
		return 5 * args


class Hexagon(Circle):
	#六个正三角形
	def get_area(self,args):
		return 6 * sqrt(3) * args ** 2 / 4

	def get_perimeter(self, args):
		return 6 * args


class Cube(Circle):
	def get_area(self, args):
		return 6 * args ** 2

	def get_perimeter(self, args):
		return 12 * args

	def get_volume(self, args):
		return args ** 3


class Parameters:
	def __init__(self, args):
		#raise NotImplementedError
		self.args = args

	def choose_figure(self, geometry):
		self.figure = geometry

	def area(self):
		area = self.figure.get_area(self.args)
		if type(area) == int:
			return area
		else:
			if str(area).split('.')[1] == 0:
				return int(area)
			else:
				return round(area, 2)

	def volume(self):
		volume = self.figure.get_volume(self.args)
		if type(volume) == int:
			return volume
		else:
			if str(volume).split('.')[1] == 0:
				return int(volume)
			else:
				return round(volume, 2)

	def perimeter(self):
		perimeter = self.figure.get_perimeter(self.args)
		if type(perimeter) == int:
			return perimeter
		else:
			if str(perimeter).split('.')[1] == 0:
				return int(perimeter)
			else:
				return round(perimeter, 2)

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing

    #assert Figure("circle", 10).area() == 314.16
    #assert Figure("triangle", 3, 4, 5).volume() == 0
    #assert Figure("rectangle", 1.5, 2.5).area() == 3.75
    #assert Figure("pentagon", 500).perimeter() == 2500
    #assert Figure("hexagon", 100.003).perimeter() == 600.02
    #assert Figure("cube", 20).volume() == 8000
    figure = Parameters(10)
    figure.choose_figure(Circle())
    assert figure.area() == 314.16

    figure = Parameters(100)
    figure.choose_figure(Circle())
    assert figure.volume() == 0

    figure = Parameters(3.3)
    figure.choose_figure(Triangle())
    assert figure.perimeter() == 9.9

    figure = Parameters(5)
    figure.choose_figure(Triangle())
    assert figure.area() == 10.83

    figure = Parameters(10)
    figure.choose_figure(Triangle())
    assert figure.volume() == 0

    figure = Parameters(3)
    figure.choose_figure(Square())
    assert figure.perimeter() == 12

    figure = Parameters(5)
    figure.choose_figure(Square())
    assert figure.area() == 25

    figure = Parameters(2.5)
    figure.choose_figure(Square())
    assert figure.volume() == 0

    
    figure = Parameters(10)
    figure.choose_figure(Pentagon())
    assert figure.perimeter() == 50

    figure = Parameters(10)
    figure.choose_figure(Pentagon())
    assert figure.area() == 172.05
   

    figure = Parameters(10)
    figure.choose_figure(Hexagon())
    assert figure.area() == 259.81
           


    figure = Parameters(10)
    figure.choose_figure(Cube())
    assert figure.perimeter() == 120

    figure = Parameters(10)
    figure.choose_figure(Cube())
    assert figure.area() == 600


    print("Coding complete? Let's try tests!")
