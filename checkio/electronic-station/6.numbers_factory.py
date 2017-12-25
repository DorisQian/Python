"""
You are given a two or more digits number N. For this mission, you should find the smallest positive number of X, such that the product of its digits is equal to N. If X does not exist, then return 0.

Let's examine the example. N = 20. We can factorize this number as 2*10, but 10 is not a digit. Also we can factorize it as 4*5 or 2*2*5. The smallest number for 2*2*5 is 225, for 4*5 -- 45. So we select 45.

Hints: Remember prime numbers (numbers divisible by only one) and be careful with endless loops.

Input: A number N as an integer.

Output: The number X as an integer.

Example:

checkio(20) == 45
checkio(21) == 37
checkio(17) == 0
checkio(33) == 0

How it is used: This task will teach you how to work with numbers in code. You can factorize numbers and reconstruct them into new numbers. Of course you can solve this problem with brute force, but is that the best way? Numbers are the foundation of mathematics and programming.

Precondition: 
9 < N < 105.

你得到一个两个或更多的数字n，为了这个任务，你应该找到最小的正数X，这样它的数字的乘积等于n，如果X不存在，则返回0。
让我们看看这个例子。N = 20。我们可以把这个数分解成2 * 10，但10不是一个数字。也可以把它分解成4 * 5或2 *2* 5。2*2* 5的最小值是225,4 *5 - 45。所以我们选择45。
提示:记住素数(只可被1整除的数)，并且要小心无穷循环。


输入:数字N为整数。
输出:X作为一个整数。

如何使用:这个任务将教会你如何处理代码中的数字。你可以将数字分解并重新构造成新的数字。当然你可以用蛮力来解决这个问题，但是这是最好的方法吗?数字是数学和编程的基础。
"""
def checkio(number):
    #replace this for solution
    return 0

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(20) == 45, "1st example"
    assert checkio(21) == 37, "2nd example"
    assert checkio(17) == 0, "3rd example"
    assert checkio(33) == 0, "4th example"
    assert checkio(3125) == 55555, "5th example"
    assert checkio(9973) == 0, "6th example"
