'''
You stand by the edge of a lake with two empty jars. You notice that both of the jars have a volume. You can fill each jar with water from the lake, pour water from one jar to the other or pour water back into lake. You should measure the volume of water in either jar. The required volume of water may be in either of the jars and it does not matter which.

Each action is described as a string of two symbols: from and to. The jars are marked as 1 and 2, the lake is marked 0. If you want to take water from the lake and fill first jar, then it's "01". To pour water from second jar into the first would be "21". Dump water out of the first jar and back into the lake would be "10". When you fill a jar from the lake, that jars volume will be full. When you pour water out a jar and into the lake, that jars volume will be empty. If you pour water from one jar to another, you can only pour as much as will fill the full volume of the receiving jar.

water-jars
The function has three arguments: The volume of first jar, the volume of second jar and the goal. All arguments are positive integers (number > 0). You should return a list with action's sequence.
The solution must contain the minimum possible number of steps

Input: The volume of first jar, the volume of second jar and the goal as integers.

Output: The sequence of steps as a list/tuple with strings.

Example:

checkio(5, 7, 6) == ['02', '21', '10', '21', '02', '21', '10', '21', '02', '21']
checkio(3, 4, 1) == ["02", "21"]

How it is used: This is a kind of optimisation problem with restrictions. It can be used for the development of the technological process and reducing cost of manufacturing.

Precondition: 
0 < first, second, goal < 10
goal ≤ first or goal ≤ second
All test cases have solution.
'''
