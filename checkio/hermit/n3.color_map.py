'''
In mathematics the four color theorem, or the four color map theorem, states that: when given any separation of a plane into contiguous regions and producing a figure called a map, no more than four colors are required to color the regions of the map so that no two adjacent regions have the same color. Two regions are called adjacent if they share a common boundary that is not a corner, where corners are the points shared by three or more regions. For our model we will use a grid with square cells.

You are given a regional map as a grid (matrix). There are N countries located on this map. Each country has a number from 0 to N-1. Two cells are adjacent if they have a common edge. Each country has one or more cells that are connected. Thus you can move between any cells of the country X just using for this adjacent cells. 
Each cell is marked by the number of its designated country.

You should "color" a map with 4 colors. All of the cells comprising one country should be one color. Adjacent cells of various countries should not have the same color.

The result should be represented as a sequence of numbers 1,2,3 or 4. Each element shows the color of its country matching the index. For example, the 0th element shows the color of country 0. So the result should have N elements.

color-map
Input: A map of region as a tuple of tuples with integers.

Output: The color sequence as a tuple/list of integer.

Example:

color_map(((0, 0, 0), (0, 1, 1), (0, 0, 2)) # [1, 2, 3] or [2, 3, 1] or ...

How it is used: This is a classic constraint satisfaction problem. The four color theorem was proven in 1976 by Kenneth Appel and Wolfgang Haken. It was the first major theorem to be proved using a computer. Appel and Haken's approach started by showing that there is a particular set of 1,936 maps, each of which cannot be part of a smallest-sized counterexample to the four color theorem.

Precondition: 0 < len(region) ≤ 10
all(0 < len(row) ≤ 10 and len(row) == len(region[0]) for row in region)
One country cells are connected.
Country numbers are sequence from 0 to N-1.
'''