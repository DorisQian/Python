"""
The Hamming distance between two binary integers is the number of bit positions that differs (read more about the Hamming distance on Wikipedia). For example:

    117 = 0 1 1 1 0 1 0 1
     17 = 0 0 0 1 0 0 0 1
      H = 0+1+1+0+0+1+0+0 = 3

You are given two positive numbers (N, M) in decimal form. You should calculate the Hamming distance between these two numbers in binary form.

Input: Two arguments as integers.

Output: The Hamming distance as an integer.

Example:

checkio(117, 17) == 3
checkio(1, 2) == 2
checkio(16, 15) == 5

How it is used: This is a basis for Hamming code and other linear error-correcting programs. The Hamming distance is used in systematics as a measure of genetic distance. On a grid (ie: a chessboard,) the Hamming distance is the minimum number of moves it would take a rook to move from one cell to the other.

Precondition:
0 < n < 106
0 < m < 106

两个二进制整数之间的汉明距离是不同的位(在维基百科上读到汉明距离的更多信息)。

你得到了两个正数(N,M)的小数形式。你应该用二进制的形式计算这两个数之间的汉明距离。

输入:两个作为整数的参数。
输出:汉明距离为整数。

如何使用:这是汉明码和其他线性纠错程序的基础。汉明距离作为一种测量遗传距离的方法被用于系统。在网格上(例如:棋盘)，汉明距离是移动从一个单元到另一个单元的最小移动次数。


"""

def checkio(n, m):
	'''
	i = bin(n ^ m)
	count = i.count('1')
	return count
	'''
	return bin(n ^ m).count('1')
    


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(117, 17) == 3, "First example"
    assert checkio(1, 2) == 2, "Second example"
    assert checkio(16, 15) == 5, "Third example"
