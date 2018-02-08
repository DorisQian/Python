'''
"Wow! That was amazing!" Stephen was greatly impressed. He took his eyes off the telescope and leaned back.

"Did you see that?" asked Sofia.

...moments ago a super massive black hole had just "swallowed" another one...

"You were right Sofia, that was an incredible event" Stephen said. "So, can I join your A&A (Astronomy & Astrophysics) research group?"

Sofia looked at him triumphantly and said - "Really, my plan was to rope you in anyway! We are currently researching black holes and their gravitational fields and we are looking for someone to help us create a software model that will predict the future state of black holes".

"Hmm, it's very interesting. Let me try...".

You need to help Stephen implement a software model (function) that predicts the state of black holes under a controlled environment. The A&A research team has identified some peculiarities in the behavior of black holes.

To create the software model one should take into account:

1. The cartesian coordinate system is used to map out the black holes.
2. Each black hole is represented as a circle with x, y (center coordinates) and r (radius).
3. In contrast to the area, which may change during the absorption process, the coordinates remain constant.
4. The area of a black hole greatly influences its mass, and consequently, the gravitational field.
5. The absorption order of black holes depends on the distance between their centers, starting with the black holes that are closest to each other. If the distance between different black holes is equal, then the leftmost black hole in the list should merge first.
6. The absorption process (merging) of black holes is possible if and only if the following conditions are met:
   - The intersection area of the two black holes is greater than or equal to 55% (>= 55%) of one of the two black holes area.
   - The area of one of the two black holes is over 20% (>= 20%) more than the area of the other.
7. If one black hole absorbs another, their areas are summarized as (Stotal = S1 + S2).
8. The absorption process continues as long as all conditions are met (see p. 6).
Let's look at some simple examples:

Input: [(2, 4, 2), (3, 9, 3)]
No intersection
Output: [(2, 4, 2), (3, 9, 3)]



first-example	Input: [(0, 0, 2), (-1, 1, 2)]
S1 = 12.57; S2 = 12.57
Intersection area = 7.03
p1 = 56% p2 = 56%
Domination: 0%
Output: [(0, 0, 2), (-1, 1, 2)]
first-example	Input: [(1, 3, 2), (1, 3, 2.19)]
S1 = 12.57; S2 = 15.07
Domination: 19.9%
Output: [(1, 3, 2), (1, 3, 2.19)]


first-example
More complex example: [(2, 2, 3), (0, 4, 2), (4, 6, 2), (4.7, 3, 0.5)]

Steps	Before
Input: [(2, 2, 3), (0, 4, 2), (4, 6, 2), (4.7, 3, 0.5)]
R1, R2 - distance (2.83); S1 = 28.27; S2 = 12.57
Intersection area = 6.04
p1 = 21% p2 = 48%
Output: [(2, 2, 3), (0, 4, 2), (4, 6, 2), (4.7, 3, 0.5)]
----------------------------------------------------------
Input: [(2, 2, 3), (0, 4, 2), (4, 6, 2), (4.7, 3, 0.5)]
R1, R4 - distance (2.88); S1 = 28.27; S4 = 0.79
Intersection area = 0.5
p1 = 2% p4 = 63%
Output: [(2, 2, 3.04), (0, 4, 2), (4, 6, 2)]
----------------------------------------------------------
Input: [(2, 2, 3.04), (0, 4, 2), (4, 6, 2)]
R1, R2 - distance (2.83); S1 = 29.03; S2 = 12.57
Intersection area = 6.21
p1 = 21% p4 = 49%
Output: [(2, 2, 3.04), (0, 4, 2), (4, 6, 2)]
----------------------------------------------------------
Input: [(2, 2, 3.04), (0, 4, 2), (4, 6, 2)]
R1, R3 - distance (4.47); S1 = 29.03; S2 = 12.57
Intersection area = 0.87
p1 = 3% p4 = 7%
Output: [(2, 2, 3.04), (0, 4, 2), (4, 6, 2)]
----------------------------------------------------------
Input: [(2, 2, 3.04), (0, 4, 2), (4, 6, 2)]
R2, R3 - distance (4.47)
S1 = 12.57; S2 = 12.57
No intersection
----------------------------------------------------------
Output: [(2, 2, 3.04), (0, 4, 2), (4, 6, 2)]
first-example
After
first-example
Input: A list of tuples [(x, y, r), ..., ...], where x, y - coordinates, r - radius of a black hole

Output: Predictable (final) state of black holes as a list/tuple of lists/tuples, radius should be given with two digits precision as ±0.01.

Example:

checkio([(0, 0, 2.1)]) == [(0, 0, 2.1)]
checkio([(2, 4, 2), (3, 9, 3)]) == [(2, 4, 2), (3, 9, 3)]
checkio([(3, 3, 3), (2, 2, 1), (3, 5, 1.5)]) == [(3, 3, 3.5)]

How it is used: You can use this in game development (see Agar.io example), studying geometry or developing software models of real physical processes.

Precondition: 1 ≤ len(data) ≤ 20
0.5 ≤ radius ≤ 10
x ∈ [-100; 100], y ∈ [-100; 100]

“哇！太棒了！”斯蒂芬深受感动。他把眼睛从望远镜上移开，向后靠。

“你看到了吗？”索非亚问。

...刚才一个超级巨大的黑洞刚刚“吞噬”另一个...

“你是对的索非亚，这是一个令人难以置信的事件”斯蒂芬说。 “那么，我可以加入你的A＆A（天文和天体物理学）研究小组吗？

索非亚高高兴兴地看着他说：“真的，我的计划是要把你绳上去！我们正在研究黑洞及其引力场，我们正在寻找人来帮助我们创建一个软件模型来预测未来的状态黑洞”。

“呃，这很有趣，让我试试...”。

您需要帮助Stephen实施一个软件模型（功能），以预测受控环境下的黑洞状态。 A＆A研究小组确定了黑洞行为的一些特点。

要创建软件模型，应该考虑到：

1.笛卡尔坐标系用来绘制黑洞。
2.每个黑洞表示为一个带有x，y（中心坐标）和r（半径）的圆。
3.与在吸收过程中可能改变的区域相比，坐标保持不变。
来自“简明英汉词典”黑洞的面积极大地影响了它的质量，从而也影响了引力场。
5.黑洞的吸收顺序取决于它们的中心之间的距离，从彼此最接近的黑洞开始。如果不同黑洞之间的距离相等，则列表中最左边的黑洞应该先合并。
6.当且仅当符合下列条件时，黑洞的吸收过程（合并）才有可能：
    - 两个黑洞的交点面积大于或等于两个黑洞面积之一的55％（> = 55％）。
    - 两个黑洞之一的面积比另一个面积多20％（> = 20％）。
7.如果一个黑洞吸收了另一个黑洞，则它们的区域总结为（Stotal = S1 + S2）。
8.只要满足所有条件，吸收过程就会继续（见第6页）。
我们来看一些简单的例子：

输入：元组列表[（x，y，r），...，...]，其中x，y - 坐标，r - 黑洞半径
输出：黑洞的可预测（最终）状态作为列表/元组的列表/元组，半径应以±0.01的两位数字精度给出。

它是如何使用的：你可以在游戏开发中使用它（参见Agar.io例子），研究几何或者开发真实物理过程的软件模型。
'''