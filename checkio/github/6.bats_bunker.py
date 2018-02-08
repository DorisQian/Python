'''
While searching for an adventure on the island, our robotic trio found a creepy old bunker. In the bunker, someone has hidden a rare and powerful computer chip which the robots hope to install on their spaceship. Our adventurous heroes have tried to search for this chip, but the bunker is occupied by robo-bats and the Alpha Bat appears to be in possession of the chip. In order to obtain the chip, the robots must capture Alpha Bat. This is no easy feat though; the bunker is filled with bat scouts which will alert the others if they spot intruders. If we want to catch the Alpha Bat, we will need to know the amount of time it takes for the alert sent by the scout near the entrance to reach the Alpha Bat.

We have the advantage that the bunker's walls do not reflect sound, so the alert signals can extend only in a straight line. The time it takes an alert to move between two bats is proportional to the Euclidean distance between cell centers (see the illustration). The time for the alert to travel between neighbouring cells is 1 second. Alert "lines" cannot pass through walls or around corners.

You are given the map of bunker as a list of strings:
"-" is an empty cell
"W" is a wall
"B" is a bat 
"A" is the Alpha Bat 
The entrance is placed at top left cell and there's always a bat right there (be careful, the Alpha bat can be here too).

You should calculate the minimal possible time for the alert to reach the leader with a precision of two digits (±0.01).

bats-bunker
Input: A map of the bunker as a list of strings.

Output: The minimal possible time with a precision of two digits as a float.

Example:

checkio([
    "B--",
    "---",
    "--A"]) == 2.83
checkio([
    "B-B",
    "BW-",
    "-BA"]) == 4
checkio([
    "BWB--B",
    "-W-WW-",
    "B-BWAB"]) == 12
checkio([
    "B---B-",
    "-WWW-B",
    "-WA--B",
    "-W-B--",
    "-WWW-B",
    "B-BWB-"]) == 9.24

How it is used: This task is a tricky search problem. It teaches you how to build a graph and determine the line of visibility for the Bats. These concepts can help develop security in the form of CCTV placement, process lighting and even add search and discover algorithms to in game AI.

Precondition:
3 ≤ len(bunker) ≤ 7
all(3 ≤ len(row) ≤ 7 and len(row) == len(bunker[0]) for row in bunker)
bunker[0][0] == "B" or bunker[0][0] == "A"
The Alpha bat can be only one. 
Path from left corner to Alpha Bet always exists.

当我们在岛上寻找冒险的时候，我们的机器人三重奏发现了一个令人毛骨悚然的旧地堡。在掩体中，有人藏有一个机器人希望在他们的飞船上安装的稀有而强大的计算机芯片。我们的冒险英雄已经试图寻找这个芯片，但地堡被机器人蝙蝠占领，阿尔法蝙蝠似乎拥有的芯片。为了获得芯片，机器人必须捕获阿尔法蝙蝠。虽然这不是容易的事，碉堡里充满了蝙蝠侦察兵，如果他们发现了入侵者，他们会提醒其他人。如果我们想要抓住阿尔法蝙蝠，我们需要知道入口附近的侦察兵发出的警报到达阿尔法蝙蝠的时间。

我们的优势在于地堡的墙壁不会反射声音，所以警报信号只能以一条直线延伸。警报在两个蝙蝠之间移动的时间与细胞中心之间的欧几里得距离成正比（见插图）。警报在相邻小区之间传播的时间为1秒。警报“线”不能通过墙壁或角落。

你将地堡的地图作为字符串列表：
“ - ”是一个空单元格
“W”是一堵墙
“B”是一只蝙蝠
“A”是阿尔法蝙蝠
入口放置在左上方，那里总是有一只蝙蝠（小心，阿尔法蝙蝠也可以在这里）。

您应该计算警报以两位数（±0.01）的精度到达领导的最小可能时间。

蝙蝠，沙坑
输入：地堡的地图作为字符串列表。
输出：以两位数的精度作为浮点的最小可能时间。

如何使用：这个任务是一个棘手的搜索问题。它教你如何建立一个图形并确定蝙蝠的可视性。这些概念可以帮助开发CCTV安置，工艺照明，甚至在游戏AI中增加搜索和发现算法。

前提：
阿尔法蝙蝠可能只有一个。
从左角到Alpha Bet的路径始终存在。
'''


def checkio(bunker):
    return 0

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    def almost_equal(checked, correct, significant_digits=2):
        precision = 0.1 ** significant_digits
        return correct - precision < checked < correct + precision

    assert almost_equal(checkio([
        "B--",
        "---",
        "--A"]), 2.83), "1st example"
    assert almost_equal(checkio([
        "B-B",
        "BW-",
        "-BA"]), 4), "2nd example"
    assert almost_equal(checkio([
        "BWB--B",
        "-W-WW-",
        "B-BWAB"]), 12), "3rd example"
    assert almost_equal(checkio([
        "B---B-",
        "-WWW-B",
        "-WA--B",
        "-W-B--",
        "-WWW-B",
        "B-BWB-"]), 9.24), "4th example"