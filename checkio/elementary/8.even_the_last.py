"""
You are given an array of integers. You should find the sum of the elements with even indexes (0th, 2nd, 4th...) then multiply this summed number and the final element of the array together. Don't forget that the first element has an index of 0.

For an empty array, the result will always be 0 (zero).

Input: A list of integers.

Output: The number as an integer.

给你一个整数数组。你应该找到具有偶数索引的元素的总和（0，2，4 ...），然后把这个总和数和数组的最后一个元素相乘。不要忘记，第一个元素的索引是0。

对于一个空数组，结果将始终为0（零）。

输入：整数列表。

输出：数字为整数。

例：

checkio （[ 0 ，1 ，2 ，3 ，4 ，5 ] ）== 30       
checkio （[ 1 ，3 ，5 ] ）== 30    
checkio （[ 6 ] ）== 36  
checkio （[ ] ）== 0  

它是如何使用的： 索引和切片是Python和其他语言编码的重要元素。这将派上用场！

前提条件：
0 ≤ len(array) ≤ 20
all(isinstance(x, int) for x in array)
all(-100 < x < 100 for x in array)

"""
def checkio(array):
    """
        sums even-indexes elements and multiply at the last
    """
    if len(array) == 0:
    	return 0
    else:
    	sum = 0
    	for i in range(len(array)):
    		if i % 2 == 0:
    			sum += array[i]
    	return (sum * array[-1])


#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio([0, 1, 2, 3, 4, 5]) == 30, "(0+2+4)*5=30"
    assert checkio([1, 3, 5]) == 30, "(1+5)*5=30"
    assert checkio([6]) == 36, "(6)*6=36"
    assert checkio([]) == 0, "An empty array = 0"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
