'''
Nicola likes to categorize all sorts of things. He categorized a series of numbers 
and as the result of his efforts, a simple sequence of numbers became a deeply-nested 
list. Sophia and Stephan don't really understand his organization and need to figure 
out what it all means. They need your help to understand Nikolas crazy list.

There is a list which contains integers or other nested lists which may contain yet 
more lists and integers which then… you get the idea. You should put all of the 
integer values into one flat list. The order should be as it was in the original 
list with string representation from left to right.

We need to hide this program from Nikola by keeping it small and easy to hide. 
Because of this, your code should be shorter than 140 characters (with whitespaces).

Input data: A nested list with integers.

Output data: The one-dimensional list with integers.

Example:

flat_list([1, 2, 3]) == [1, 2, 3]
flat_list([1, [2, 2, 2], 4]) == [1, 2, 2, 2, 4]
flat_list([[[2]], [4, [5, 6, [6], 6, 6, 6], 7]]) == [2, 4, 5, 6, 6, 6, 6, 6, 7]
flat_list([-1, [1, [-2], 1], -1]) == [-1, 1, -2, 1, -1]

How it is used: This concept is useful for parsing and analyzing files 
with complex structures and the task challenges your creativity in writing short code.

Precondition: 0 ≤ |array| ≤ 100
∀ x ∈ array : -232 < x < 232 or x is a list
depth < 10

尼古拉喜欢分类各种各样的东西。 他分类了一系列数字
作为他努力的结果，一串简单的数字变成了一个深深的嵌套名单。 索菲亚（Sophia）和斯蒂芬（Stephan）并不真正了解他的组织，需要指出
这是什么意思。 他们需要你的帮助来理解尼古拉斯疯狂的名单。

有一个包含整数或其他可能包含的嵌套列表的列表更多的列表和整数，然后...你明白了。 你应该把所有的
整数值放入一个平面列表中。 顺序应该和原来一样列表中的字符串表示从左到右。

我们需要把这个程序从尼古拉隐藏起来，保持它小而易于隐藏。因此，您的代码应该少于140个字符（使用空格）。

输入数据：带整数的嵌套列表。
输出数据：带整数的一维列表。

如何使用：这个概念对解析和分析文件很有用
结构复杂，任务挑战写短代码的创造力。
'''

def flat_list(array):
    r = []
    def relist(array):
    	for i in array:
    		if type(i) is not int:
    			relist(i)
    		else:
    			r.append(i)
    relist(array)
    return r


if __name__ == '__main__':
    assert flat_list([1, 2, 3]) == [1, 2, 3], "First"
    assert flat_list([1, [2, 2, 2], 4]) == [1, 2, 2, 2, 4], "Second"
    assert flat_list([[[2]], [4, [5, 6, [6], 6, 6, 6], 7]]) == [2, 4, 5, 6, 6, 6, 6, 6, 7], "Third"
    assert flat_list([-1, [1, [-2], 1], -1]) == [-1, 1, -2, 1, -1], "Four"
    print('Done! Check it')