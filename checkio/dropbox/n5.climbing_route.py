'''
You have an elevation map and you want to know the shortest climbing route.

The map is given as a list of strings.

0 : plain ( elevation is 0)
1-9 : hill (number is elevation)
"mountain" is adjacent (only 4 directions) hill group.

It consists of two or more hills.
Isolated hill is not mountain.
Start is top-left. Goal is bottom-right. You have to go over all the mountaintops. 
You can only move vertical and horizontal. And you can only move to the same or one elevation 
difference. You should look for the shortest route and return Number of steps. (if mountains 
do not exist, You may go to the goal at the shortest from the start.)

example

Input: A elevation map as a list of strings.

Output: number of steps as Integer.

Example:

climbingRoute(['000',
               '120',
               '000']) == 6

climbingRoute(['000000002110',
               '011100002310',
               '012100002220',
               '011100000000']) == 26

How it is used: Geographic analysis, Game map design and so on.

Precondition:
elevation_map[0][0] == elevation_map[-1][-1] == '0'
3 ≤ len(elevation_map)
all(3 ≤ len(row) and len(row) == len(elevation_map[0]) for row in elevation__map)
Each mountain has only one mountaintop.
There is no mountain that can not climb.

你有一张海拔地图，你想知道最短的攀登路线。

该地图以字符串列表形式给出。

0：平原（海拔为0）
1-9：山（数字是海拔）
“山”毗邻（只有4个方向）山群。

它由两个或更多的山丘组成。
孤山不是山。
开始是左上角。目标是右下。你必须经过所有的山顶。
你只能移动垂直和水平。你只能移动到相同或一个标高
区别。您应该查找最短路线并返回步数。 （如果山脉
不存在，你可以从一开始就以最短的时间到达目标。）


输入：作为字符串列表的高程图。
输出：步数为整数。


它如何使用：地理分析，游戏地图设计等等。

前提：
elevation_map [0] [0] == elevation_map [-1] [ - 1] =='0'
3≤len（elevation_map）
在elevation_map中的所有行（3≤len（row）和len（row）== len（elevation_map [0]））
每座山只有一座山顶。
没有不能爬的山。
'''