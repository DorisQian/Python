'''
Metal strips, pipes, rods, etc. are being delivered in lengths of 6000 millimeters 
(6 meters). We want to cut them into pieces of different lengths.

Write a piece of code that finds how to do this in the most efficient way, that is, 
with the least possible quantity of material wasted. You are given the requested pipe 
lengths (as a list of integers). You should find the most efficient way of cutting, 
and return the sum of the wasted pipe length.

Input: A 'BOM' (Bill Of Materials), a list of lengths in millimeters that have to be 
cut (list of integer).

Output: The sum of wasted pipe length (Integer).

Example:

most_efficient_cutting([3000, 2200, 2000, 1800, 1600, 1300]) == 100
most_efficient_cutting([4000, 4000, 4000]) == 6000

How it is used:
To find the most efficient way of using the given resources.

Precondition:
all(1 <= b <= 6000 for b in bom)

金属带，管道，棒等正在交付6000毫米的长度
（6米）。 我们想把它们切成不同长度的碎片。

写一段代码，找出如何以最有效的方式做到这一点，也就是说，
尽可能少的材料浪费。 您将获得所需的管道
长度（作为整数列表）。 你应该找到最有效的切割方式，
并返回浪费的管道长度的总和。

输入：'BOM'（材料清单），必须是以毫米为单位的长度列表
剪切（整数列表）。
输出：浪费的管道长度的总和（整数）。

如何使用它：
找到使用给定资源的最有效方式。

前提：
全部（b <b>中1 <= b <= 6000）
'''