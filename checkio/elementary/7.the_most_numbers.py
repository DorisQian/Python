"""
You are given an array of numbers (floats). You should find the difference between the maximum and minimum element. Your function should be able to handle an undefined amount of arguments. For an empty argument list, the function should return 0.

Floating-point numbers are represented in computer hardware as base 2 (binary) fractions. So we should check the result with ±0.001 precision.
Think about how to work with an arbitrary number of arguments.

Input: An arbitrary number of arguments as numbers (int, float).

Output: The difference between maximum and minimum as a number (int, float).

给你一个数组（浮点数）。你应该找到最大和最小元素的区别。你的函数应该能够处理一个未定义数量的参数。对于一个空的参数列表，该函数应该返回0。

计算机硬件中将浮点数表示为基2（二进制）分数。所以我们应该以±0.001的精度检查结果。
想想如何处理任意数量的参数。

输入：任意数量的参数作为数字（int，float）。

输出：最大值和最小值的差值（int，float）。

例：

checkio （1 ，2 ，3 ）== 2    
checkio （5 ，- 5 ）== 10   
checkio （10.2 ，- 2.2 ，0 ，1.1 ，0.5 ）== 12.4      
checkio （）== 0  
    
它是如何使用的： 在这里，您将学习如何将不定数量的参数传递给函数。

前提条件： 0 ≤ len(args) ≤ 20
all(-100 < x < 100 for x in args)
all(isinstance(x, (int, float)) for x in args)

def checkio(*args):
    return 0

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    def almost_equal(checked, correct, significant_digits):
        precision = 0.1 ** significant_digits
        return correct - precision < checked < correct + precision

    assert almost_equal(checkio(1, 2, 3), 2, 3), "3-1=2"
    assert almost_equal(checkio(5, -5), 10, 3), "5-(-5)=10"
    assert almost_equal(checkio(10.2, -2.2, 0, 1.1, 0.5), 12.4, 3), "10.2-(-2.2)=12.4"
    assert almost_equal(checkio(), 0, 3), "Empty"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")


"""

def checkio(*args):
    return 0

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    def almost_equal(checked, correct, significant_digits):
        precision = 0.1 ** significant_digits
        return correct - precision < checked < correct + precision

    assert almost_equal(checkio(1, 2, 3), 2, 3), "3-1=2"
    assert almost_equal(checkio(5, -5), 10, 3), "5-(-5)=10"
    assert almost_equal(checkio(10.2, -2.2, 0, 1.1, 0.5), 12.4, 3), "10.2-(-2.2)=12.4"
    assert almost_equal(checkio(), 0, 3), "Empty"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
