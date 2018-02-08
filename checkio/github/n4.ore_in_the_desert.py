'''
During their adventure, the Robo-trio came across a desert, and the ships sensors have registered ore in the region. The desert has a size of 10x10 cells and can be represented as a 2D array. The ship has four probes which can be used to help us find the ore. At each step you will need to return the coordinates of a cell (as [row, column]) for the probe to travel to. If the cell contains ore, then you can finish; else the probe will give a distance to the location of the ore cell (it will be the Euclidean distance between cells' centers). The perception of probe is not very good and it will give you a result rounded to the closest integer (1.41 ≈ 1; 2.83 ≈ 3). At each step you receive information from the previous probes as a list of list. Each list will be in the following format: [row, column, distance]. At the beginning of the mission, you will only receive an empty list.

ore-in-the-desert
Input: Information of the previous probes as a list of lists. Each list contains three integers.

Output: The coordinate of the next probe as a list of two integers.

Example:

checkio([])
checkio([[5, 3, 4]])
checkio([[5, 3, 4], [2, 9, 3]])

How it is used: This task illustrates trilateration. Trilateration is the process of determining absolute or relative locations of points by measurement of distances, using the geometry of circles, spheres or triangles. In addition to being an interesting geometric problem, trilateration does have practical applications in surveying and navigation and is an important part of the equations making global positioning systems (GPS) possible.

Precondition: 
len(desert) == 10
all(len(row) == 10 for row in desert)
There is always exist an ore cell in the desert.

在他们的冒险期间，机器人三人遇到了沙漠，船上的传感器在该地区注册了矿石。沙漠的大小为10x10个单元格，可以表示为二维数组。船上有四个探针可以帮助我们找到矿石。在每一步中，您将需要返回一个单元格的坐标（如[行，列]），以便探针前往。如果细胞含有矿石，那么你可以完成;否则探测器会给矿石单元的位置（这将是单元格中心之间的欧几里得距离）。探针的感觉不是很好，它会给你一个四舍五入到最接近的整数（1.41≈1; 2.83≈3）的结果。在每个步骤中，您都会从列表中获取以前探测器的信息。每个列表将采用以下格式：[行，列，距离]。在任务开始时，您只会收到一个空的列表。

矿在-的沙漠
输入：以前的探测器的信息作为列表的列表。每个列表包含三个整数。
输出：将下一个探测器的坐标作为两个整数的列表。

如何使用：这个任务说明了三边测量。三角测量是通过测量距离来确定点的绝对或相对位置的过程，使用圆形，球形或三角形的几何形状。三角测量除了是一个有趣的几何问题之外，在测量和导航领域也有实际应用，是全球定位系统（GPS）方程的重要组成部分。
'''
