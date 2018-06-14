'''
You are the active traveler who have visited a lot of countries. The main city in the every country it is the capital of course. And every country can have the only one capital. So you should create class Capital which has a special properties: only one instance of this class could be created and all other instances should be the same as the very first. 
Also you shoud add the name() method which returns the name of the capital. 
In this mission you should use Singleton design pattern.

Example:

ukraine_capital_1 = Capital("Kyiv")
ukraine_capital_2 = Capital("London")
ukraine_capital_3 = Capital("Marocco")
ukraine_capital_2.name() == "Kyiv"
ukraine_capital_3.name() == "Kyiv"

Input: class Capital.
Output: name of the capital.

How it is used: For creation of the unique object as a single instance.

Precondition: All data are correct.

你是访问过很多国家的活跃旅行者。 在每个国家的主要城市当然是首都。 每个国家都有唯一的资本。 因此，您应该创建具有特殊属性的类Capital：只能创建此类的一个实例，而其他所有实例应该与第一个实例相同。
你也应该添加返回大写的name（）方法。
在这个任务中你应该使用Singleton设计模式。

输入：类资本。
输出：大写的名字。

它如何使用：用于创建唯一对象作为单个实例。
'''

class Capital:
    def __init__(self, city_name):
        raise NotImplementedError

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing

    ukraine_capital_1 = Capital("Kyiv")
    ukraine_capital_2 = Capital("London")
    ukraine_capital_3 = Capital("Marocco")

    assert ukraine_capital_2.name() == "Kyiv"
    assert ukraine_capital_3.name() == "Kyiv"

    print("Coding complete? Let's try tests!")