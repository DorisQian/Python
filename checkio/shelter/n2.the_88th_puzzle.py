'''
Dr. Emmett Brown: If my calculations are correct, when this baby hits 88 miles 
per hour... you're gonna see some serious shit.

===

Marty McFly: Hey, Doc, we better back up. We don't have enough road to get up to 88.
Dr. Emmett Brown: Roads? Where we're going, we don't need roads.

"Back to the Future" (1985)
According to ancient Chinese legend, 88 is a magic number. On the 88th page of the 
book, "Ancient human puzzles catalog for modern robots", you will find a puzzle which 
Nikola’s archaeologist uncle discovered a very long time ago in an ancient human magazine. 
Nikola has been trying to solve this puzzle since he first rolled off his parents assembly 
line, and now it’s time for us to help him figure this out once and for all.

The puzzle looks like four intersecting circles with 12 colored marbles: 2 red, 2 blue, 
2 green, 2 orange and 4 grey. Take a look at the illustration to see how this setup works. 
The marbles should be placed as it shown below. Each hole and color has a number for data 
representing a state. Colored numbers: 1 - blue, 2 - green, 3 - red, 4 - orange, 0 - grey. 
The initial state (or completed) will be represented as the sequence of numbers, where an 
index is a “hole” number: 
(1, 2, 1, 0, 2, 0, 0, 3, 0, 4, 3, 4).

initial_state

You can rotate the rings clockwise. Each move rotates the ring by 90 degrees. The rings are 
numbered and sequence of action should be represented as a list/tuple of numbers from 1 to 4.

You are given a twisted puzzle state as a tuple of numbers. You should return it to the initial 
state with the minimal number of steps. For example, the state in the picture below would be 
represented as (0,2,1,3,2,1,4,0,0,4,0,3) and can be solved in 4 steps "1433" or "4133". The 
first means "rotate 1st ring one time (by 90 degrees of course), 4th - one time, 3th - two times.

state

Input: A puzzle state as a tuple of integers.
Output: The shortest solution as a string.

Example:

puzzle88((0,2,1,3,2,1,4,0,0,4,0,3)) == "1433"
    

How it is used: This is one more puzzle which will show you how you can use computer modeling 
and simulation to solve an abstract problem - in this case, a combinatorial problem.

Precondition:
len(state) == 12
all(0 ≤ n ≤ 4 for n in state)
All test cases are solvable.

艾米特布朗博士：如果我的计算是正确的，那么当这个婴儿撞到88英里时
每小时...你会看到一些严重的狗屎。

===

Marty McFly：嘿，医生，我们最好备份一下。我们没有足够的马路来达到88。
埃米特布朗博士：道路？我们要去哪里，我们不需要道路。

“回到未来”（1985）
据中国古代传说，88是一个神奇的数字。在第88页
书，“古代人类困惑现代机器人目录”，你会发现一个谜题
尼古拉的考古学家叔叔很早以前就在一本古老的人类杂志中发现。
自从他第一次推出父母会议以来，尼古拉一直试图解决这个难题
现在是时候让我们帮助他彻底解决这个问题了。

这个谜题看起来像四个相交的圆圈，有12个彩色弹珠：2个红色，2个蓝色，
2个绿色，2个橙色和4个灰色。看看插图，看看这个设置是如何工作的。
大理石应放置如下图所示。每个孔和颜色都有一个数据编号
代表一个国家。彩色数字：1 - 蓝色，2 - 绿色，3 - 红色，4 - 橙色，0 - 灰色。
初始状态（或完成）将表示为数字序列，其中a
索引是一个“洞”号码：
（1，2,1,0,2,0,0,3,0,4,3,4）。

initial_state

您可以顺时针旋转环。每次移动都会使环旋转90度。戒指是
编号和动作顺序应该表示为从1到4的数字的列表/元组。

你被赋予一个扭曲的谜题状态作为数字元组。你应该将它返回到最初
以最少的步数进行状态。例如，下图中的状态是
表示为（0,2,1,3,2,1,4,0​​,0,4,0,3）并且可以用4个步骤“1433”或“4133”来解决。该
第一种意思是“一次旋转第一圈（当然是90度），第四次 - 一次，第三次 - 两次。州

输入：拼图状态为整数元组。
输出：作为一个字符串的最短解决方案。

例：

puzzle88（（0,2,1,3,2,1,4,0​​,0,4,0,3））==“1433”
    
它是如何使用的：这是另一个难题，它将告诉你如何使用计算机建模
和模拟来解决一个抽象问题 - 在这种情况下是一个组合问题。

前提：
len（state）== 12
全部（状态中n为0≤n≤4）
所有的测试用例都可以解决。
'''