'''
For this task, you're going to play a dice game, but first you must prepare for an 
overwhelming victory. The game itself is very simple. Both players roll a single 
die and whoever rolls highest scores a point. (On a tie, both players must reroll 
until someone scores.)

These aren't standard dice however. Each player can put any positive number on any 
side of the die as long as the number of sides match and the total of all the chosen 
numbers are the same. For example, one player might use a six sided die with the 
numbers [3, 3, 3, 3, 6, 6] while the other player uses a six sided die with the 
numbers [4, 4, 4, 4, 4, 4]. The interesting part of this game is that even with 
the same number of sides and the same total, different dice have different chances 
of winning. Using the example die, the player with all 4's will win 2/3 of the time.

To prepare for this game, you're investigating different ways of picking the numbers. 
To do this, write a program that will take an opponent's die and output some die which 
will win against it more than half the time. If no die satisfies the task requirements, 
return an empty list.

Input: An enemy's die as a sorted list of integers, one for each face of the opponent's die.

Output: Your die as a list of integers, one for each face of your die or an empty list.

Example:

winning_die([3, 3, 3, 3, 6, 6]) == [4, 4, 4, 4, 4, 4] # Or [3, 3, 4, 4, 5, 5]
winning_die([4, 4, 4, 4, 4, 4]) == [2, 2, 5, 5, 5, 5] # Or [5, 5, 2, 2, 5, 5]
winning_die([2, 2, 5, 5, 5, 5]) == [3, 3, 3, 3, 6, 6]
winning_die([1, 1, 3]) == [1, 2, 2]
winning_die([1, 2, 3, 4, 5, 6]) == [] # Any 6-sided die totaling 21 has a 50/50 chance of winning against the standard die.
winning_die([2, 3, 4, 5, 6, 7]) == [1, 1, 3, 7, 7, 8] # This can be beat though.
winning_die([1, 2, 3, 4, 5, 6]) == []

How it is used: This task illustrates some of the unintuitive results in probability. 
Many people would think that two dice as similar as the ones in the description above 
(same number of sides, same average roll) would have a roughly 50/50 chance against each 
other. Even more unusual is that sets of dice can be created where die A beats die B, 
die B beats die C and yet die C beats die A (e.g. the first three examples above). 
These are called nontransitive dice.

Preconditions:
3 ≤ len(die) ≤ 10
sum(die) ≤ 100
min(die) ≥ 1
max(die) ≤ 18

对于这个任务，你要玩一个骰子游戏，但首先你必须准备一个
压倒性的胜利。游戏本身很简单。双方球员都单打
死亡和谁得分最高的一个人。 （在平局上，双方都必须重掷
直到有人得分。）

这些不是标准的骰子。每个玩家可以放任何正数
只要边的数量和所有选择的总数相匹配
数字是一样的。例如，一个玩家可能会使用六面骰子
数字[3，3，3，6，6]，而其他玩家使用六面模具
数字[4，4，4，4，4]。这个游戏有趣的部分是，即使与
同样数量的边和相同的总数，不同的骰子有不同的机会
的胜利。以这个例子来说，所有4的玩家将赢得三分之二的时间。

为了准备这个游戏，你正在调查不同的方式选择数字。
要做到这一点，写一个程序，将采取对手的死亡，并输出一些死亡
将在一半以上的时间内赢得胜利。如果没有死亡符合任务要求，
返回一个空的列表。

输入：敌人的死亡，作为整数的排序列表，对于对手死亡的每个面孔。
输出：你的死亡是一个整数列表，一个死亡的每个面或一个空列表。

如何使用：这个任务说明了一些概率上的不直观的结果。
许多人会认为这两个骰子与上面描述的那些相似
（同样数量的边数，相同的平均数）对每个数据大概有50/50的机会
其他。 更为不寻常的是，一组骰子可以在A击败B的地方创建，
die B击败了die C，但仍然击败了die A（例如上面的前三个例子）。
这些被称为不灵敏的骰子。
'''

import itertools
def probility(enemy_die, ans):
    s = 0
    for i in ans:
        ss = 0
        for j in enemy_die:
            if i > j:
                ss += 1
            elif i < j:
                ss -= 1
        s += ss
    return s

def winning_die(enemy_die):
    total = sum(enemy_die)
    number = len(enemy_die)
    m = max(enemy_die)
    for i in itertools.combinations_with_replacement(range(1, 18), number):
        if sum(i) == total:
            if probility(enemy_die,i) > 0:
                return i
    return []
    

if __name__ == '__main__':
    #These are only used for self-checking and not necessary for auto-testing
    def check_solution(func, enemy):
        player = func(enemy)
        total = 0
        for p in player:
            for e in enemy:
                if p > e:
                    total += 1
                elif p < e:
                    total -= 1
        return total > 0

    assert check_solution(winning_die, [3, 3, 3, 3, 6, 6]), "Threes and Sixes"
    assert check_solution(winning_die, [4, 4, 4, 4, 4, 4]), "All Fours"
    assert check_solution(winning_die, [1, 1, 1, 4]), "Unities and Four"
    assert winning_die([1, 2, 3, 4, 5, 6]) == [], "All in row -- No die"
