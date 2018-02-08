'''
In computer science and discrete mathematics, an inversion is a pair of places in a sequence where the elements in these places are out of their natural order. So, if we use ascending order for a group of numbers, then an inversion is when larger numbers appear before lower number in a sequence.

Check out this example sequence: (1, 2, 5, 3, 4, 7, 6) and we can see here three inversions
- 5 and 3; - 5 and 4; - 7 and 6.

You are given a sequence of unique numbers and you should count the number of inversions in this sequence.

Input: A sequence as a tuple of integers.

Output: The inversion number as an integer.

Example:

count_inversion((1, 2, 5, 3, 4, 7, 6)) == 3
count_inversion((0, 1, 2, 3)) == 0

How it is used: In this mission you will get to experience the wonder of nested loops, that is of course, if you don't use advanced algorithms.

Precondition: 2 < len(sequence) < 200
len(sequence) == len(set(sequence))
all(-100 < x < 100 for x in sequence)

在计算机科学和离散数学中，反演是一个序列中的一对地方，这些地方的元素超出了它们的自然顺序。 所以，如果我们使用升序来表示一组数字，那么反转就是当较大的数字出现在一个序列中较低的数字之前。

看看这个例子序列：（1，2，5，3，4，7，6），我们可以在这里看到三个反演
- 5和3; - 5和4; - 7和6

给你一个唯一的数字序列，你应该计算在这个序列中的倒数的数量。

输入：一个序列作为整数的元组。

输出：反转数字为整数。

如何使用：在这个任务中，您将体验到嵌套循环的奇迹，当然，如果您不使用高级算法。
'''