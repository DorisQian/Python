'''
Square roots, cube roots, 4th roots... each are too boring for Nicola. He needs to find 
the super root! With your help he will almost certainly find it.

The super root of a number N is the number x, such that xx = N.

The result should be accurate so that xx ≈ N±0.001. Or N - 0.001 < xx < N + 0.001.

Input: A number (N) as an integer.

Output: The super root (x) as a float or an integer.

Example:
super_root(4) == 2
super_root(27) == 3
super_root(81) == 3.504339593597054
    
How it is used: This concept can be useful for the cryptography. And you will look how work 
your calculator then calculate roots.

Precondition:
1 ≤ number ≤ 10 ** 10

平方根，立方根，第四根......每个都对尼古拉太无聊了。 他需要找到
超级根！ 在你的帮助下，他几乎肯定会找到它。

数字N的超级根是数字x，因此xx = N.

结果应该是准确的，以便xx≈N±0.001。 或N - 0.001 <xx <N + 0.001。

输入：一个数字（N）作为整数。
输出：超级根（x）作为浮点数或整数。

例：
super_root（4）== 2
super_root（27）== 3
super_root（81）== 3.504339593597054
    
它是如何使用的：这个概念对于密码学是有用的。 你会看看工作
你的计算器然后计算根。

前提：
1≤数字≤10 ** 10

二分法
'''


def super_root(number):
    x = 5
    delta = 5
    while abs(x ** x - number) > 0.001:
        delta /= 2
        if x ** x < number:
            x += delta
        else:
            x -= delta
    return x

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    def check_result(function, number):
        result = function(number)
        if not isinstance(result, (int, float)):
            print("The result should be a float or an integer.")
            return False
        p = result ** result
        if number - 0.001 < p < number + 0.001:
            return True
        return False
    assert check_result(super_root, 4), "Square"
    assert check_result(super_root, 9), "Cube"
    assert check_result(super_root, 81), "Eighty one"
