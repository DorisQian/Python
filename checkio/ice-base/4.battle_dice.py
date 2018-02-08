'''
For this task, you need to figure out what your probability of winning a board game is. The game involves two players moving units around a map. When the units battle and both players roll several dice, one for each unit, to see who wins and at what cost. You want to find the probability of winning one of these battles, regardless of any losses. Keep in mind that if the battle ends with no units remaining on either side, that's a draw, not a win.

When a conflict begins, each player rolls one die per unit. Each die has a number of attack icons and defense icons on each side. After a roll, the player loses a number of units equal to the number of attack icons the opponent rolled minus the number of defense icons they rolled themselves. For example, if player one rolled 2 attack icons and 4 defense icons and player two rolled 3 attack icons and 1 defense icons, player one would lose 0 units (3 - 4 but you can't lose negative units) and player two would lose 1 unit (2 - 1).

After unit losses are applied, the players roll again. This continues until one player has no units remaining.

You are given a description of the dice as a list of which icons are on a face and how many dice each player has. All of the dice are exactly the same. Each element in the list is a string containing zero or more A's representing the attack icons and zero or more D's representing the defense icons. (A face can be blank.) For example, the list ["AAD", "ADD", "A", "D", "", ""] represents a six sided die with two attack and one defense on one face, one attack and two defense on another, a single attack on the third face, a single defense on the fourth and two blank faces.

You should calculate the probability that player one will win the conflict. If player one has a 1 in 7 chance of winning, you should return ≈0.1429. The result should be given with four digits precision as ±0.0001.

Input: Three arguments. A dice description as a list of strings. A number of units for player one and player two as integers.

Output: The probability that player one will win the conflict as a float or integer.

Example:

battle_probability(['A', 'D'], 3, 3) == 0.0000 # It's not immediately obvious, but each player will always lose the same number of units
battle_probability(['A', 'D'], 4, 3) == 1.0000
battle_probability(['AA', 'A', 'D', 'DD'], 3, 4) == 0.0186
battle_probability(['AA', 'A', 'D', 'DD'], 4, 4) == 0.4079
battle_probability(['AA', 'A', 'D', 'DD'], 5, 4) == 0.9073

How it is used: Such multi-step probability calculations are a staple of both programming contests and probability textbooks.

Preconditions:
1 ≤ units_one ≤ 10
1 ≤ units_two ≤ 10
2 ≤ len(dice_description) ≤ 10
There is at least 1 attack icon on the die
There are at most 3 icons on each face

对于这个任务，你需要弄清楚你赢得棋盘游戏的可能性是什么。游戏涉及两名玩家在地图周围移动单位。当单位战斗和双方球员滚动几个骰子，每个单位一个，看看谁赢了，花了多少钱。你想找到赢得其中一场战斗的概率，不管有没有损失。请记住，如果战斗结束，任何一方都没有剩余单位，那么这是一场平局，而不是一场胜利。

当冲突开始时，每个玩家每个单位掷出一个死亡。每个骰子在每边都有许多攻击图标和防御图标。在一次掷骰后，玩家失去的数量等于对手掷出的攻击图标的数量减去他们自己掷出的防御图标的数量。例如，如果玩家掷出2个攻击图标和4个防御图标，玩家2掷出3个攻击图标和1个防御图标，玩家将失去0个单位（3 - 4，但不能失去负面单位），玩家2会失去1个单位（2 - 1）。

单位损失后，球员再次滚动。这一直持续到一个玩家没有剩余单位。

给你一个骰子的描述，列出一张脸上有哪些图标，每个玩家有多少个骰子。所有的骰子都是一样的。列表中的每个元素都是一个包含零个或多个A的字符串，代表攻击图标，零个或多个D代表防御图标。 （例如，一张脸可以是空白的）例如，列表[“AAD”，“ADD”，“A”，“D”，“”，“”]代表一个六面骰子，一面有两个攻击和一个防守一次攻击两次防守，三次面对单一攻击，四次空白面对一次防守。

你应该计算玩家将赢得冲突的概率。如果玩家有七分之一的获胜机会，则应该返回≈0.1429。结果应该以±0.0001的四位精度给出。

输入：三个参数。作为字符串列表的骰子描述。玩家一和玩家二的单位数量是整数。
输出：玩家将以浮点或整数形式赢得冲突的概率。


如何使用：这种多步概率计算是编程竞赛和概率教科书的主要内容。

前提条件：
骰子上至少有一个攻击图标
每个脸上至多有3个图标
'''

def battle_probability(dice_description, units_one, units_two):
    return 0.0

if __name__ == '__main__':
    #These are only used for self-checking and are not necessary for auto-testing
    def almost_equal(checked, correct, significant_digits=4):
        precision = 0.1 ** significant_digits
        return correct - precision < checked < correct + precision

    assert(almost_equal(battle_probability(['A', 'D'], 3, 3), 0.0000)), "Always ties, nobody wins"
    assert(almost_equal(battle_probability(['A', 'D'], 4, 3), 1.0000)), "Always win"
    assert(almost_equal(battle_probability(['AA', 'A', 'D', 'DD'], 3, 4), 0.0186)), "You can win"
    assert(almost_equal(battle_probability(['AA', 'A', 'D', 'DD'], 4, 4), 0.4079)), "Ready to fight"
    assert(almost_equal(battle_probability(['AA', 'A', 'D', 'DD'], 5, 4), 0.9073)), "I have good chance"
