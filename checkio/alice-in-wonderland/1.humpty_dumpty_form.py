'''
I said you LOOKED like an egg, Sir,' Alice gently explained. 'And some eggs are very pretty, 
you know' she added, hoping to turn her remark into a sort of a compliment.

'Some people,' said Humpty Dumpty, looking away from her as usual, 'have no more sense than a baby!'

Alice didn't know what to say to this: it wasn't at all like conversation, 
she thought, as he never said anything to HER; in fact, his last remark was evidently 
addressed to a tree--so she stood and softly repeated to herself:--

Humpty Dumpty sat on a wall:
Humpty Dumpty had a great fall.
All the King's horses and all the King's men
Couldn't put Humpty Dumpty in his place again.
'That last line is much too long for the poetry,' she added, almost out loud, forgetting 
that Humpty Dumpty would hear her.

"Through the Looking-Glass." Lewis Carroll
After reading this fragment Nicola wants to build his own "Humpty Dumpty". As a basis he 
chooses the spheroid (read more about it on Wikipedia). We know the height and the width 
(in inches) for this spheroid. For the job at hand, Nikola needs to know how much material is required.

You can help him and create a function to calculate the volume (cubic inches) and the 
surface area (square inches).

spheroid
Tips: Be careful with sin-1x -- this is arcsin.

Input: Two arguments. A height and a width as integers.

Output: The volume and the surface area as a list of floats. The results should be 
accurate to two decimals.

Example:

checkio(4, 2) == [8.38, 21.48]
checkio(2, 2) == [4.19, 12.57]
checkio(2, 4) == [16.76, 34.69]
    
How it is used:
This is a simple math task, but we want to introduce you to the splendid shape -- spheroid 
(in case you hadn't heard of it yet).

The prolate spheroid is the shape of the ball in several sports, such as in rugby and 
Australian football. In American football, a more pointed prolate spheroid is used. Several 
moons of the Solar system approximate prolate spheroids in shape, though they are actually 
scalene. Examples are Mimas, Enceladus, and Tethys which orbit Saturn and Miranda which orbits Uranus.

The true shape of the Earth is called an Oblate Spheroid, though it is only very slightly 
oblate. The diameter from the North Pole to the South Pole (the shortest diameter) is approximately 
12,714 km. The equatorial diameter (the longest diameter) is approximately 12,756 km. This 
is not a big difference, but it does mean the Earth is not quite a sphere.

Precondition: 0 < width < 100
0 < height < 100

主席先生，我说你看起来像个鸡蛋，“爱丽丝轻轻地解释道。 “有些鸡蛋非常漂亮，你知道的，”她补充说，
希望把她的话变成一种恭维话。
“有些人，”矮胖子说，像往常一样远离她，“没有比婴儿更有意义的了！
爱丽丝不知道该说些什么：她想，这完全不像谈话，因为他从来没有对她说过任何话。事实上，他最后一句
话显然是写给了一棵树，于是她站起来，轻声重复着：

矮胖子坐在墙上：
胖胖的胖子倒下了。
所有的国王的马和所有的国王的人
不能再把矮胖子放在他的位置上。
“最后一行对于诗歌来说太长了，”她几乎大声地补充道，忘记了矮胖子会听到她的声音。

“通过镜子”。刘易斯·卡罗尔
看完片段后，尼古拉想要建立自己的“矮胖子”。作为一个基础，他选择了椭球体（在维基百科上阅读更多内容）。
我们知道这个球体的高度和宽度（以英寸为单位）。对于手头的工作，尼古拉需要知道需要多少材料。

你可以帮助他，并创建一个函数来计算体积（立方英寸）和表面积（平方英寸）。

球体
提示：小心sin-1x - 这是arcsin。

输入：两个参数。高度和宽度为整数。
输出：体积和表面积作为浮点列表。结果应该精确到小数点后两位。


如何使用它：
这是一个简单的数学任务，但我们想向您介绍精美的形状 - 球体（如果您还没有听说过）。

扁球体是橄榄球和澳大利亚橄榄球等几项运动中球的形状。在美式足球中，使用更尖锐的长椭球体。
几个太阳系的卫星近似长椭球体，虽然它们实际上是斜角。例如Mimas，土卫二和特提斯绕轨道土星和米兰达围绕天王星。

地球的真实形状被称为扁圆球体，尽管它只是非常轻微的扁圆形。从北极到南极（最短直径）的直径
约为12714公里。赤道直径（最长直径）约为12756公里。这不是一个很大的区别，但它确实意味着地球不是一个完全的球体。
'''

import math
def checkio(height, width):
    if height == width:
    	s = 4 * math.pi * (height / 2) ** 2
    	v = (4 / 3) * math.pi * (height / 2) ** 3
    else:
    	s = 4 * math.pi * ((height / 2) * (width / 2) * (width / 2)) ** (2/3)
    	v = (4 / 3) * math.pi * (height / 2) * (width / 2) * (width / 2)
    print([round(v, 2), round(s, 2)])
    return [round(v, 2), round(s, 2)]

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(4, 2) == [8.38, 21.48], "Prolate spheroid"
    assert checkio(2, 2) == [4.19, 12.57], "Sphere"
    assert checkio(2, 4) == [16.76, 34.69], "Oblate spheroid"