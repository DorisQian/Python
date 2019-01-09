'''
The New Year is coming and you have decided to decorate your home. But simple garlands and Christmas 
decorations are so boring, so you have decided to use your programing skills and create something really 
cool and original. Your task is to create class Lamp() and method light() which make lamp to glow by one of 
four color in the sequence - (‘Green’, ‘Red’, ‘Blue’, ‘Yellow’). When the light() method is used at the 
first time the color should be 'Green', at the second time - 'Red' and so on. If the current color is 'Yellow', 
the next color should be 'Green' and so on. In this mission you can use State design pattern. It is used in the 
situations where object should change self behaviour depending on the internal state.

Example:

lamp_1 = Lamp()
lamp_2 = Lamp()

lamp_1.light() #Green
lamp_1.light() #Red
lamp_2.light() #Green
    
lamp_1.light() == "Blue"
lamp_1.light() == "Yellow"
lamp_1.light() == "Green"
lamp_2.light() == "Red"
lamp_2.light() == "Blue"

Input: a few lines indicating the number of lamp inclusions.
Output: color of the lamp.

How it is used: To implement objects with mutable behavior.

Precondition: 4 colors: Green, Red, Blue, Yellow.

新的一年即将到来，你决定装饰你的家。 但简单的花环和圣诞装饰是如此无聊，所以你决定使用你的编程技巧，
创造出一些非常酷和原创的东西。 你的任务是创建类灯（）和方法灯（），使灯以四种颜色之一（'绿色'，'红色'，'蓝色'，'黄色'）
发光。 当第一次使用light（）方法时，颜色应为“绿色”，第二次为“红色”，依此类推。 如果当前颜色是“黄色”，
则下一个颜色应该是“绿色”等等。 在这个任务中你可以使用状态设计模式。 它用于对象根据内部状态改变自我行为的情况。

输入：几行指示灯内含物的数量。
输出：灯的颜色。

如何使用它：实现具有可变行为的对象。

先决条件：4种颜色：绿色，红色，蓝色，黄色。
'''
class Change:
    def __init__(self, color):
        self.color = color
    def switch(self):
        if self.color == 'Green':
            return 'Red'
        elif self.color == 'Red':
            return 'Blue'
        elif self.color == 'Blue':
            return 'Yellow'
        else:
            return 'Green'

class Lamp:
    def __init__(self):
        self.color = ' '

    def light(self):
        color = Change(self.color)
        self.color = color.switch()
        #print(self.color)
        return self.color

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing

    lamp_1 = Lamp()
    lamp_2 = Lamp()

    lamp_1.light() #Green
    lamp_1.light() #Red
    lamp_2.light() #Green
    
    assert lamp_1.light() == "Blue"
    assert lamp_1.light() == "Yellow"
    assert lamp_1.light() == "Green"
    assert lamp_2.light() == "Red"
    assert lamp_2.light() == "Blue"
    print("Coding complete? Let's try tests!")