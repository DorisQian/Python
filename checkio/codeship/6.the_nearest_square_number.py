'''
You have some number and you are trying to find the nearest square number (a perfect square). Square number is the number the square root of which is an integer. For example, if we start with the number 8, then the two nearby square numbers are 4 (sqrt(4) == 2) and 9 (sqrt(9) == 3). So the answer is 9, because 9 is the nearest.

example

example

Input: A number.

Output: The nearest square number.

Example:

nearest_square(8) == 9
nearest_square(13) == 16
nearest_square(24) == 25
nearest_square(9876) == 9801

How it is used: For mathematical analysis.

Precondition:
0 < number <= 1000000

你有一些数字，你正试图找到最接近的平方数（一个完美的正方形）。 平方数是其平方根是整数的数字。 例如，如果我们从数字8开始，那么附近的两个正方形数字是4（sqrt（4）== 2）和9（sqrt（9）== 3）。 所以答案是9，因为9是最近的。

例

输入：一个数字。
输出：最近的平方数。

如何使用它：用于数学分析。
'''

def nearest_square(number):
    #replace this for solution
    return 0

if __name__ == '__main__':
    print("Example:")
    print(nearest_square(8))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert nearest_square(8) == 9
    assert nearest_square(13) == 16
    assert nearest_square(24) == 25
    assert nearest_square(9876) == 9801
    print("Coding complete? Click 'Check' to earn cool rewards!")