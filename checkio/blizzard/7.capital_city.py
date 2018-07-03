'''
You are an active traveler who have visited a lot of countries. The main city in the every country is its capital and 
each country can have only one capital city. So your task is to create the class Capital which has some special 
properties: the first created instance of this class will be unique and single, 
and all of the other instances should be the same as the very first one. 
Also you should add the name() method which returns the name of the capital. 
In this mission you should use the Singleton design pattern.

Example:

ukraine_capital_1 = Capital("Kyiv")
ukraine_capital_2 = Capital("London")
ukraine_capital_3 = Capital("Marocco")
ukraine_capital_2.name() == "Kyiv"
ukraine_capital_3.name() == "Kyiv"

Input: The class Capital.

Output: The name of the capital.

How it is used: For creation of a unique object as a single instance.

Precondition: All data is correct.

你是一个活跃的旅行者，曾经访问过很多国家。 每个国家的主要城市都是其首都和
每个国家只能有一个首都。 所以你的任务是创建一个特殊的类Capital
properties：这个类的第一个创建实例将是唯一且单一的，
所有其他实例应与第一个实例相同。
你也应该添加返回大写的name（）方法。
在此任务中，您应该使用Singleton设计模式。
'''


class Singleton(object):
	_instance = None

	def __new__(cls, *args, **kw):
		if not cls._instance:
			cls._instance = super(Singleton, cls).__new__(cls)
		return cls._instance


class Capital(Singleton):
	first_init = True

	def __init__(self, city_name):
		if self.first_init:
			self.cityname = city_name
			self.first_init = False
			#self.__class__.__first_init = False
		#raise NotImplementedError

	def name(self):
		return self.cityname

if __name__ == '__main__':
	#These "asserts" using only for self-checking and not necessary for auto-testing

	ukraine_capital_1 = Capital("Kyiv")
	ukraine_capital_2 = Capital("London")
	ukraine_capital_3 = Capital("Marocco")
	assert ukraine_capital_2.name() == "Kyiv"
	assert ukraine_capital_3.name() == "Kyiv"

	print("Coding complete? Let's try tests!")