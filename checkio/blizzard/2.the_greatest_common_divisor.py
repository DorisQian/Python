'''
"[The Euclidean algorithm] is the granddaddy of all algorithms, because it is the oldest nontrivial algorithm that has survived to the present day."
-- Donald Knuth, The Art of Computer Programming, Vol. 2: Seminumerical Algorithms, 2nd edition (1981).

The greatest common divisor (GCD), also known as the greatest common factor of two or more integers (at least one of which is not zero), is the largest positive integer that divides a number without a remainder. For example, the GCD of 8 and 12 is 4.

You are given an arbitrary number of positive integers. You should find the greatest common divisor for these numbers.

Input: An arbitrary number of positive integers.

Output: The greatest common divisor as an integer.

Example:

great_common_divisor(6, 4) == 2
great_common_divisor(2, 4, 8) == 2

How it is used: GCD is a basic concept found in mathematically oriented software. This is a good example of a simple algorithm which has many possible applications.

Precondition: 
1 < len(args) ≤ 10
all(0 < x ≤ 2 ** 32 for x in args)

“[欧几里德算法]是所有算法的祖父，因为它是迄今存活到今天的最古老的非平凡算法。”
- Donald Knuth，计算机编程艺术，Vol。 2：Seminumerical Algorithms，第2版（1981年）。

最大公约数（GCD）也称为两个或多个整数（其中至少有一个不为零）的最大公因数，是除数之外没有余数的最大正整数。 
例如，8和12的GCD是4。

给你任意数量的正整数。 你应该找到这些数字的最大公约数。

输入：任意数量的正整数。
输出：最大公约数为整数。

如何使用它：GCD是数学导向软件中的一个基本概念。 这是一个简单算法的很好的例子，它有许多可能的应用。
'''

def greatest_common_divisor(*args):
    """
    效率低
    1
    m = min(args)
    appro = [i for i in range(1, m + 1) if m % i == 0]
    appro.reverse()

    for n in appro:
    	count = 0
    	for j in args:
    		if j % n == 0:
    			count += 1
    	if count == len(args):
    		return n
	2
    m = min(args)
    for i in range(m, 0, -1):
    	if m % i == 0:
    		count = 0
    		for n in args:
    			if n % i == 0:
    				count += 1
    		if count == len(args):
    			return i
    """
from functools import reduce
gcd = lambda a, b: a if b == 0 else gcd(b, a % b)
greatest_common_divisor = lambda *args: reduce(gcd, args)

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert greatest_common_divisor(6, 4) == 2, "Simple"
    assert greatest_common_divisor(2, 4, 8) == 2, "Three arguments"
    assert greatest_common_divisor(2, 3, 5, 7, 11) == 1, "Prime numbers"
    assert greatest_common_divisor(3, 9, 3, 9) == 3, "Repeating arguments"