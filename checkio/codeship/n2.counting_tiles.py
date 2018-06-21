'''
Stephan needs some help building a circular landing zone using the ice square tiles for their new Ice Base. Before he converts the area to a construction place, Stephan needs to figure out how many square tiles he will need.

Each square tile has size of 1x1 meters. You need to calculate how many whole and partial tiles are needed for a circle with a radius of N meters. The center of the circle will be at the intersection of four tiles. For example: a circle with a radius of 2 metres requires 4 whole tiles and 12 partial tiles.


Input: The radius of a circle as a float

Output: The quantities whole and partial tiles as a list with two integers -- [solid, partial].

Example:
checkio(2) == [4, 12]
checkio(3) == [16, 20]
checkio(2.1) == [4, 20]
checkio(2.5) == [12, 20]
How it is used: This task is a simple geometry problem; but you can use it for architecture and topography. As we see in the description, you can calculate the amount of materials needed for a project.

Precondition:
0 < radius ≤ 4

斯蒂芬需要一些帮助建立一个圆形着陆区，使用他们新的冰基的冰块。 在他将该地区改建为施工场所之前，斯蒂芬需要弄清楚他需要多少块方形瓷砖。

每块方形瓷砖的尺寸为1x1米。 您需要计算半径为N米的圆需要多少个完整和部分贴图。 圆的中心将位于四个瓷砖的交点处。 例如：半径为2米的圆需要4块全瓷砖和12块部分瓷砖。


输入：作为浮点的圆的半径

输出：将整个和部分图块的数量作为具有两个整数的列表 - [solid，partial]。

它是如何使用的：这个任务是一个简单的几何问题; 但您可以将其用于建筑和地形。 正如我们在描述中看到的那样，您可以计算项目所需的材料数量。
'''