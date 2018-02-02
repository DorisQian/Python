'''
You have a Domino box. Domino tiles contain two numbers from 0 (empty) to 6. 
Tiles are unordered and 1-6 is the same as 6-1. The double-six set contains 
28 unique tiles - all combinations of number pairs.

Several tiles fell out of the box. You should try to line up a chain from 
these tiles, compiling them to each other's suitable sides (sides with the 
same numbers). Thus, you can get a continuous chain of tiles. In some cases, 
such a chain will not be the only one.

For example, you've ended up these tiles:
1-5, 2-5, 3-5, 4-5, 3-4
So, with them you can build two complete chains:
1-5, 5-3, 3-4, 4-5, 5-2
1-5, 5-4, 4-3, 3-5, 5-2
Your goal in this mission is to count how many complete chains you can make 
using all of the given dominoes.

Note. Chains must be unique. An inverted chain is not considered as unique: 
"1-2, 2-3, 3-4, 4-5" and "5-4, 4-3, 3-2, 2-1" are the same chain.

Input: String with the description of the domino tiles. Like this one: "5-4, 4-3, 3-2, 2-1".

Output: Integer. The maximum number of complete chains that you can build 
using all of the given tiles.

Examples:

domino_chain("0-2, 0-5, 1-5, 1-3, 5-5") == 1
domino_chain("1-5, 2-5, 3-5, 4-5, 3-4") == 2
domino_chain("0-5, 1-5, 2-5, 3-5, 4-5, 3-4") == 0

How it is used: This is a combinatorial problem. You can solve it by modeling 
a real game of dominoes. Or refreshing your knowledge of graph theory. Many 
things in life resemble the process of forming a domino chain: for example, 
flights between several cities.

Precondition: 5 <= len(given_tiles) <= 17

你有一个Domino框。多米诺骨牌瓷砖包含从0（空）到6的两个数字。
瓷砖是无序的，1-6和6-1是一样的。双六组包含
28个独特的瓷砖 - 数字对的所有组合。

几个瓷砖从箱子里掉出来。你应该尝试排队从一个链
这些瓷砖，编译到对方的适当的一面（两侧与
相同的数字）。因此，你可以得到连续的瓷砖链。在某些情况下，
这样的链条不会是唯一的。

例如，你已经结束了这些瓷砖：
1-5，2-5,3-5,4-5,3-4
所以，他们可以建立两个完整的链条：
1-5，5-3，3-4，4-5，5-2
1-5，5-4，4-3，3-5，5-2
你在这个任务中的目标是统计你可以制造多少个完整的链条
使用所有给定的多米诺骨牌。

注意。链必须是唯一的。倒链不被认为是唯一的：
“1-2,2-3,3-4,4-5”和“5-4,4-3,3-2,2-1”是相同的链。

输入：字符串与多米诺骨牌瓷砖的描述。像这样：“5-4,4-3,3-2,2-1”。

输出：整数。您可以构建的完整链的最大数量
使用所有给定的瓷砖。

如何使用：这是一个组合问题。你可以通过建模一个真正的多米诺骨牌游戏来解决它。
或刷新你的图论的知识。生活中的许多事情类似于形成多米诺骨牌链的过程：例如，几个城市之间的航班。
'''