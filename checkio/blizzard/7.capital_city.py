'''
You are an active traveler who have visited a lot of countries. The main city in the every country is its capital and each country can have only one capital city. So your task is to create the class Capital which has some special properties: the first created instance of this class will be unique and single, and all of the other instances should be the same as the very first one. 
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