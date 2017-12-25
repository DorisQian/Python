"""
From a set of ints you have to create a list of closed intervals as tuples, so the intervals are covering all the values found in the set.

A closed interval includes its endpoints! The interval 1..5, for example, includes each value x that satifies the condition 1 <= x <= 5.

Values can only be in the same interval if the difference between a value and the next smaller value in the set equals one, otherwise a new interval begins. Of course, the start value of an interval is excluded from this rule.
A single value, that does not fit into an existing interval becomes the start- and endpoint of a new interval.

Input: A set of ints.

Output: A list of tuples of two ints, indicating the endpoints of the interval. The Array should be sorted by start point of each interval

Examples:

create_intervals({1, 2, 3, 4, 5, 7, 8, 12}) == [(1, 5), (7, 8), (12, 12)]
create_intervals({1, 2, 3, 6, 7, 8, 4, 5}) == [(1, 8)]

从一组ints中，您必须创建一个作为元组的闭区间列表，因此间隔将覆盖集合中发现的所有值。
闭区间包括它的端点!间隔1 . .例如，包含满足条件1 <= x <= 5的每个值x。
如果值与集合中的下一个较小值之间的差值为1，则值只能在相同的间隔内，否则将开始新的间隔。当然，间隔的开始值被排除在这个规则之外。
一个单独的值，它不适合于一个现有的间隔，成为一个新的间隔的开始和终点。

输入:一组输入。
输出:两个ints的元组列表，表示间隔的端点。每个间隔的起始点应该对数组进行排序
"""
def create_intervals(data):
    """
        Create a list of intervals out of set of ints.
    """
    # your code here
    return None

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert create_intervals({1, 2, 3, 4, 5, 7, 8, 12}) == [(1, 5), (7, 8), (12, 12)], "First"
    assert create_intervals({1, 2, 3, 6, 7, 8, 4, 5}) == [(1, 8)], "Second"
    print('Almost done! The only thing left to do is to Check it!')
