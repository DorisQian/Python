'''
Several power plants in this area exploded last night. We don’t know why yet. Our engineering team is still trying to figure it out. I think it was some kind of a bug. I told them not to release anything only 5 minutes before leaving for the day.

Anyway…

For emergencies, we have a couple of mobile power stations. Help us to figure out which cities blacked out so we can send them there as soon as possible.

Fortunately, we still have the original plan of the electricity grid and already removed the blown up power plants from it. The updated plan now shows the remaining power plants, their supply range as well as their connections to the power grid. This should be enough for you to figure out which cities are not getting power.

You are given the power grid and power-plant's information (plant-number and supply-range). You should find out which cities blacked out. A power plant can supply itself and connected cities with power, but the range is limited.



Input: Two arguments. The first one is the network, represented as a list of connections. Each connection is a list of two nodes that are connected. A city or power plant can be a node. Each city or power plant is a unique string. The second argument is a dict where keys are power plants and values are the power plant's range.

Output: A set of strings. Each string is the name of a blacked out city.

Example:


power_supply([['p1', 'c1'], ['c1', 'c2']], {'p1': 1}) == set(['с2'])
power_supply([['c0', 'c1'], ['c1', 'p1'], ['c1', 'c3'], ['p1', 'c4']], {'p1': 1}) == set(['c0', 'c3'])
power_supply([['p1', 'c1'], ['c1', 'c2'], ['c2', 'c3']], {'p1': 3}) == set([])

Precondition:

len(set(chain(*networks))) <= 25

这个地区的几个发电厂昨晚爆炸了。我们现在还不知道为什么。我们的工程团队仍在努力弄清楚。我认为这是一种错误。我告诉他们不要在出发前五分钟发布任何东西。

无论如何…

对于紧急情况，我们有几个移动电站。帮助我们弄清楚哪些城市已经停电，所以我们尽快把它们寄到那里。

幸运的是，我们仍然有原有的电网规划，并已经从中拆除了电站。现在更新的计划显示了剩余的发电厂，它们的供电范围以及它们与电网的连接。这应该足以让你找出哪些城市没有获得权力。

您将得到电网和发电厂的信息（工厂号和供应范围）。你应该找出哪些城市停电了。发电厂可以为自己和连接的城市供电，但范围有限。



输入：两个参数。第一个是网络，表示为连接列表。每个连接都是连接的两个节点的列表。城市或发电厂可以是节点。每个城市或发电厂是一个独特的字符串。第二个参数是一个字典，其中键是电厂，值是电厂的范围。
输出：一组字符串。每个字符串都是黑色城市的名称。
'''
