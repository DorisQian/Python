'''
To start the game, they put several black and white pearls in one of the boxes. 
Each robots have Nth moves, then initial set are restored for a next player. 
For each move, the robot take a pearl out of the box and put one of the opposite 
color back. The winner is the one who pulls the white pearl on the Nth step 
(or +1 point if they play many parties).

Our robots don't like indeterminacy and want to know the probability of a white 
pearl on the Nth step. The probability is a value between 0 (0% chance or will 
not happen) and 1 (100% chance or will happen). The result is a float from 0 to 
1 with two digits precision (±0.01).

You are given a start set of pearls as a string that contains "b" (black) and "w" 
(white) and the number of the step (N). The order of the pearls does not matter.

probability

Input: The start sequence of the pearls as a string and the step number as an integer.

Output: The probability for a white pearl as a float.

Example:

checkio('bbw', 3) == 0.48
checkio('wwb', 3) == 0.52
checkio('www', 3) == 0.56
checkio('bbbb', 1) == 0
checkio('wwbb', 4) == 0.5
checkio('bwbwbwb', 5) == 0.48

How it is used: This task introduces you to the basics of probability theory and 
statistics. Fun fact: regardless of the initial state, as the number of steps 
increases, the probability approaches 0.5!

Precondition: 0 < N ≤ 20
0 < |pearls| ≤ 20


为了开始游戏，他们在一个盒子里放了几个黑色和白色的珍珠。
每个机器人有N次移动，然后为下一个玩家恢复初始设置。
对于每一个动作，机器人从箱子里拿出一颗珍珠，并把一个相反的
颜色回来。 胜利者是第N步拉白珍珠的人
（如果他们参加很多派对，则为+1点）。

我们的机器人不喜欢不确定性，想知道白色的可能性
第N步的珍珠。 概率是介于0（0％几率或意志）之间的值
不会发生）和1（100％几率或将会发生）。 结果是从0到一个浮点数
1，精度为两位数（±0.01）。

您将获得一组珍珠作为包含“b”（黑色）和“w”的字符串
（白色）和步数（N）。 珍珠的顺序并不重要。

可能性

输入：珍珠的起始序列作为字符串，步骤号码为整数。
输出：白色珍珠作为浮动的概率。

如何使用：这个任务向你介绍了概率论和基础知识
统计。 有趣的是：不管初始状态如何，步数
增加，概率接近0.5！
'''

def probability(w, b, k, p, n):
	if n == 0:
		a.append((w / k) * p)
		# print (a)
		return
	if w > 0:
		probability(w - 1, b + 1, k, p * (w / k), n - 1)
	if b > 0:
		probability(w + 1, b - 1, k, p * (b / k), n - 1)


def checkio(marbles, step):
    global a
    a = []
    w = float(marbles.count('w'))
    b = float(marbles.count('b'))
    k = len(marbles)
    probability(w, b, k, 1.0, step - 1)
    return round(sum(a),2)


#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio('bbw', 3) == 0.48, "1st example"
    assert checkio('wwb', 3) == 0.52, "2nd example"
    assert checkio('www', 3) == 0.56, "3rd example"
    assert checkio('bbbb', 1) == 0, "4th example"
    assert checkio('wwbb', 4) == 0.5, "5th example"
    assert checkio('bwbwbwb', 5) == 0.48, "6th example"