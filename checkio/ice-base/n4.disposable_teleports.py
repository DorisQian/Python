'''
dteleports-pic The island has eight stations which are connected by a network of teleports; however, the teleports take a very long time to recharge. This means you can only use each one once. After you use a teleport, it will shut down and no longer function. But you can visit any station more than once. For this task, you should begin at number 1 and try to travel around to all the stations before returning to the starting point. The map of the teleports is presented as a string in which the comma-separated list represents teleports. Each teleport is given the name of the station it connects to. This name consists of two digits, such as '12' or '32.' Each test requires you to provide a route which passes through every station. A route is presented as a string of the station numbers in the sequence in which they must be visited (ex. 123456781).

disposable-teleports

Input: A teleport map as a string.

Output: The sequence of station numbers as a string.

Example:

checkio("12,23,34,45,56,67,78,81") == "123456781"
checkio("12,28,87,71,13,14,34,35,45,46,63,65") == "1365417821"
checkio("12,15,16,23,24,28,83,85,86,87,71,74,56") == "12382478561"
checkio("13,14,23,25,34,35,47,56,58,76,68") == "132586741"

How it is used: This task is another example of the graph-search problem. It’s like trying to find a route where you can not to step on the same spot twice.

Precondition:
len(stations) == 8
Teleports are not repeated and undirected.

dteleports-pic岛上有八个通过传送网连接的电台;然而，传送花费很长时间来充电。这意味着你只能使用一次。使用传送器后，它将关闭，不再起作用。但是你可以不止一次去任何一个站点。对于这个任务，你应该从1号开始，在返回到起点之前尝试绕过所有车站。传送的地图以逗号分隔的列表表示传送的字符串呈现。每个传送点都给出了它连接的站点的名称。该名称由两个数字组成，如“12”或“32”。每个测试都要求您提供一条通过每个站点的路线。一条路线按照必须被访问的顺序（例如123456781）作为一串车站号码呈现。

一次性-传送点

输入：一个传送地图作为一个字符串。
输出：站号的序列作为一个字符串。

如何使用：这个任务是图搜索问题的另一个例子。这就像试图找到一个路线，你不能在同一个地方踩两次。

前提：
len（站）== 8
传送不重复，不重复。
'''