"""
Sophia's drones are not soulless and stupid drones; they can make and have friends. In fact, they already are working for the their own social network just for drones! Sophia has received the data about the connections between drones and she wants to know more about relations between them.

We have an array of straight connections between drones. Each connection is represented as a string with two names of friends separated by hyphen. For example: "dr101-mr99" means what the dr101 and mr99 are friends. Your should write a function that allow determine more complex connection between drones. You are given two names also. Try to determine if they are related through common bonds by any depth. For example: if two drones have a common friends or friends who have common friends and so on.

network
Let's look at examples:
scout2 and scout3 have the common friend scout1 so they are related. super and scout2 are related through sscout, scout4 and scout1. But dr101 and sscout are not related.

Input: Three arguments: Information about friends as a tuple of strings; first name as a string; second name as a string.

Output: Are these drones related or not as a boolean.

Example:

check_connection(
    ("dr101-mr99", "mr99-out00", "dr101-out00", "scout1-scout2",
     "scout3-scout1", "scout1-scout4", "scout4-sscout", "sscout-super"),
    "scout2", "scout3") == True
check_connection(
    ("dr101-mr99", "mr99-out00", "dr101-out00", "scout1-scout2",
     "scout3-scout1", "scout1-scout4", "scout4-sscout", "sscout-super"),
    "dr101", "sscout") == False

How it is used: This concept will help you find not too obvious connections with the building of bond networks. And how to work social networks.

Precondition: len(network) ≤ 45
if "name1-name2" in network, then "name2-name1" not in network
3 ≤ len(drone_name) ≤ 6
first_name and second_name in network.

索菲亚的无人机不是没有灵魂和愚蠢的无人机;他们可以交朋友，也可以交朋友。事实上，他们已经在为他们自己的社交网络工作，仅仅是为了无人机!索菲亚已经收到关于无人机之间的联系的数据，她想知道更多关于他们之间的关系。
我们有一系列的无人机之间的直线连接。每个连接都表示为一个字符串，其中有两个由连字符分隔的好友名称。例如:“dr101 - mr99”意味着dr101和mr99是朋友。你应该写一个函数，它可以决定无人机之间更复杂的连接。你也有两个名字。试着确定它们是否与任何深度的共同债券相关。例如:如果两架无人机有普通朋友或朋友，他们有共同的朋友，等等。
网络
让我们来看看例子:
scout2和scout3有普通朋友scout1，所以它们是相关的。超级和scout2是通过sscout,scout4和scout1相关的。但是dr101和sscout并没有关系。
输入:三个参数:关于朋友的信息作为字符串的元组;第一个名称为字符串;第二个名称作为字符串。
输出:这些无人机是相关的还是布尔型的。
"""
