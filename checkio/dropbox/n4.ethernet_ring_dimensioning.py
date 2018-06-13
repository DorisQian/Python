'''
A ring topology is a network configuration where the devices are connected to each 
other in a circular shape. Optical rings are widely used in mobile networks to transport 
the traffic from a base station to the backbone, through the mobile backhaul.

ITU backhaul with rings

Definition of a ring

For the sake of simplicity, in this task, we define a ring as a connex graph which vertexes:

- have a degree 2, which means they have 2 incident edges.
- are connected to two distinct vertexes

These two conditions ensure that there is a single link between each pair of adjacent nodes. 
Ring are represented as a string made of distinct characters, which position in the string 
reflects the position in the ring. For instance, the ring "AEFCBG" defines the following topology:
ring definition

Shortest path asymmetric routing

Multiple traffic flows will be routed on the ring. 
Each flow is routed on the shortest path from the ingress node (starting point of the traffic) 
to the egress node (exit point of the traffic).
If there are two shortest paths, the path which order fits the ring definition is kept.
Let's consider the following situation:
paths along the ring

The path from A to B (and from B to A) will be "A - G - B", because it uses only two links, while 
the path going the other way around ("A - E - F - C - B") uses five links.
However, there are two paths of equal length to route a traffic from A to C: "A - E - F - C" and 
"A - G - B - C". The first one, "A - E - F - C", is kept: it is the same order as in the ring definition ("AEFCBG").
The traffic from C to A will use the path "C - B - G - A": the routing is asymmetric in that case.
Flow aggregation

A traffic flow is represented as a couple (s, dr) where:

- s is a string of length 2, containing the ingress node and the egress node.
- dr is the data rate in Gbps (gigabit per second).

The data rate of a traffic flow will be counted for all the links of the shortest path.
A traffic flow ("AB", 5) means that 5 Gbps will be routed on the shortest path from A to B. 
We count 5 Gbps on the link "AG" and 5 Gbps on the link "GB". For a traffic flow ("CA", 15), we 
count 15 Gbps on the links "CB", "BG", and "GA".
In order to simplify the model, we consider that the traffic flows ingress -> egress and egress -> 
ingress are equivalent with regard to dimensioning.
Two traffic flows ("AG", 3) and ("GA", 3) induce a 6-Gbps flow on the link AG, as would ("AG", 6) 
or ("GA", 6): links are not directional. Given a list of traffic flows, we consider the resulting 
bandwidth on each link to dimension the ring.
Ethernet links dimensioning

There are five main types of Ethernet links used in mobile networks:

- Fast Ethernet (FE): 100 Mbps (or 0.1 Gbps)
- Gigabit Ethernet (GE): 1 Gbps.
- 10 Gigabit Ethernet (10GE): 10 Gbps
- 40 Gigabit Ethernet (40GE): 40 Gbps.
- 100 Gigabit Ethernet (100GE): 100 Gbps.

In order to select a type of link, we look for the smallest bandwidth allowing to carry the whole 
traffic with a single link. Handling a 5-Gbps traffic would require 50 FE links, 5 GE links, 
or 1 10GE link. Therefore, a 10GE Ethernet link is used. For a 15-Gbps traffic, a 40GE Ethernet 
link is required. For a traffic higher than 100 Gbps, 100GE Ethenet links are used (2 100GE Ethernet 
links for a 101-Gbps flow).
Given a ring and a list of traffic flows, you should return the number of Ethernet links of each 
type that are required to carry the resulting bandwidth:
resulting dimensioning


In this example, we have 10 Gbps from E to C, 5 Gbps from A to C and 60 Gbps from A to B.
These traffic flows induce the following bandwidth: 15 Gbps from E to C, 5 Gbps from A to E and 60 
Gbps from A to B.
The link dimensioning results in 2 100GE, 2 40GE and 1 10GE Ethernet links.
The result is given as a list containing the number of links for each category, from 100GE to FE. In 
our example, the result is [2, 2, 1, 0, 0]

Input: A variable number of arguments. The first one is a ring, represented as a string where each 
character is a node. The remaining arguments are traffic flows, represented as couples (s, dr) where 
s is a 2-characters string (ingress node, egress node) and dr is a positive value (traffic in Gbps).

Output: A list with 5 integers, one per type of link, in decreasing order of bandwidth capacity.

Example:

checkio("AEFCBG", ("AC", 5), ("EC", 10), ("AB", 60)) == [2, 2, 1, 0, 0]
checkio("ABCDEFGH", ("AD", 4)) == [0, 0, 3, 0, 0]
checkio("ABCDEFGH", ("AD", 4), ("EA", 41)) == [4, 0, 3, 0, 0]

How it is used: Links dimensioning is used for network planning and design. For real networks, 
various softwares are used to dimension the network based on the expected traffic load (for pre-sales 
engineers, when the network does not yet exist), or traffic measurements (for post-sales engineers to 
compute how much traffic the network can handle, and plan the network evolution). 
However, real-life network dimensioning is much more complex than what is described in this task, as 
it deals with traffic differentiation and protection against equipment failure.

Preconditions:
The ring is a valid ring (connex, 2-degree nodes).
The traffic is a positive value (integer or float).

环形拓扑是设备连接到每个设备的网络配置
其他以圆形形状。光环广泛用于移动网络传输
通过移动回程从基站到骨干网的流量。

国际电联回程与环

戒指的定义

为了简单起见，在这个任务中，我们将一个环定义为顶点的连接图：

- 有2级，这意味着他们有2个事件边缘。
- 连接到两个不同的顶点

这两个条件确保每对相邻节点之间存在单个链接。
环被表示为由不同字符组成的字符串，它们位于字符串中
反映了环中的位置。例如，环“AEFCBG”定义了以下拓扑：
环定义

最短路径不对称路由

多个业务流将在环上路由。
每个流都在来自入口节点的最短路径上（流量的起点）
到出口节点（流量的出口点）。
如果有两条最短路径，则保持顺序适合环定义的路径。
让我们考虑以下情况：
沿着环的路径

从A到B（从B到A）的路径将是“A-G-B”，因为它只使用两个链接，而
（“A - E - F - C - B”）的路径使用五个链接。
但是，有两条等长的路径将路由从A到C的流量：“A - E - F - C”和
“A - G - B - C”。第一个“A - E - F - C”被保留下来：它与环形定义（“AEFCBG”）的顺序相同。
从C到A的流量将使用路径“C-B-G-A”：在这种情况下，路由不对称。
流量聚合

交通流量表示为一对（s，dr），其中：

- s是长度为2的字符串，包含入口节点和出口节点。
- dr是数据速率，单位为Gbps（千兆比特每秒）。

对于最短路径的所有链路，流量的数据速率将被计算在内。
流量（“AB”，5）表示5 Gbps将在从A到B的最短路径上路由。
我们在“AG”链接上计算5 Gbps，在“GB”链接上计算5 Gbps。对于交通流（“CA”，15），我们
在“CB”，“BG”和“GA”链接上计数15 Gbps。
为了简化模型，我们考虑流量入口 - >出口和出口 - >
在尺寸方面，入口是等效的。
（“AG”，6）两个业务流（“AG”，3）和（“GA”，3）在链路AG上产生6-Gbps流。
或（“GA”，6）：链接不是定向的。给定一个流量列表，我们考虑结果
每个链路上的带宽来确定环的尺寸。
以太网链接尺寸

移动网络中使用的以太网链路主要有五种类型：

- 快速以太网（FE）：100 Mbps（或0.1 Gbps）
- 千兆以太网（GE）：1 Gbps。
- 10千兆以太网（10GE）：10 Gbps
- 40千兆以太网（40GE）：40 Gbps。
- 100千兆以太网（100GE）：100 Gbps。

为了选择一种链路类型，我们寻找可以承载整个链路的最小带宽
只有一个链接的流量。处理5-Gbps流量需要50条FE链路，5条GE链路，
或1个10GE链路。因此，使用10GE以太网链路。对于15-Gbps流量，40GE以太网
链接是必需的。对于高于100 Gbps的流量，使用100GE Ethenet链路（2个100GE以太网
链接为101-Gbps流量）。
给定一个环和一个流量列表，你应该返回每个以太网链路的数量
输入带宽所需的类型：
由此产生尺寸

在这个例子中，我们有从E到C的10 Gbps，从A到C的5 Gbps和从A到B的60 Gbps。
这些业务流会产生以下带宽：从E到C的15 Gbps，从A到E和60的5 Gbps
从A到B的Gbps。
链路尺寸标注可以生成2个100GE，2个40GE和1个10GE以太网链路。
结果以包含每个类别的链接数量的列表形式给出，从100GE到FE。在
我们的例子中，结果是[2,2,1,0,0]

输入：可变数量的参数。第一个是一个环，表示为每个字符串
字符是一个节点。其余的参数是交通流量，以夫妇（s，dr）表示
s是一个2个字符的字符串（入口节点，出口节点），dr是一个正值（以Gbps为单位的流量）。

输出：具有5个整数的列表，每个链接类型一个，按照带宽容量的降序排列。

如何使用：链接尺寸标注用于网络规划和设计。对于真实的网络，
根据预期的流量负载（用于售前），使用各种软件来确定网络的尺寸
工程师，当网络尚不存在时）或流量测量（对于售后工程师来说）
计算网络可以处理多少流量，并规划网络演进）。
然而，现实生活中的网络维度比这个任务中描述的要复杂得多，因为
它处理流量分化和防止设备故障。
'''
图见具体网页