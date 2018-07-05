'''
The singularity has happened and we are being made to build the ideal robo-city for our overlords. In this shining robotropolis, all buildings will be rectangular and all streets laid along south-north and east-west lines in a glorious grid. Before we get started, we to create a class to represent the perfect building.

Because all the buildings in the city are rectangular and their walls are parallel to the streets, we can define any building using only the coordinates of South-Western corner as two arguments (the length of the west to east walls, and the length of the north to south wall) along with the height of the building. These values are described as positive numbers using conventional units. The origin point of our coordinate system lies in the South-West , as a result the northern corner ends up having the greater coordinate value than the southern corner. To complete this mission we need to use a couple operations. See the class description below.

class Building(south, west, width_WE, width_NS, height=10)

Returns a new Building instance with the South-West corner at [south, west] coordinates, the size is width_WE by width_NS and the height of the building is height. "height" is a positive number with a default value of 10.

>>> Building(10, 10, 1, 2, 2)
Building(10, 10, 1, 2, 2)
>>> Building(0, 0, 10.5, 2.546)
Building(0, 0, 10.5, 2.546, 10)

corners()

Returns a dictionary with the coordinates of the building corners. The dictionary has following keys: "north-west", "north-east", "south-west", "south-east". The values are lists or tuples with two numbers.

>>> Building(1, 2, 2, 2).corners()
{"north-west": [3, 2], "north-east": [3, 4], "south-west": [1, 2], "south-east": [1, 4]}

area()

Returns the area of the building.

>>> Building(1, 2.5, 4.2, 1.25).area()
5.25

volume()

Returns the volume of the building.

>>> Building(1, 2.5, 4.2, 1.25, 101).volume()
530.25

__repr__()

This is a string representation of the Building. This method is used for "print" or "str" conversion. Returns the string in the following view:
"Building({south}, {west}, {width_we}, {width_ns}, {height})"
>>> str(Building(0, 0, 10.5, 2.546))
"Building(0, 0, 10.5, 2.546, 10)"

In this mission all data will be correct and you don't need to implement value checking.

Input: Statements and expression with the Building class.

Output: The behaviour as described.

How it is used: Here you will learn how to write a simple class with minimal functionality to achieve greater glory for Robonia.

Precondition: All data are correct.

这个奇点已经发生了，我们正在为我们的地主建造一个理想的机器城市。在这个闪耀的机器人世界中，所有的建筑物都是长方形的，所有的街道都沿着南北线和东西线布置在一个光辉的格子里。在我们开始之前，我们要创建一个类来代表完美的建筑。

因为城市中的所有建筑物都是长方形的，而且它们的墙壁与街道平行，所以我们可以只用西南角的坐标来定义任何建筑物作为两个参数（西墙到东墙的长度，以及北至南墙）以及建筑物的高度。这些值被描述为使用传统单位的正数。我们的坐标系的原点位于西南方，因此北角的坐标值比南角的坐标值大。要完成这个任务，我们需要使用几个操作。请参阅下面的课程描述。

（南，西，宽度_WE，宽度_NS，高度= 10）

返回坐标为[south，west]的西南角的新建筑实例，尺寸为width_WE，宽度为NS，建筑物的高度为高度。 “高度”是一个默认值为10的正数。

角（）

返回具有建筑物角落坐标的字典。该词典有以下键：“西北”，“东北”，“西南”，“东南”。值是两个数字的列表或元组。

区（）

返回建筑物的面积。

卷（）

返回建筑物的体积。


__repr __（）

这是建筑物的字符串表示形式。此方法用于“打印”或“str”转换。返回以下视图中的字符串：

在这个任务中，所有的数据都是正确的，你不需要执行值检查。

输入：建筑类的语句和表达式。
输出：描述的行为。

如何使用：在这里，您将学习如何编写一个简单的类与最小的功能，以实现更大的荣耀Robonia。

先决条件：所有的数据都是正确的。
'''

class Building:
    def __init__(self, south, west, width_WE, width_NS, height=10):
        self.south = south
        self.west = west
        self.width = width_WE
        self.length = width_NS
        self.height = height

    def corners(self):
        corner = dict()
        corner['south-west'] = [self.south, self.west]
        corner['north-west'] = [self.south + self.length, self.west]
        corner['south-east'] = [self.south, self.west + self.width]
        corner['north-east'] = [self.south + self.length, self.west + self.width]
        return corner

    def area(self):
        return self.length * self.width

    def volume(self):
        return self.length * self.width * self.height

    def __repr__(self):
        return ('Building({0.south}, {0.west}, {0.width}, {0.length}, {0.height})'.format(self))


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    def json_dict(d):
        return dict((k, list(v)) for k, v in d.items())

    b = Building(1, 2, 2, 3)
    b2 = Building(1, 2, 2, 3, 5)
    assert json_dict(b.corners()) == {'north-east': [4, 4], 'south-east': [1, 4],
                                      'south-west': [1, 2], 'north-west': [4, 2]}, "Corners"
    assert b.area() == 6, "Area"
    assert b.volume() == 60, "Volume"
    assert b2.volume() == 30, "Volume2"
    assert str(b) == "Building(1, 2, 2, 3, 10)", "String"
