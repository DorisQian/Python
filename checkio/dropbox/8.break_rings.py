'''
A blacksmith gave his apprentice a task, ordering them to make a selection of rings. 
The apprentice is not yet skilled in the craft and as a result of this, some (to be 
honest, most) of rings came out connected together. Now he's asking for your help 
separating the rings and deciding how to break enough rings to free so as to get the 
maximum number of rings possible.

All of the rings are numbered and you are told which of the rings are connected. This 
information is given as a sequence of sets. Each set describes the connected rings. For 
example: {1, 2} means that the 1st and 2nd rings are connected. You should count how many 
rings we need to break to get the maximum of separate rings. Each of the rings are numbered 
in a range from 1 to N, where N is total quantity of rings.

example-rings

In the above image you can see the connections: [[1,2],[2,3],[3,4],[4,5],[4,6],[6,5]]. The 
optimal solution here would be to break 3 rings, making 3 full and separate rings. So the result is 3.

Input: Information about the connected rings as a tuple of sets with integers.

Output: The number of rings to break as an integer.

Example:

break_rings(({1, 2}, {2, 3}, {3, 4}, {4, 5}, {4, 6}, {6, 5})) == 3

How it is used: This model specializes in optimizing something with specific conditions. 
Using the basic concepts, you could create a model for improving a transportation grid.

Precondition: all(len(s) == 2 for s in rings)
sorted(reduce(set.union, rings)) == list(range(1, max(reduce(set.union, rings)) + 1))


一名铁匠给了他的学徒一项任务，命令他们挑选戒指。
学徒对技艺还不熟练，因此，有些人（待定）
诚实，大多数）戒指连接在一起。现在他正在寻求你的帮助
分开戒指，并决定如何打破足够的戒指，以获得自由
可能的最大圈数。

所有的环都被编号，你会被告知哪个环被连接。这个
信息是作为一系列的集合给出的。每组描述连接的环。对于
例如：{1，2}表示第一个和第二个环连接。你应该算多少
我们需要打破戒指以获得最大的单独戒指。每个环都被编号
范围从1到N，其中N是环的总数量。

例如环

在上图中，您可以看到连接：[[1,2]，[2,3]，[3,4]，[4,5]，[4,6]，[6,5]]。该
这里的最佳解决方案是打破3个戒指，制造3个完整戒指。所以结果是3。

输入：关于连接环的信息作为具有整数的集合的元组。
输出：作为整数中断的振铃数。


如何使用：该模型专门针对特定条件进行优化。
使用基本概念，您可以创建一个改善交通网格的模型。
set update,将整理拆分成个体，添加到set中
'''

'''
def break_rings(rings):
	now = list(rings)
	count = 0
	while len(now):
		number = []
		for ring in now:
			number.append(list(ring)[0])
			number.append(list(ring)[1])
		set_number = set(number)

		n = max([number.count(i) for i in set_number])
		refer = dict()
		max_num = [i for i in set_number if number.count(i) == n]
		neighbor = []
		if len(max_num) == 0:
				continue
		elif len(max_num) == 1:
			max_number = max_num[0]
		else:
			for i in max_num:
				relation = [x for x in now if i in x]
				for x in relation:
					if list(x)[0] == i:
						neighbor.append(list(x)[1])
					else:
						neighbor.append(list(x)[0])
				cou = 0
				for j in neighbor:
					cou += number.count(j)
				refer[i] = cou
			max_number = min([k for k, v in refer.items() if v == min(refer.values())])

		for ring in rings:
			if max_number in ring and ring in now:
				now.remove(ring)
				number.remove(max_number)
		count += 1

	print(count)
	return count
	'''
import itertools
def break_rings(rings):
	link_map = {}
	for links in rings:
		for link in links:
			link_map.setdefault(link, set(links)).update(links)

	for i in range(1, len(link_map)):
		for destroy_ring in itertools.combinations(link_map.keys(), i):
			destoryed = set(destroy_ring)
			count = 0
			for link in link_map.items():
				if link[0] not in destoryed:
					count += len(link[1] - destoryed) - 1
			if count == 0:
				return i


if __name__ == '__main__':
	# These "asserts" using only for self-checking and not necessary for auto-testing
	assert break_rings(({1, 2}, {2, 3}, {3, 4}, {4, 5}, {5, 6}, {4, 6})) == 3, "example"
	assert break_rings(({1, 2}, {1, 3}, {1, 4}, {2, 3}, {2, 4}, {3, 4})) == 3, "All to all"
	assert break_rings(({5, 6}, {4, 5}, {3, 4}, {3, 2}, {2, 1}, {1, 6})) == 3, "Chain"
	assert break_rings(({8, 9}, {1, 9}, {1, 2}, {2, 3}, {3, 4}, {4, 5}, {5, 6}, {6, 7}, {8, 7})) == 5, "Long chain"
	assert break_rings([[1,3],[3,4],[3,5],[4,6],[6,7],[8,3],[8,1],[2,6],[8,4],[9,5],[4,5],[1,7]]) == 5
	assert break_rings([[1,9],[1,2],[8,5],[4,6],[5,6],[8,1],[3,4],[2,6],[9,6],[8,4],[8,3],[5,7],[9,7],[2,3],[1,7]]) == 5
	assert break_rings([[3,4],[5,6],[2,7],[1,5],[2,6],[8,4],[1,7],[4,5],[9,5],[2,3],[8,2],[2,4],[9,6],[5,7],[3,6],[1,3]]) == 5
