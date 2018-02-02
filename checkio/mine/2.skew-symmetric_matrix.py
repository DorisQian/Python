'''
In mathematics, particularly in linear algebra, a skew-symmetric matrix
(also known as an antisymmetric or antimetric) is a square matrix A whose 
transpose is also its negative. This means it satisfies the equation A = −AT. 
If the entry in the i-th row and j-th column is aij, i.e. A = (aij) then the 
symmetric condition becomes aij = −aji.

You should determine whether the specified square matrix is skew-symmetric or not.

You can find more details on Skew-symmetric matrices on its Wikipedia page.

Input: A square matrix as a list of lists with integers.

Output: If the matrix is skew-symmetric or not as a boolean.

Example:

checkio([
    [ 0,  1,  2],
    [-1,  0,  1],
    [-2, -1,  0]]) == True
checkio([
    [ 0,  1, 2],
    [-1,  1, 1],
    [-2, -1, 0]]) == False
checkio([
    [ 0,  1, 2],
    [-1,  0, 1],
    [-3, -1, 0]]) == False

How it is used: Skew-symmetric matrices can be useful for the cross product, 
an operation in mathematics used in the calculation of movement of forces. Matrixes 
are basis for the linear algebra and vector graphics.

Precondition: 0 < N < 5

在数学中，特别是在线性代数中，是一个斜对称矩阵
（也称为反对称或反对称）是一个方阵A
转置也是它的负面影响。 这意味着它满足等式A = -AT。
如果第i行和第j列中的条目是aij，即A =（aij），那么
对称条件变成aij = -aji。

您应该确定指定的方形矩阵是否是斜对称的。
你可以在Wikipedia页面找到更多关于斜对称矩阵的细节。

输入：方阵作为整数列表的列表。
输出：如果矩阵是斜对称的或不是布尔值。

它是如何使用的：斜对称矩阵可以用于交叉乘积，
用于计算力的运动的数学运算。矩阵是线性代数和矢量图形的基础。
'''
def checkio(matrix):
    return True or False


#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio([
        [0, 1, 2],
        [-1, 0, 1],
        [-2, -1, 0]]) == True, "1st example"
    assert checkio([
        [0, 1, 2],
        [-1, 1, 1],
        [-2, -1, 0]]) == False, "2nd example"
    assert checkio([
        [0, 1, 2],
        [-1, 0, 1],
        [-3, -1, 0]]) == False, "3rd example"
