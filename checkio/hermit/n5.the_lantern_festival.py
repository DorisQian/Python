'''
Tōrō nagashi (灯籠流し) is a Japanese ceremony in which participants float paper lanterns (chōchin) down a river. The word tōrō is Japanese for lantern, while nagashi means "to cruise" or "flow". This is primarily done on the last evening of the Bon Festival, a festival based on the belief that these lanterns would guide the spirits back to the world of the dead.

Our robots are going to float their own illuminated lanterns down a river and watch how they flow down the river. Rivers in RoboLand generally have flat banks, sharp right angle turns and a consistent width throughout the length of the river.

Each Robot simultaneously put their lantern in a row spanning the entire width of the river. Each lantern floats with a constant speed of 1 cell/minute. The river has several streams and each lantern will float in its own stream without moving into any of the other streams. The image below illustrates how streams flow in the river.

river-schema

The river flows from the northern to the southern edge. It is not intersected by nor does it merge with another river, or a branch of itself. Because the river has the same width, streams do not intersect each other. The river always has banks and does not end or touch west or east edge of the map.

The Robots place their lanterns on the northern edge of river. This moment occurrs at the 0th minute. The number of lanterns is equal to the width of the river (in cells). Each lantern lights all the neighbouring cells, including the diagonals cells. You should model how the lanterns flow down the river and determine how many water cells will be lit a a time interval of X minutes.

You are given a map detailing a section of the river as a sequence of strings which forms a matrix. Water cells are marked as ".", land cells - "X". In addition, you are given a specified time as a number of minutes from when the lanterns are placed. Count how many water cells will are lit at that given time. If a cell is lit by two lanterns at the same time, then count it only once. Don't forget count cells where the lanterns are located.

lantern-examples
Input: Two arguments. A map of river as a tuple of strings and time as an integer.

Output: The number of lightened water cells as an integer.

Example:

lanterns_flow(("X....XXX",
               "X....XXX",
               "X....XXX",
               "X....XXX",
               "X....XXX",
               "X......X",
               "X......X",
               "X......X",
               "X......X",
               "XXX....X"), 0) == 8
    
How it is used: Here we will examine a complex model of parallel motion. This concept can be used to model the flow of a production line in a factory, or racecars over the course of a race track.

Precondition:
0 < len(river_map) < 20
The river has the same width in cells.
"time" is given for cases when all lanterns on the map.
'''