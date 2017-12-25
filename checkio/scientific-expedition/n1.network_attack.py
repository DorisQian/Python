"""
Nicola regularly inspects the local networks for security issues. He uses a smart and aggressive program which takes control of computers on the network. This program attacks all connected computers simultaneously, then uses the captured computers for further attacks. Nicola started the virus program in the first computer and took note of the time it took to completely capture the network. We can help him improve his process by modeling and improving his inspections.

We are given information about the connections in the network and the security level for each computer. Security level is the time (in minutes) that is required for the virus to capture a machine. Capture time is not related to the number of infected computers attacking the machine. Infection start from the 0th computer (which is already infected). Connections in the network are undirected. Security levels are not equal to zero (except infected).

Information about a network is represented as a matrix NxN size, where N is a number of computers. If ith computer connected with jth computer, then matrix[i][j] == matrix[j][i] == 1, else 0. Security levels are placed in the main matrix diagonal, so matrix[i][i] is the security level for the ith computer.

attack

You should calculate how much time is required to capture the whole network in minutes.

Input: Network information as a list of lists with integers.

Output: The total time of taken to capture the network as an integer.

Example:

capture([[0, 1, 0, 1, 0, 1],
         [1, 8, 1, 0, 0, 0],
         [0, 1, 2, 0, 0, 1],
         [1, 0, 0, 1, 1, 0],
         [0, 0, 0, 1, 3, 1],
         [1, 0, 1, 0, 1, 2]]) == 8
capture([[0, 1, 0, 1, 0, 1],
         [1, 1, 1, 0, 0, 0],
         [0, 1, 2, 0, 0, 1],
         [1, 0, 0, 1, 1, 0],
         [0, 0, 0, 1, 3, 1],
         [1, 0, 1, 0, 1, 2]]) == 4
capture([[0, 1, 1],
         [1, 9, 1],
         [1, 1, 9]]) == 9
    

How it is used: This concept shows how to model and examine various network configurations. The idea does not only apply to computer networks however, it can also be a model for the spread of disease or dissemination of rumors.

Precondition:

3 ≤ len(matrix) ≤ 10
matrix[0][0] == 0
all(len(row) == len(matrix[0]) for row in matrix)
all(matrix[i][j] == matrix[j][i] for i in range(len(matrix)) for j in range(len(matrix)))
all(0 < matrix[i][i] < 10 for i in range(1, len(matrix)))
all(0 ≤ matrix[i][j] ≤ 1 for i in range(len(matrix)) for j in range(len(matrix)) if i != j)

Nicola定期检查当地的网络安全问题。他使用了一个智能和侵略性的程序控制计算机在网络上。该程序同时攻击所有连接的计算机，然后使用捕获的计算机进行进一步的攻击。Nicola在第一个计算机上启动了病毒程序，并注意到它花了很多时间来完全捕获网络。我们可以通过建模和改进他的检查来帮助他改进流程。
我们得到了关于网络中的连接和每台计算机的安全级别的信息。安全级别是病毒捕捉机器所需的时间(分钟)。捕获时间与攻击机器的受感染计算机的数量无关。感染从第0台计算机(已经被感染)开始。网络中的连接是无定向的。安全级别不等于零(除了受感染)。
网络的信息表示为一个矩阵NxN的大小，其中N是许多计算机。如果第i个计算机与第j个计算机连接，则矩阵[i][j]= =矩阵[i]= = 1，否则为0。安全级别被放置在主矩阵对角线上，因此矩阵[i][i]是第i计算机的安全级别。
攻击
您应该计算在几分钟内捕获整个网络所需的时间。

输入:网络信息作为列表的整数列表。
输出:以整数捕获网络的总时间。

如何使用:这个概念展示了如何建模和检查各种网络配置。这个想法不仅适用于计算机网络，它也可以成为传播疾病或传播谣言的一种模式。
"""

