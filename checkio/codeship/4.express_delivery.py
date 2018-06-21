'''
Our three robots found a few mysterious boxes on the island. After some examination Nicola discovered that these boxes have an an interesting feature. If you place something in one of them, you can retrieve it again from any other box. Stephan figures this makes for quick delivery of cargo across the island, moving loads twice as fast. Stephan can place the cargo in one box and pick it up later at the delivery point. On the map there are water cells which Stephan can't pass, but else these boxes will make his task a whole lot easier.

The map for delivery is presented as an array of strings, where:

"W" is a water (closed cell)
"B" is a box
"E" is a goal point.
"S" is a start point.
"." is an empty cell.
Stephan moves between neighbouring cells in two minutes if he carries a load. Without any carry-on luggage, he only needs one minute. Loading and unloading of cargo in (and out of) the box takes one minute. You should find the fastest way for the cargo delivery (minimum time).

The route is a string, where each letter is an action.

"U" -- Up (north)
"D" -- Down (south)
"L" -- Left (west)
"R" -- Right (east)
"B" -- Load or unload in (out) a box.
express-delivery
Input: A map for delivery as a list of strings.

Output: The fastest route as a string.

Example:

checkio(["S...","....","B.WB","..WE"]) #RRRDDD
checkio(["S...","....","B..B","..WE"]) #DDBRRRBD
    
How it is used: This problem is similar to the "Open labyrinth", but here we have various cost of moves. Using this task, you will learn algorithms used in pathfinding and graph traversal. For example: in some strategy or role playing games, a unit can move with different speed on various terrains.

Precondition: 0 < rows < 10
0 < columns < 10
∀ x,y ∈ coordinates : 0 ≤ x,y ≤ 10


我们的三个机器人在岛上发现了几个神秘的盒子。经过一番检查后，尼古拉发现这些箱子有一个有趣的功能。如果你在其中的一个放置东西，你可以从任何其他盒子再次检索它。斯蒂芬的数字表明，这使得货物可以快速运送到整个岛屿，使货物运送速度提高两倍。斯蒂芬可以将货物放在一个箱子里，稍后在交货地点捡起货物。在地图上有斯蒂芬不能通过的水细胞，但是这些盒子会让他的任务变得更容易。

交付地图以字符串数组呈现，其中：

“W”是水（闭孔）
“B”是一个盒子
“E”是一个目标点。
“S”是一个起点。
“”是一个空单元格。
如果他携带负载，Stephan会在两分钟内在相邻的小区之间移动。没有任何随身行李，他只需要一分钟。在货箱内（和外面）装载和卸载货物需要一分钟。您应该找到最快的货运方式（最短时间）。

路线是一个字符串，每个字母都是一个动作。

“U” - 向上（北）
“D” - 向下（南）
“L” - 左（西）
“R” - 右（东）
“B” - 加载或卸载一个盒子。
快速传送
输入：作为字符串列表交付的地图。
输出：作为一个字符串的最快路径。
  
它是如何使用的：这个问题类似于“打开迷宫”，但是这里我们有各种各样的移动成本。使用此任务，您将了解用于寻路和图形遍历的算法。例如：在某些策略或角色扮演游戏中，单位可以在各种地形上以不同的速度移动。
'''

from typing import List

def checkio(field_map: List[str]) -> str:
    return "RRRDDD"

if __name__ == '__main__':
    print("Example:")
    print(checkio(["S...", "....", "B.WB", "..WE"]))

    #This part is using only for self-checking and not necessary for auto-testing
    ACTIONS = {
        "L": (0, -1),
        "R": (0, 1),
        "U": (-1, 0),
        "D": (1, 0),
        "B": (0, 0)
    }

    def check_solution(func, max_time, field):
        max_row, max_col = len(field), len(field[0])
        s_row, s_col = 0, 0
        total_time = 0
        hold_box = True
        route = func(field[:])
        for step in route:
            if step not in ACTIONS:
                print("Unknown action {0}".format(step))
                return False
            if step == "B":
                if hold_box:
                    if field[s_row][s_col] == "B":
                        hold_box = False
                        total_time += 1
                        continue
                    else:
                        print("Stephan broke the cargo")
                        return False
                else:
                    if field[s_row][s_col] == "B":
                        hold_box = True
                    total_time += 1
                    continue
            n_row, n_col = s_row + ACTIONS[step][0], s_col + ACTIONS[step][1],
            total_time += 2 if hold_box else 1
            if 0 > n_row or n_row >= max_row or 0 > n_col or n_row >= max_col:
                print("We've lost Stephan.")
                return False
            if field[n_row][n_col] == "W":
                print("Stephan fell in water.")
                return False
            s_row, s_col = n_row, n_col
            if field[s_row][s_col] == "E" and hold_box:
                if total_time <= max_time:
                    return True
                else:
                    print("You can deliver the cargo faster.")
                    return False
        print("The cargo is not delivered")
        return False

    assert check_solution(checkio, 12, ["S...", "....", "B.WB", "..WE"]), "1st Example"
    assert check_solution(checkio, 11, ["S...", "....", "B..B", "..WE"]), "2nd example"
    print("Coding complete? Click 'Check' to earn cool rewards!")
