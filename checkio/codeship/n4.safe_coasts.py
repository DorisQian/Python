'''
You are given a regional map as an array with strings, which is represented as 2D array. Water cells are marked as "." and land cells as "X". Cells where the Ghost Ship can appear are marked with a ""D". You should finish the map and mark (replace the relevant water cells) all of the safe cells with an "S" and the dangerous ones as "D" (cells the Ghost Ship can reach).

The Ghost Ship can move to neighbour cells at in the cardinal directions - up, down, left, and right. It cannot move to cells which are placed next to land including cells at the diagonals. So, the safe cells are cells where Flying Dutchman cannot approach from all possible directions.

safe-coast

("D..XX.....",        ("DDSXXSDDDD",
 "...X......",         "DDSXSSSSSD",
 ".......X..",         "DDSSSSSXSD",
 ".......X..",         "DDSSSSSXSD",
 "...X...X..",  ===\   "DDSXSSSXSD",
 "...XXXXX..",  ===/   "SSSXXXXXSD",
 "X.........",         "XSSSSSSSSD",
 "..X.......",         "SSXSDDDDDD",
 "..........",         "DSSSSSDDDD",
 "D...X....D")         "DDDSXSDDDD")

    
Input: A regional map as a tuple of strings.

Output: The finished map as a list/tuple of strings.

Example:

finish_map(("D..XX.....",
            "...X......",
            ".......X..",
            ".......X..",
            "...X...X..",
            "...XXXXX..",
            "X.........",
            "..X.......",
            "..........",
            "D...X....D"))) == ["DDSXXSDDDD",
                                "DDSXSSSSSD",
                                "DDSSSSSXSD",
                                "DDSSSSSXSD",
                                "DDSXSSSXSD",
                                "SSSXXXXXSD",
                                "XSSSSSSSSD",
                                "SSXSDDDDDD",
                                "DSSSSSDDDD",
                                "DDDSXSDDDD"]  # or tuple
    
How it is used: This concept can be used to model the placement of defensive structures in strategy games, or model more real-life things such as how an invasive species would react to an inhibiting agent such as ant traps, or weed killer.

Precondition:
3 ≤ len(regional_map) ≤ 10
all(3 ≤ len(row) ≤ 10 and len(row) == len(regional_map[0]) for row in regional_map)
any("D" in row for row in regional_map)


给你一个区域地图作为一个带有字符串的数组，用2D数组表示。 水细胞标记为“。”。 和地面细胞为“X”。 您应该完成地图并标记（替换相关水细胞）所有安全细胞为“S”，危险细胞为“D”（细胞） 鬼船可以到达）。

幽灵船可以向上，向下，向左和向右移动到基本方向的邻居小区。 它不能移动到靠近地面的细胞，包括细胞在对角线上。 所以，安全的细胞就是Flying Dutchman无法从所有可能的方向接近的细胞。

安全海岸


输入：区域地图作为字符串的元组。

输出：完成的地图作为字符串的列表/元组。

它是如何使用的：这个概念可以用来模拟策略游戏中防御结构的位置，或者模拟更真实的事物，比如入侵物种如何对抑制剂（如蚂蚁陷阱或除草剂）作出反应。
'''