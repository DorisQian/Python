"""
If you have 50 different plug types, appliances wouldn't be available and would be very expensive. 
But once an electric outlet becomes standardized, many companies can design appliances, and competition ensues, 
creating variety and better prices for consumers. 
-- Bill Gates

You are given a non-empty list of integers (X). For this task, you should return a list consisting of only the 
non-unique elements in this list. To do so you will need to remove all unique elements (elements which are 
contained in a given list only once). When solving this task, do not change the order of the list. 
Example: [1, 2, 3, 1, 3] 1 and 3 non-unique elements and result will be [1, 3, 1, 3].


Input: A list of integers.

Output: The list of integers.

Example:

checkio([1, 2, 3, 1, 3]) == [1, 3, 1, 3]
checkio([1, 2, 3, 4, 5]) == []
checkio([5, 5, 5, 5, 5]) == [5, 5, 5, 5, 5]
checkio([10, 9, 10, 10, 9, 8]) == [10, 9, 10, 10, 9]

How it is used: This mission will help you to understand how to manipulate arrays, something that is the basis 
for solving more complex tasks. The concept can be easily generalized for real world tasks. 
For example: if you need to clarify statistics by removing low frequency elements (noise).

You can find out more about Python arrays in one of our articles featuring lists, tuples, array.array 
and numpy.array.

Precondition:
0 < len(data) < 1000

如果你有50种不同的插头类型，电器就无法使用，而且会非常昂贵。
但是一旦一个电源插座标准化了，许多公司就可以设计家用电器了，于是竞争就开始了。
为消费者创造多样化和更好的价格。
——比尔盖茨

您得到一个非空的整数列表(X)。对于这个任务，您应该返回一个仅由该列表组成的列表
列表中的非唯一元素。要做到这一点，您需要删除所有的唯一元素(元素
只包含在一个列表中一次)。在解决这个任务时，不要改变列表的顺序。
例:[1,2,3,1,3]1和3非唯一元素，结果将是[1,3,1,3]。


输入:一个整数的列表。

输出:整数的列表。

例子:

checkio([1,2,3,1,3])= =[1,3,1,3]
checkio([1,2,3,4,5])= =[]
checkio([5,5,5,5,5])= =[5,5,5,5,5]
checkio([10、9、10、10、9、8])= =(10、9、10、10、9]

如何使用:这个任务将帮助您了解如何操作数组，这是基础
用于解决更复杂的任务。这个概念可以很容易地概括为现实世界的任务。
例如:如果您需要通过删除低频率元素(噪声)来澄清统计信息。

您可以在我们的一篇文章中找到更多关于Python数组的信息，其中有一个列表，tuple,array. array
和numpy.array。

先决条件:
0 < len(data)< 1000
"""

#Your optional code here
#You can import some modules or create additional functions

from collections import Counter
def checkio(data):
    
    return (i for i in data if data.count(i) >1 )
    return filter(lambda x : data.count(x) > 1, data)
    counter = Counter(data)
    return (item for item in data if counter[item] > 1)

if __name__ == "__main__":
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert list(checkio([1, 2, 3, 1, 3])) == [1, 3, 1, 3], "1st example"
    assert list(checkio([1, 2, 3, 4, 5])) == [], "2nd example"
    assert list(checkio([5, 5, 5, 5, 5])) == [5, 5, 5, 5, 5], "3rd example"
    assert list(checkio([10, 9, 10, 10, 9, 8])) == [10, 9, 10, 10, 9], "4th example"
    print("It is all good. Let's check it now")