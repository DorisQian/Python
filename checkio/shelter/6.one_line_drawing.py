'''
“The line that describes the beautiful is elliptical. It has simplicity and constant 
change. It cannot be described by a compass, and it changes direction at every one of its points.”

Rudolf Arnheim
Leonardo da Vinci, Raphael, Michelangelo, Albrecht Dürer, M.C. Escher, Hans Holbein, Paul Klee, 
LeRoy Neiman. All of these famous artists were left handed.

Our Robots have been spending some time researching the great artists from the Human civilization 
and would like to learn some of the fundamentals of art. For their first lesson, they need to learn 
to control their left hand-manipulators well enough to make smooth motions. For this exercise, they 
have decided to draw various figures on graph paper with an extra challenge rule -- don't lift your pen.

A figure is represented as a set of segments in the rectangular coordinate system. Each segment is 
represented as a sequence of 4 numbers: (x1, y1, x2, y2), where x1, y1 are coordinates for the first 
end and x2, y2 -- for the second. Segments are undirected. All points in a figure are connected, so 
you can reach each point from any point.

You should find a path in order to draw the figure. You can pass through each segment only once and 
are not allowed to lift the pen. The result must be represented as a sequence of points (tuples with 
coordinates) in the order of how the pen moves to create the drawing. The path may be started and ended 
at any point. If it's impossible to draw a figure then return an empty sequence. Let's look at some examples:

figures
Example 1: the figure is represented as {(1,2,1,5),(1,2,7,2),(1,5,4,7),(4,7,7,5)} and can be two path 
- ((7,2),(1,2),(1,5),(4,7),(7,5)) or ((7,5),(4,7),(1,5),(1,2),(7,2)).
Example 2: the figure {(1,2,1,5),(1,2,7,2),(1,5,4,7),(4,7,7,5),(7,5,7,2),(1,5,7,2),(7,5,1,2)} can not 
be drawn with the given rules, so the result is an empty list or tuple.
Example 3: it's like fig.2 but with one more segment (1,5,7,5) and can be drawn several ways. One of 
them ((7,2),(1,2),(1,5),(4,7),(7,5),(7,2),(1,5),(7,5),(1,2)).

Input: Figure segments as a set of tuples with 4 integers each.

Output: The path as a list or tuple of tuples with 2 integers each.

Example:

draw({(1,2,1,5),(1,2,7,2),(1,5,4,7),(4,7,7,5)}) == ((7,2),(1,2),(1,5),(4,7),(7,5))
draw({(1,2,1,5),(1,2,7,2),(1,5,4,7),(4,7,7,5),(7,5,7,2),(1,5,7,2),(7,5,1,2)}) == []
draw({(1,2,1,5),(1,2,7,2),(1,5,4,7),(4,7,7,5),(7,5,7,2),(1,5,7,2),(7,5,1,2),(1,5,7,5)}) == 
((7,2),(1,2),(1,5),(4,7),(7,5),(7,2),(1,5),(7,5),(1,2))

How it is used: This mission illustrates the basics of computer generated vector graphics. 
The same principles may also be applied to AI pathfinding and topological work.

Precondition:
0 < len(segments) < 30
all(all(0 < x < 100 for x in s) for s in segments)

“描述美丽的线条是椭圆形的。它具有简单性和不变性
更改。它不能用罗盘来描述，它会在每一点上改变方向。“

鲁道夫阿恩海姆
达芬奇，拉斐尔，米开朗基罗，阿尔布雷希特丢勒，M.C.埃舍尔，汉斯霍尔拜因，保罗克利，
LeRoy Neiman。所有这些着名的艺术家都是左撇子。

我们的机器人花费了一些时间研究人类文明中伟大的艺术家
并想了解一些艺术的基础知识。为了第一课，他们需要学习
控制他们的左手操纵器足够好，以使运动平稳。对于这个练习，他们
已决定在方格纸上绘制各种图形，并附带额外的挑战规则 - 请勿抬起笔。

一个图形表示为直角坐标系中的一组线段。每个细分是
表示为4个数字的序列：（x1，y1，x2，y2），其中x1，y1是第一个
结束和x2，y2 - 为第二。细分是无向的。图中的所有点都是连通的，所以
你可以从任何点到达每个点。

你应该找到一条路径来绘制图形。您只能传递一次和每个细分
不允许抬起笔。结果必须表示为一系列的点（带有的元组）
坐标）按笔的移动顺序创建绘图的顺序。路径可能会启动并结束
在任何时候。如果无法绘制数字，则返回空序列。我们来看一些例子：

人物
例1：该数字表示为{（1,2,1,5），（1,2,7,2），（1,5,4,7），（4,7,7,5）}和可以是两条路径
- （（7,2），（1,2），（1,5），（4,7），（7,5））或（（7,5），（4,7），（1,5 ），（1,2），（7,2））。
例2：图{（1,2,1,5），（1,2,7,2），（1,5,4,7），（4,7,7,5），（7,5 ，7,2），（1,5,7,2），（7,5,1,2）}不能
用给定的规则绘制，结果是一个空列表或元组。
示例3：它与图2相似，但具有多个段（1,5,7,5），可以通过多种方式绘制。之一
（7,2），（1,2），（1,5），（4,7），（7,5），（7,2），（1,5），（7,5）， （1,2））。

输入：图分段为一组元组，每个元组都有4个整数。
输出：将路径作为每个具有2个整数的元组的列表或元组的元组。


它是如何使用的：这个任务演示了计算机生成的矢量图形的基础知识。
AI路径查找和拓扑工作也可以应用相同的原理。

前提：
0 <len（段）<30
全部（全部（对于x，s中的0 <x <100）分段中的s）
'''

def draw(segments):
    return []


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    def checker(func, in_data, is_possible=True):
        user_result = func(in_data)
        if not is_possible:
            if user_result:
                print("How did you draw this?")
                return False
            else:
                return True
        if len(user_result) < 2:
            print("More points please.")
            return False
        data = list(in_data)
        for i in range(len(user_result) - 1):
            f, s = user_result[i], user_result[i + 1]
            if (f + s) in data:
                data.remove(f + s)
            elif (s + f) in data:
                data.remove(s + f)
            else:
                print("The wrong segment {}.".format(f + s))
                return False
        if data:
            print("You forgot about {}.".format(data[0]))
            return False
        return True

    assert checker(draw,
                   {(1, 2, 1, 5), (1, 2, 7, 2), (1, 5, 4, 7), (4, 7, 7, 5)}), "Example 1"
    assert checker(draw,
                   {(1, 2, 1, 5), (1, 2, 7, 2), (1, 5, 4, 7),
                    (4, 7, 7, 5), (7, 5, 7, 2), (1, 5, 7, 2), (7, 5, 1, 2)},
                   False), "Example 2"
    assert checker(draw,
                   {(1, 2, 1, 5), (1, 2, 7, 2), (1, 5, 4, 7), (4, 7, 7, 5),
                    (7, 5, 7, 2), (1, 5, 7, 2), (7, 5, 1, 2), (1, 5, 7, 5)}), "Example 3"
