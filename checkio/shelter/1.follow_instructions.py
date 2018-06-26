'''
You’ve received a letter from a friend whom you haven't seen or heard from for a while. 
In this letter he gives you instructions on how to find a hidden treasure.

In this mission you should follow a given list of instructions which will get you to a certain 
point on the map. A list of instructions is a string, each letter of this string points you in 
the direction of your next step.

The letter "f" - tells you to move forward, "b" - backward, "l" - left, and "r" - right.

It means that if the list of your instructions is "fflff" then you should move forward two times, 
make one step to the left and then again move two times forward.

Now, let's imagine that you are in the position (0,0). If you move forward your position will change 
to (0, 1). If you move again it will be (0, 2). If your next step is to the left then your position 
will become (-1, 2). After the next two steps forward your coordinates will be (-1, 4)

Your goal is to find your final coordinates. Like in our case they are (-1, 4)

Input: A string.

Output: A tuple (or list) of two ints

Example:

follow("fflff") == (-1, 4)
follow("ffrff") == (1, 4)
follow("fblr") == (0, 0)

How it is used: In games with a map

Precondition: only chars f,b,l and r are allowed

你收到了一段你从未见过或听到过的朋友的一封信。
在这封信中，他给你指示如何找到隐藏的宝藏。

在这个任务中，你应该遵循给定的指令列表，这将使你得到一定的帮助
点在地图上。指令列表是一个字符串，该字符串的每个字母都指向您
你下一步的方向。

字母“f” - 告诉你前进，“b” - 向后，“l” - 向左，“r” - 向右。

这意味着如果你的指示清单是“fflff”，那么你应该前进两次，
向左一步，然后再向前两步。

现在，让我们假设你处于位置（0,0）。如果你前进，你的位置将会改变
到（0,1）。如果你再次移动它将是（0，2）。如果你的下一步是在左边，那么你的位置
将变成（-1,2）。在接下来的两个步骤之后，你的坐标将是（-1,4）

你的目标是找到你的最终坐标。就像我们的情况一样，它们是（-1,4）

输入：一个字符串。

输出：两个整数的元组（或列表）


它是如何使用的：在带有地图的游戏中

先决条件：只允许字符f，b，l和r
'''

def follow(instructions):
	result = [0, 0]
	for i in instructions:
		if i == 'f':
			result[1] += 1
		elif i == 'b':
			result[1] -= 1
		elif i == 'l':
			result[0] -= 1
		else:
			result[0] += 1
	return tuple(result)


if __name__ == '__main__':
    print("Example:")
    print(follow("fflff"))
    
    # These "asserts" are used for self-checking and not for an auto-testing
    assert follow("fflff") == (-1, 4)
    assert follow("ffrff") == (1, 4)
    assert follow("fblr") == (0, 0)
    print("Coding complete? Click 'Check' to earn cool rewards!")
