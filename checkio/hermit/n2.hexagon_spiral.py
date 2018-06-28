'''
Bees are very well organized insects. Let's suppose that bees have numerical ordering system for their honeycomb. If each cell in the honeycomb is hexagon and the bees want to build an accurate honeycomb then one method the could use to build it is to build in a spiraling pattern. This would mean that the numerical order is also in a spiral. That way each cell has own number and we have navigation system on the honeycomb. For this mission, we will need to account for that information while we define the distance between specific cells.

The map of the honeycomb consists of a collection of hexagonal elements. The first element in the center is marked as 1 and in a continuing clockwise spiral, the rest of the elements are marked in ascending order ad infinitum. On this map, you can "move" through the adjoining edges of the hexagonal elements to place yourself in a neighboring cell.

hex-spiral

For example: the distance between elements 1 and 9 is two moves and the distance between 8 and 18 is two move. Between 17 and 13 - 4 moves.

Input: Pair of numbers that represent 2 elements as integers.

Output: The distance between the 2 elements as an integer.

Example:

hex_spiral(2, 9) == 1
        hex_spiral(9, 2) == 1
        hex_spiral(6, 19) == 2
        hex_spiral(5, 11) == 3

How it is used: Often times, turn based strategy games or role playing games will use a hex grid based map for unit placement allowing for six possible movement directions. This mission will help you to write a simple program which can tell a unit the distance between specific cells. Add a few restrictions for minimum and maximum distance and you could program not only movement range, but also range of attack, area of effect or even range of influence.

Precondition:
all(0 < x < 1000 for x in args)
'''