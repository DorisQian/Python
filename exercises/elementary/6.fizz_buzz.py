"""
Fizz buzz" is a word game we will use to teach the robots about division. Let's learn computers.

You should write a function that will receive a positive integer and return:
"Fizz Buzz" if the number is divisible by 3 and by 5;
"Fizz" if the number is divisible by 3;
"Buzz" if the number is divisible by 5; 
The number as a string for other cases.
Input: A number as an integer.

Output: The answer as a string.

你应该写一个函数，它会收到一个正整数，并返回：
“Fizz Buzz”，如果数字可以被3和5整除; 如果数字可以被3整除，则为
“Fizz” ; 如果数字可以被5整除，则发出
“Buzz” ; 
该数字作为其他情况下的字符串。
输入：一个数字作为一个整数。

输出：答案是一个字符串。

例：

checkio(15) == "Fizz Buzz"
checkio(6) == "Fizz"
checkio(5) == "Buzz"
checkio(7) == "7"

    
它是如何使用的： 在这里，您可以学习如何编写最简单的函数，并使用if-else语句。

先决条件： 0 <number≤1000
"""

# Your optional code here
# You can import some modules or create additional functions


def checkio(number):
    if number % 15 == 0:
        return "Fizz Buzz"
    elif number % 3 == 0:
        return "Fizz"
    elif number % 5 == 0:
        return "Buzz"
    else:
        return str(number)

if __name__ == '__main__':
    assert checkio(15) == "Fizz Buzz", "15 is divisible by 3 and 5"
    assert checkio(6) == "Fizz", "6 is divisible by 3"
    assert checkio(5) == "Buzz", "5 is divisible by 5"
    assert checkio(7) == "7", "7 is not divisible by 3 or 5"

