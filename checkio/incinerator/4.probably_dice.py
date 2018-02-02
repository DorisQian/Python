'''
You're on your way to a board game convention. Chances are there’ll be some stiff 
competition, so you decide to learn more about dice probabilities since you suspect 
you'll be rolling a lot of them soon.

Typically, when using multiple dice, you simply roll them and sum up all the result. 
To get started with your investigation of dice probability, write a function that takes 
the number of dice, the number of sides per die and a target number and returns the 
probability of getting a total roll of exactly the target value. The result should be 
given with four digits precision as ±0.0001. For example, if you roll 2 six-sided dice, 
the probability of getting exactly a 3 is 2/36 or 5.56%, which you should return as ≈0.0556.

distribution
For each test, assume all the dice are the same and are numbered from 1 to the number of 
sides, inclusive. So a 4-sided die (D4) would have an equal chance of rolling a 1, 2, 3 or 
4. A 20-sided die (D20) would have an equal chance of rolling any number from 1 to 20.

Tips: Be careful if you want to use a brute-force solution -- you could have a very, 
very long wait for edge cases.

Input: Three arguments. The number of dice, the number of sides per die and the target number as integers.

Output: The probability of getting exactly target number on a single roll of the given dice as a float.

Example:

probability(2, 6, 3) == 0.0556  # 2 six-sided dice have a 5.56% chance of totalling 3
probability(2, 6, 4) == 0.0833
probability(2, 6, 7) == 0.1667
probability(2, 3, 5) == 0.2222  # 2 three-sided dice have a 22.22% chance of totalling 5
probability(2, 3, 7) == 0       # The maximum you can roll on 2 three-sided dice is 6
probability(3, 6, 7) == 0.0694
probability(10, 10, 50) == 0.0375

How it is used: This task illustrates some of the basics of probability. Many events can 
be described as the combination of other events. In this case you're combining several dice 
into one total to crit the Orc King for massive damage.

Preconditions:
1 ≤ dice_number ≤ 10
2 ≤ sides ≤ 20
0 ≤ target < 1000

你正在去棋盘游戏大会的路上。有可能会有一些僵硬
竞争，所以你决定更多地了解骰子概率，因为你怀疑
你很快就会滚动很多。

通常情况下，当使用多个骰子时，只需将它们滚动并总结所有结果即可。
要开始骰子概率的调查，写一个函数
骰子的数量，每个骰子的数量以及目标数量，并返回
获得正确的目标值总卷的概率。结果应该是
以四位数的精度给出±0.0001。例如，如果您掷出两个六面骰子，
得到一个3的概率是2/36或5.56％，你应该返回≈0.0556。

分配
对于每个测试，假设所有的骰子是相同的，并从1到数字编号
双方，包容性。所以一个四面模具（D4）将有相等的滚动1,2,3或3的机会
4.一个20面的模具（D20）将有相同的机会滚动从1到20的任何数字。

提示：如果你想使用暴力解决方案要小心 - 你可以有一个非常，
很长时间等待边缘情况。

输入：三个参数。骰子的数量，每个骰子的边数和整数的目标数量。

输出：在给定骰子的单个滚动上获得完全目标数字的概率作为浮点数。

如何使用：这个任务说明了一些概率的基础知识。 许多事件可以
被描述为其他事件的组合。 在这种情况下，你正在组合几个骰子
成为一个共同的重大兽人国王的重大损害。
'''

def probability(dice_number, sides, target):
    return 0.0

if __name__ == '__main__':
    #These are only used for self-checking and are not necessary for auto-testing
    def almost_equal(checked, correct, significant_digits=4):
        precision = 0.1 ** significant_digits
        return correct - precision < checked < correct + precision
        
    assert(almost_equal(probability(2, 6, 3), 0.0556)), "Basic example"
    assert(almost_equal(probability(2, 6, 4), 0.0833)), "More points"
    assert(almost_equal(probability(2, 6, 7), 0.1667)), "Maximum for two 6-sided dice"
    assert(almost_equal(probability(2, 3, 5), 0.2222)), "Small dice"
    assert(almost_equal(probability(2, 3, 7), 0.0000)), "Never!"
    assert(almost_equal(probability(3, 6, 7), 0.0694)), "Three dice"
    assert(almost_equal(probability(10, 10, 50), 0.0375)), "Many dice, many sides"
