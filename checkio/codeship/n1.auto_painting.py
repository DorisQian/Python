'''
Nicola has built a semi-automatized painting system, but this system can paint only one side of an item. After that, an operator must reload the machine and paint the other side (the system detects painted sides automatically). The painting process always takes the same amount of time. The camera can paint K surfaces at a time. Nicola wants Stephan to operate the painting machine and he needs to develop an algorithm for Stephan which will allow him to paint N (0 < N ≤ 10) surfaces in the shortest possible timeframe. Be careful that you don't paint the item more than two times.

system
The items are numbered from 0 to 9. You are given the paint holding capacity of the machine (K) and the quantity of items (N). You should return the sequence Stephen must paint as a string, where each action is the numbers of painted items. Actions separated by comma (",").

Input: Capacity of the painting system and quantity of items as integers.

Output: The sequence of actions as a string.

Example:

checkio(2, 3)  # "01,12,02"
checkio(6, 3)  # "012,012"
checkio(3, 6)  # "012,012,345,345"
checkio(1, 4)  # "0,0,1,1,2,2,3,3"
checkio(2, 5)  # "01,01,23,42,34"
    
How it is used: This is similar to cooking three steaks in one frying pan. Each steak has two sides and it takes a minute to cook one side of two steaks, how would you cook all steaks in three minutes? This task takes the concept and models it in a technical way. The ideas behind the task also model real technological process in a factories.

Precondition:
0 < capacity ≤ 10
0 < number ≤ 10

尼古拉已经建立了一个半自动绘画系统，但是这个系统只能绘制一个物品的一面。 之后，操作员必须重新装载机器并对另一侧进行涂漆（系统会自动检测涂漆侧）。 绘画过程总是需要相同的时间。 相机一次可以绘制K个曲面。 Nicola希望Stephan操作喷漆机，他需要为Stephan开发一种算法，使他能够在最短的时间内绘制N（0 <N≤10）个曲面。 小心不要将物品涂抹两次以上。

系统
这些项目的编号从0到9.您获得机器的涂料容量（K）和项目数量（N）。 您应该返回斯蒂芬必须绘制的字符串，其中每个动作都是绘制项目的数量。 以逗号分隔的动作（“，”）。

输入：绘画系统的容量和作为整数的项目数量。

输出：作为字符串的动作序列。

如何使用：这与在一个煎锅中烹饪三块牛排相似。 每块牛排都有两面，需要一分钟的时间烹饪两块牛排的一面，如何在三分钟内烹制所有牛排？ 这项任务将采用这一概念并以技术方式对其进行建模。 这项任务背后的想法也模拟了工厂中真正的技术过程。
'''
