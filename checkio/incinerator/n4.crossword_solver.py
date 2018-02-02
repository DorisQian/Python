'''
“Looking at the sky, he suddenly saw that it had become black. Then white 
again, but with great rippling circles. The circles were vultures wheeling 
around the sun. The vultures disappeared, to be replaced by checkers squares 
ready to be played on. On the board, the pieces moved around incredibly rapidly, 
winning dozens of games every minute. They were scarcely lined up before they 
started rushing at each other again, banging into each other, forming fighting 
combinations, wiping the other side out in the wink of an eye. Then the squares 
scattered, giving way to the grille of a crossword puzzle, and here, too, words 
flashed, drove each other away, clustered, were erased. They were all very long 
words, like Catalepsy, Thunderbird, Superrequeteriquísímo and Anticonstitutionally.” 
― Jean-Marie G. Le Clézio, The Book of Flights

A crossword is a word puzzle that normally takes the form of a square or a rectangular 
grid of white and black shaded squares. The goal is to fill the white squares with 
letters, forming words or phrases, by solving clues which lead to the answers. In 
languages that are written left-to-right, the answer words and phrases are placed 
in the grid from left to right and from top to bottom. The shaded squares are used 
to separate the words or phrases.

We will solve a few crosswords which have a lattice-like structure, with a higher 
percentage of shaded squares, leaving up to half the letters in an answer unchecked. 
For example, if the top row has an answer running all the way across, there will be 
no across answers in the second row. Your program receives a crossword pattern without 
clues and numbers, and it should determine word positions itself with the following rules:
- If a cell is placed in the most left column or neighbour left cell is shaded, and the 
neighbouring right cell is empty, then this cell is the beginning of left-to-right word;
- If a cell is placed in the top row or the neighbouring upward cell is shaded, and 
neighbour down cell is empty, then this cell is the beginning of up-to-down word.
All words have a length greater than or equal to 3 letters. All empty cells should filled in.

You are given a crossword as a sequence of strings, where "X" is a shaded cell and "." 
is an empty cell. You are also given the predefined list of words in lowercase. (You can 
find it here or in the default code). This list is the same for all crosswords and 
contains about 1500 nouns. You should use only the given words.

You don't need to find all of the possible solutions. It will be enough to find any 
solution which fills the crossword puzzle and contains the correct words.

crossword

Input: Two arguments. A crossword as a tuple of strings and the words as a tuple of strings.

Output: Any solved variant of the crossword as a tuple/list of strings.

Example:

solver(('.XXX.', '...X.', '.X.X.', '.....'))
How it is used: This is a classic constraint satisfaction problem and can save you time 
with the daily crosswords.

Precondition:
3 < len(crossword) ≤ 10
all(3 < len(row) ≤ 10 and len(row) == len(crossword[0]) for row in crossword)

“望着天空，他突然看到它变成了黑色。然后白色
再一次，但是波澜壮阔的圈子。这些圈子是秃鹫
在太阳附近。秃鹰消失了，被方格棋子取代
准备好被播放。在棋盘上，棋子移动得非常快，
每分钟赢得几十场比赛。他们之前几乎没有排队
又开始互相冲撞，互相冲撞，形成了战斗
在眨眼之间擦拭另一面。然后广场
散开，让位于纵横字谜的格栅，这里也是文字
闪烁，相互驱赶，聚集，被抹去。他们都很长
词，如僵尸，雷鸟，Superrequeteriquísímo和Anticonstitutionally。
- Jean-Marie G. LeClézio，The Book of Flights

填字游戏是一个字拼图，通常采取正方形或矩形的形式
网格的白色和黑色阴影正方形。目标是填补白色方块
通过解决导致答案的线索来形成单词或短语。在
从左到右书写的语言，回答词和短语被放置
在网格中从左到右，从上到下。使用阴影正方形
分开单词或短语。

我们将解决一些格子状结构的一些较高的填字
阴影正方形的百分比，留下一半答案未选中的字母。
例如，如果最上面的一行有答案，那么就会有
没有在第二行的答案。您的程序没有收到填字游戏模式
线索和数字，而且应该按照以下规则自行确定单词的位置：
- 如果一个单元格被放置在最左边的列中，或者邻居左边的单元格被遮蔽了，那么
相邻的右边单元格是空的，那么这个单元格是从左到右的单词的开始;
- 如果一个单元格放置在最上面一行或者相邻的向上单元格被遮蔽，
邻居下行单元是空的，那么这个单元就是从上到下的单词的开始。
所有单词的长度大于或等于3个字母。所有空单元格都应填入。

给你一个字符串作为一串字符串，其中“X”是一个阴影单元格和“。”。
是一个空的单元格。您还可以以小写形式给出预定义的单词列表。 （您可以
在这里或在默认代码中找到它）。这个列表是相同的所有填字游戏和
包含约1500个名词。你应该只使用给定的单词。

你不需要找到所有可能的解决方案。这将足以找到任何
解决方案，填补纵横字谜和包含正确的话。

填字游戏

输入：两个参数。纵横字谜作为字符串的元组，字作为字符串的元组。

输出：作为字符串的元组/字符串的任何已解决的填字的变体。

如何使用：这是一个经典的约束满足问题，可以节省您的时间
与日常的填字游戏。
'''