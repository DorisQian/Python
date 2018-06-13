'''
An IP network is a set of routers that communicate routing information using a protocol. 
A router is uniquely identified by an IP address. 
In IPv4, an IP address consists of 32 bits, canonically represented as 4 decimal numbers 
of 8 bits each. The decimal numbers range from 0 (00000000) to 255 (11111111).
Each router has a "routing table" that contains a list of IP addresses, for the router to 
know where to send IP packets.
Route summarization in IP networks
As the network grows large (hundreds of routers), the number of IP addresses in the routing 
table increases rapidly. Maintaining a high number of IP addresses in the routing table would 
result in a loss of performances (memory, bandwidth and CPU resources limitation).
Route summarization, also called route aggregation, consists in reducing the number of routes 
by aggregating them into a "summary route".

Let's consider the following example:
summary route

We have 4 routers connected to A. A is aware about all 4 IP addresses, because it has a direct 
interface to each of them. However, A will not send them all to B.
Instead, it will aggregate the addresses into a summary route, and send this new route to B. 
This implies that: 

- Less bandwidth is used on the link between A and B.
- B saves memory: it has only one route to store in its routing table
- B saves CPU resources: there are less entries to consider when handling incoming IP packets
Computing a summary route
A has all 4 addresses stored in its routing table. 

Address 1	172.16.12.0
Address 2	172.16.13.0
Address 3	172.16.14.0
Address 4	172.16.15.0

A will convert these IP addresses to binary format, align them and find the boundary line between 
the common prefix on the left (highlighted in red), and the remaining bits on the right. 

Address 1	10101100	00010000	00001100	00000000
Address 2	10101100	00010000	00001101	00000000
Address 3	10101100	00010000	00001110	00000000
Address 4	10101100	00010000	00001111	00000000

A creates a new IP address made of the common bits, and all other bits set to "0".
This new IP address is converted back to decimal numbers.
Finally, A computes the number of common bits, also called "subnet".
The summary route is this new IP address, followed by a slash and the subnet: 172.16.12.0/22
Input: A list of strings containing the IP addresses
Output: A string containing the summary route, represented as an IP address, followed by a slash and the subnet.

Example:

checkio(["172.16.12.0", "172.16.13.0", "172.16.14.0", "172.16.15.0"]) == "172.16.12.0/22"
checkio(["172.16.12.0", "172.16.13.0", "172.155.43.9"]) == "172.0.0.0/8"
checkio(["172.16.12.0", "172.16.13.0", "172.155.43.9", "146.11.2.2"]) == "128.0.0.0/2"

Preconditions: 
all(re.match(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$",d) for d in data))
all(-1 < int(n) < 256 for n in d.split(".") for d in data)
len(data) == len(set(data)) and len(data) > 1

IP网络是一组使用协议传送路由信息的路由器。
路由器由IP地址唯一标识。
在IPv4中，IP地址由32位组成，标准地表示为4位十进制数
每个8位。十进制数的范围从0（00000000）到255（11111111）。
每个路由器都有一个“路由表”，其中包含路由器的IP地址列表
知道在哪里发送IP数据包。
IP网络中的路由汇总
随着网络规模越来越大（数百个路由器），路由中的IP地址数量也越来越多
表格迅速增加。在路由表中维护大量的IP地址会
导致性能损失（内存，带宽和CPU资源限制）。
路由汇总也称为路由汇聚，包括减少路由数量
通过将它们聚合成一个“总结路线”。

我们来考虑下面的例子：
总结路线

我们有4台路由器连接到A.A知道所有4个IP地址，因为它有直接的
接口到他们每个人。但是，A不会全部发送给B.
相反，它会将地址聚合成一个汇总路线，并将此新路线发送到B.
这意味着：

- 在A和B之间的链路上使用较少的带宽。
B保存内存：它只有一个路由存储在路由表中
- B节省CPU资源：处理传入IP数据包时要考虑的条目较少
计算总结路线
A的所有4个地址存储在其路由表中。

地址1 172.16.12.0
地址2 172.16.13.0
地址3 172.16.14.0
地址4 172.16.15.0

A会将这些IP地址转换为二进制格式，对齐它们并找到它们之间的边界线
左侧的常用前缀（以红色突出显示）和右侧的其余位。

地址1 10101100 00010000 00001100 00000000
地址2 10101100 00010000 00001101 00000000
地址3 10101100 00010000 00001110 00000000
地址4 10101100 00010000 00001111 00000000

A会创建一个由公共位构成的新IP地址，并将所有其他位设置为“0”。
这个新的IP地址被转换回十进制数。
最后，A计算通用位的数量，也称为“子网”。
摘要路由是这个新的IP地址，后面跟着一个斜杠和子网：172.16.12.0/22
输入：包含IP地址的字符串列表
输出：包含汇总路由的字符串，表示为IP地址，后跟斜杠和子网。
'''