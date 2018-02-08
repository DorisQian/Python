'''
You are given a sequence of intervals, as tuples of ints where the tuples are sorted by their first element in ascending order.
It is your task to minimize the number of intervals by merging those that intersect or by removing intervals fitting into another one.

Since the range of values for the intervals is restricted to integers, you must also merge those intervals between which no value can be found.

An example:
Let's say you've got these 5 intervals: 1..6, 3..5, 7..10, 9..12 and 14..16.

1..6 and 3..5
3..5 fits into 1..6, so 3..5 must disappear.
1..6 and 7..10
Even though the intervals do not intersect, there can not be a value of type int between them, so they have to be merged to the new interval 1..10.
1..10 and 9..12
These intervals do intersect, because 9 < 10, so they have to be merged to the new interval 1..12.
1..12 and 14..16
These two intervals do not intersect, so they must not be merged.
So the intervals to be returned are:
1..12 and 14..16
Input: A sequence of intervals as a list of tuples of 2 ints, sorted by their first element.

Output: The merged intervals as a list of tuples of 2 ints, sorted by their first element.

Examples:
merge_intervals([(1, 4), (2, 6), (8, 10), (12, 19)]) == [(1, 6), (8, 10), (12, 19)]
merge_intervals([(1, 12), (2, 3), (4, 7)]) == [(1, 12)]
merge_intervals([(1, 5), (6, 10), (10, 15), (17, 20)]) == [(1, 15), (17, 20)]

Precondition:
intervals == sorted(intervals, key=lambda x: x[0]) # sorted by 1st element of the tuples
interval[0] <= interval[1]

给定一个间隔序列，作为元组的元组，按元素的升序排列第一个元素。
这是你的任务，通过合并那些相交或删除间隔适合到另一个最小化间隔的数量。

由于区间值的范围限制为整数，所以还必须合并那些没有找到值的区间。

一个例子：
假设你有这5个区间：1..6,3..5,7..10,9..12和14..16。

1..6和3..5
3..5适合1..6，所以3..5必须消失。
1..6和7..10
即使区间不相交，它们之间也不能有int类型的值，所以它们必须合并到新的区间1..10。
1..10和9..12
这些间隔相交，因为9 <10，所以它们必须合并到新的间隔1..12。
1..12和14..16
这两个区间不相交，所以不能合并。
所以要返回的时间间隔是：
1..12和14..16
输入：间隔序列，作为2个整数的元组列表，按它们的第一个元素排序。

输出：合并间隔作为2个整数的元组列表，按照它们的第一个元素排序。
'''