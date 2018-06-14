'''
You are the owner of the cafe, where 3 chefs works: JapaneseCook, RussianCook and ItalianCook. Each of them can cook the national food and drink:
- JapaneseCook: Sushi and Tea
- RussianCook: Dumplings and Compote
- ItalianCook: Pizza and Juice
Your task is to create 3 different subclasses (one for each chef) which are the child of AbstractCook and have these methods:
- add_food(food_amount, food_price), which add to the client's order value of the foods which he had chosen
- add_drink(drink_amount, drink_price), which add to the client's order value of the drinks which he had chosen
- total(), which return string like that: 'Foods: 150, Drinks: 50, Total: 200', and for the each chef instead of Foods and Drinks will be used him national food and drink.
Every client can choose only one chef. In this mission this design patter could help - Abstract Factory.

Example:

client_1 = JapaneseCook()
client_1.add_food(2, 20)
client_1.add_drink(5, 4)
client_1.total() == "Sushi: 40, Tea: 20, Total: 60"

client_2 = RussianCook()
client_2.add_food(1, 40)
client_2.add_drink(5, 20)
client_2.total() == "Dumplings: 40, Compote: 100, Total: 140"

client_3 = ItalianCook()
client_3.add_food(2, 20)
client_3.add_drink(2, 10)
client_3.total() == "Pizza: 40, Juice: 20, Total: 60"

In this mission all data will be correct and you don't need to implement value checking.

Input: Statements and expression with the 3 chef's classes.
Output: The behaviour as described.

How it is used: Work with classes and object-oriented programming - is a high level which you should learn for using full benefits of Python.

Precondition: All data are correct.

你是咖啡馆的老板，有3位厨师工作：JapaneseCook，RussianCook和ItalianCook。 他们每个人都可以烹饪民族食品和饮料：
- 日本料理：寿司和茶
- RussianCook：饺子和蜜饯
- ItalianCook：比萨和果汁
您的任务是创建3个不同的子类（每个厨师一个子类），它们是AbstractCook的子类，并具有以下方法：
- add_food（food_amount，food_price），这增加了他选择的食物的客户订单价值
- add_drink（drink_amount，drink_price），这增加了他选择的饮料的客户订单价值
- total（），返回这样的字符串：'Foods：150，Drinks：50，Total：200'，并且为每个厨师而不是Foods and Drinks将使用他的民族食品和饮料。
每个客户只能选择一位厨师。 在这个任务中，这个设计模式可以帮助 - 抽象工厂。

输入：3个主厨的课堂陈述和表达。
输出：描述的行为。

它是如何使用的：使用类和面向对象的编程 - 是一个高层次，您应该学习使用Python的全部优点。

先决条件：所有数据都是正确的。
'''

class AbstractCook:
    pass

class JapaneseCook(AbstractCook):
    pass

class RussianCook(AbstractCook):
    pass

class ItalianCook(AbstractCook):
    pass


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing

    client_1 = JapaneseCook()
    client_1.add_food(2, 30)
    client_1.add_drink(2, 10)

    client_2 = RussianCook()
    client_2.add_food(1, 40)
    client_2.add_drink(5, 20)

    client_3 = ItalianCook()
    client_3.add_food(2, 20)
    client_3.add_drink(2, 10)

    assert client_1.total() == "Sushi: 60, Tea: 20, Total: 80"
    assert client_2.total() == "Dumplings: 40, Compote: 100, Total: 140"
    assert client_3.total() == "Pizza: 40, Juice: 20, Total: 60"
    print("Coding complete? Let's try tests!")
