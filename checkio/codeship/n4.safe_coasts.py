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
'''