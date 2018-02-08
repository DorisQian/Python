'''
"We must burn the house down!" said the Rabbit's voice; and Alice called out as loud as she could, "If you do. I'll set Dinah at you!"

There was a dead silence instantly, and Alice thought to herself, "I wonder what they WILL do next! If they had any sense, they'd take the roof off." After a minute or two, they began moving about again, and Alice heard the Rabbit say, "A barrowful will do, to begin with."

"A barrowful of WHAT? thought Alice; but she had not long to doubt, for the next moment a shower of little pebbles came rattling in at the window, and some of them hit her in the face. "Ill put a stop to this, she said to herself, and shouted out, "You'd better not do that again! which produced another dead silence.

Alice noticed with some surprise that the pebbles were all turning into little cakes as they lay on the floor, and a bright idea came into her head. "If I eat one of these cakes, she thought, "its sure to make SOME change in my size; and as it cant possibly make me larger, it must make me smaller, I suppose.

"Alice's adventures in wonderland." Lewis Carroll
Someone has decided to bake a load of cakes and place them on the floor. Our robots can't help but try to find a pattern behind the cakes' disposition. Some cakes form rows, we want to count these rows. A row is a sequence of three or more cakes if we can draw a straight line through its centers. The greater row takes up the smaller rows. So if we have a row with 4 cakes, then we have only one row (not 4 by 3).

The cake locations are represented as a list of coordinates. A coordinate is a list of two integers. You should count the rows.

example
Input: Сoordinates as a list of lists with two integers.

Output: The quantity of rows as an integer.

Example:

checkio([[3, 3], [5, 5], [8, 8], [2, 8], [8, 2]]) == 2
checkio([[2, 2], [2, 5], [2, 8], [5, 2], [7, 2], [8, 2], [9, 2], [4, 5], [4, 8], [7, 5], [5, 8], [9, 8]]) == 6

How it is used: This is an example of the image and pattern recognition. This concept can be useful for the game mechanics or if you want to write a bot for games, or when transposing printed text to a digital format.

Precondition: 0 < |coordinates| < 20
∀ x,y ∈ coordinates : 0 ≤ x,y ≤ 10

“我们必须把房子烧掉！”说兔子的声音;爱丽丝尽可能大声地叫了起来，“如果你这样做，我会把黛娜送给你！”

沉默了一瞬间，爱丽丝心想：“我想知道他们接下来会做什么，如果他们有任何意义的话，他们会把屋顶关掉。过了一两分钟，他们又开始往前走了，爱丽丝听到兔子说：“一开始就会有一个可行的办法。”

“什么？”爱丽丝想了想，但是她还没有怀疑，下一刻，一阵小小的鹅卵石在窗口咔哒咔哒地响了起来，有的还打在了她的脸上。她自言自语地大声说：“你最好不要再那样做了，这又产生了一个沉默的沉默。

“爱丽丝惊讶地发现，当他们躺在地上的时候，鹅卵石都变成了小蛋糕，一个聪明的想法进入了她的脑海。 “如果我吃这些蛋糕之一，她想：”它肯定会让我的身材有所改变。而且由于它不可能让我变大，所以我认为这一定会让我变小。

“爱丽丝梦游仙境”刘易斯·卡罗尔
有人决定烤一堆蛋糕，然后放在地板上。我们的机器人不能不试图找到蛋糕背后的模式。一些蛋糕形成行，我们要计数这些行。如果我们可以通过它的中心绘制一条直线，那么一排是三个或更多的蛋糕。较大的行占用较小的行。所以如果我们有一排四块蛋糕，那么我们只有一排（而不是4×3）。

蛋糕的位置表示为一个坐标列表。坐标是两个整数的列表。你应该统计行数。

输入：СOordinates作为列表与两个整数列表。
输出：整数的行数。

如何使用：这是一个图像和模式识别的例子。这个概念可以用于游戏机制，或者如果你想写一个游戏机器人，或者将打印的文本转换为数字格式。
'''


def checkio(cakes):
    return 0

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio([[3, 3], [5, 5], [8, 8], [2, 8], [8, 2]]) == 2
    assert checkio(
        [[2, 2], [2, 5], [2, 8], [5, 2], [7, 2], [8, 2],
         [9, 2], [4, 5], [4, 8], [7, 5], [5, 8], [9, 8]]) == 6