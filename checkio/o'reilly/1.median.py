"""
We have prepared a set of Editor's Choice Solutions. You will see them first 
after you solve the mission. In order to see all other solutions you should change the filter.
elki
A median is a numerical value separating the upper half of a sorted array of 
numbers from the lower half. In a list where there are an odd number of entities, 
the median is the number found in the middle of the array. If the array contains 
an even number of entities, then there is no single middle value, instead the 
median becomes the average of the two numbers found in the middle. For this mission, 
you are given a non-empty array of natural numbers (X). With it, you must separate 
the upper half of the numbers from the lower half and find the median.

Input: An array as a list of integers.

Output: The median as a float or an integer.

Example:

checkio([1, 2, 3, 4, 5]) == 3
checkio([3, 1, 2, 5, 3]) == 3
checkio([1, 300, 2, 200, 1]) == 2
checkio([3, 6, 20, 99, 10, 15]) == 12.5


How it is used: The median has usage for Statistics and Probability theory, it 
has especially significant value for skewed distribution. For example: we want 
to know average wealth of people from a set of data -- 100 people earn $100 in 
month and 10 people earn $1,000,000. If we average it out, we get $91,000. This 
is weird value and does nothing to show us the real picture. In this case the 
median would give to us more useful value and a better picture. The Article at Wikipedia.

Precondition: 
1 < len(data) ≤ 1000
all(0 ≤ x < 10 ** 6 for x in data)

1308/5000  
我们已经准备了一套编辑器的选择方案。在你解决了任务之后，你将会看到他们。为了看到所有
其他的解决方案，你应该改变过滤器。
elki
中位数是一个数字值，它将上半部分和下半部分分开。在有奇数个实体的列表中，中位数是数组
中间的数字。如果数组包含偶数个实体，那么就没有一个中间值，而是中间的两个数字的平均值。
对于这个任务，你会得到一个非空的自然数数组(X)，你必须把上面一半的数字和下半部分分开，然后找到中位数。
输入:作为整数列表的数组。
输出:作为浮点数或整数的中位数。

如何使用:中位数用于统计和概率论，对偏态分布具有特别重要的意义。例如:我们想从一组数据中了
解人们的平均财富——每个月100个人赚100美元，10个人赚100万美元。如果我们把它平均起来，
我们得到91000美元。这是一个奇怪的值，并没有给我们展示真实的图片。在这种情况下，
中值会给我们更有用的价值和更好的图片。在维基百科文章。
"""
def checkio(data):

    length = len(data)
    so_data = sorted(data)
    i = length // 2
    if length % 2 != 0:
    	#print(so_data[i])
    	return so_data[i]
    else:
    	#print((so_data[i] + so_data[i - 1]) / 2)
    	return (so_data[i] + so_data[i - 1]) / 2
#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio([1, 2, 3, 4, 5]) == 3, "Sorted list"
    assert checkio([3, 1, 2, 5, 3]) == 3, "Not sorted list"
    assert checkio([1, 300, 2, 200, 1]) == 2, "It's not an average"
    assert checkio([3, 6, 20, 99, 10, 15]) == 12.5, "Even length"
    print("Start the long test")
    assert checkio(list(range(1000000))) == 499999.5, "Long."
