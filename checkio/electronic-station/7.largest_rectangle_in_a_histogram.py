"""
"Your power to choose can never be taken from you. 
It can be neglected and it can be ignored. 
But if used, it can make all the difference."
― Steve Goodier

You have a histogram. Try to find size of the biggest rectangle you can build out of the histogram bars.



Input: List of all rectangles heights in histogram

Output: Area of the biggest rectangle

Example:

largest_histogram([5]) == 5
largest_histogram([5, 3]) == 6
largest_histogram([1, 1, 4, 1]) == 4
largest_histogram([1, 1, 3, 1]) == 4
largest_histogram([2, 1, 4, 5, 1, 3, 3]) == 8

How it is used: There is no way the solution you come up with will be any useful in a real life. Just have some fun here.

Precondition:
0 < len(data) < 1000

你选择的力量永远不会被夺走。
它可以被忽略，也可以被忽略。
但如果使用，它会造成所有的不同。
——史蒂夫古蒂
你有一个柱状图。试着找出你可以从直方图上构建的最大矩形的大小。

输入:直方图中所有矩形高度的列表
输出:面积最大的矩形

如何使用:你提出的解决方案在现实生活中是没有任何用处的。只是在这里找点乐子。
"""
def largest_histogram(histogram):
    return max(histogram)


if __name__ == "__main__":
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert largest_histogram([5]) == 5, "one is always the biggest"
    assert largest_histogram([5, 3]) == 6, "two are smallest X 2"
    assert largest_histogram([1, 1, 4, 1]) == 4, "vertical"
    assert largest_histogram([1, 1, 3, 1]) == 4, "horizontal"
    assert largest_histogram([2, 1, 4, 5, 1, 3, 3]) == 8, "complex"
    print("Done! Go check it!")

