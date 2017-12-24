"""
You are given an array with positive numbers and a number N. You should find the N-th power of the element in the array with the index N. If N is outside of the array, then return -1. Don't forget that the first element has the index 0.

Let's look at a few examples:
- array = [1, 2, 3, 4] and N = 2, then the result is 32 == 9;
- array = [1, 2, 3] and N = 3, but N is outside of the array, so the result is -1.

Input: Two arguments. An array as a list of integers and a number as a integer.

Output: The result as an integer.

Example:

index_power([1, 2, 3, 4], 2) == 9
index_power([1, 3, 10, 100], 3) == 1000000
index_power([0, 1], 0) == 1
index_power([1, 2], 3) == -1

How it is used: This mission teaches you how to use basic arrays and indexes when combined with simple mathematics.

Precondition: 0 < len(array) ≤ 10
0 ≤ N
all(0 ≤ x ≤ 100 for x in array)

您将得到一个正数和数字N的数组。您应该在索引为N的数组中找到该元素的N次方。如果N在数组之外，则返回-1。不要忘记，第一个元素的索引为0。

我们来看几个例子：
array = [1,2,3,4]，N = 2，结果是3 2 == 9; 
- array = [1，2，3]，N = 3，但是N在数组外，所以结果是-1。

输入：两个参数。一个数组作为一个整数列表和一个整数数字。

输出：结果为整数。
如何使用： 这个任务教你如何使用简单的数学与基本的数组和索引。

"""

def index_power(array, n):
    """
        Find Nth power of the element with index N.
    """
    try:
        return(array[n] ** n)
    except IndexError:
        return -1
    # return array[n] ** n if len(array) > n else -1

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert index_power([1, 2, 3, 4], 2) == 9, "Square"
    assert index_power([1, 3, 10, 100], 3) == 1000000, "Cube"
    assert index_power([0, 1], 0) == 1, "Zero power"
    assert index_power([1, 2], 3) == -1, "IndexError"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
