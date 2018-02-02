'''
In a race, the quickest runner can never overtake the slowest, since the pursuer 
must first reach the point whence the pursued started, so that the slower must always hold a lead.

– as recounted by Aristotle, Physics VI:9, 239b15
"Achilles and the tortoise" is one of the famous Zeno's paradoxes. Nikola wants to 
check the validity of the paradox and constructed two robots for this purpose: 
Achilleborg (A1 -- fast agile prototype) and Tortoimenator (T2 -- heavy slow cyborg).

A1 is faster than T2, so it has a X seconds head start on A1. For X seconds T2 
will move at t2_speed*X metres. So A1 must first reach the point whence T2 already 
reached. But T2 is moving and next step for A1 is to reach the next point and so on 
to infinity. The paradox is correct in theory, but in practice A1 easily outruns T2.
 Hm... maybe we can calculate when A1 will catch up to T2.

A1-T2
You are given A1 and T2’s speed in m/s as well as the length of the advantage T2 has 
in seconds. Try to count the time when from when A1 come abreast with T2 (count from 
T2 start). The result should be given in seconds with precious ±10-8.

Input: Three arguments. Speeds of A1 and T2 and advantage as integers.

Output: The time when A1 catch up T2 (count from T2 start) as an integer or float.

Example:

chase(6, 3, 2) == 4
chase(10, 1, 10) == 11.11111111
    

How it is used: Let's return to school and remember our basic math principles. 
Sometimes simple arithmetic allows us to resolve difficult paradox problems easily.

Precondition:
t2_speed < a1_speed < 343
0 < advantage ≤ 60

在比赛中，最快的跑步者永远不可能超越追赶者以来最慢的跑步者
必须首先达到所追求的目标，所以慢必须始终保持领先。

- 如亚里士多德所述，物理VI：9,239b15
“阿基里斯和乌龟”是着名的芝诺悖论之一。尼古拉想要
检查悖论的有效性，并为此构建了两个机器人：
Achilleborg（A1 - 快捷敏捷原型）和Tortoimenator（T2 - 重慢机器人）。

A1比T2快，所以它在A1上有一个X秒的开头。对于X秒T2
将在t2_speed * X米移动。所以A1必须先到达T2的地步
到达。但T2正在移动，A1的下一步是到达下一个点，依此类推
到无穷远。悖论在理论上是正确的，但在实践中，A1很容易超过T2。
 呃...也许我们可以计算出A1会赶上T2。

A1-T2
给你A1和T2的速度（m / s）以及T2的长度
很快。试着从A1和T2并行的时候开始计算
T2开始）。结果应该在几秒钟内给出宝贵的±10-8。

输入：三个参数。 A1和T2的速度和作为整数的优势。
输出：A1作为整数或浮点数追上T2（从T2开始计数）的时间。

如何使用：让我们回到学校，记住我们的基本数学原理。
有时候简单的算术可以让我们很容易地解决难题。

'''