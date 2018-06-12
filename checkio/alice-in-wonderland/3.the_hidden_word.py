'''
JABBERWOCKY
'Twas brillig, and the slithy toves
Did gyre and gimble in the wabe;
All mimsy were the borogoves,
And the mome raths outgrabe.

'Beware the Jabberwock, my son!
The jaws that bite, the claws that catch!
Beware the Jubjub bird, and shun
The frumious Bandersnatch!'

He took his vorpal sword in hand:
Long time the manxome foe he sought--
So rested he by the Tumtum tree,
And stood awhile in thought.

And as in uffish thought he stood,
The Jabberwock, with eyes of flame,
Came whiffling through the tulgey wood,
And burbled as it came!

One, two! One, two! And through and through
The vorpal blade went snicker-snack!
He left it dead, and with its head
He went galumphing back.

'And hast thou slain the Jabberwock?
Come to my arms, my beamish boy!
O frabjous day! Callooh! Callay!'
He chortled in his joy.

'Twas brillig, and the slithy toves
Did gyre and gimble in the wabe;
All mimsy were the borogoves,
And the mome raths outgrabe.

"Through the Looking-Glass." Lewis Carroll

DREAMING of apples on a wall,
And dreaming often, dear,
I dreamed that, if I counted all,
-How many would appear?

"Puzzles from Wonderland." Lewis Carroll

Nicola has solved this puzzle (and I am sure that you will do equally well). 
To be prepared for more such puzzles, Nicola wants to invent a method to search 
for words inside poetry. You can help him create a function to search for certain words.

You are given a rhyme (a multiline string), in which lines are separated by 
"newline" (\n). Casing does not matter for your search, but whitespaces should 
be removed before your search. You should find the word inside the rhyme in the 
horizontal (from left to right) or vertical (from up to down) lines. For this you 
need envision the rhyme as a matrix (2D array). Find the coordinates of the word 
in the cut rhyme (without whitespaces).

The result must be represented as a list -- [row_start,column_start,row_end,column_end], where

row_start is the line number for the first letter of the word.
column_start is the column number for the first letter of the word.
row_end is the line number for the last letter of the word.
column_end is the column number for the last letter of the word.
Counting of the rows and columns start from 1.
rhymes
Input: Two arguments. A rhyme as a string and a word as a string (lowercase).

Output: The coordinates of the word.

Example:

checkio(u"""DREAMING of apples on a wall,
And dreaming often, dear,
I dreamed that, if I counted all,
-How many would appear?""", u"ten") == [2, 14, 2, 16]
checkio("""He took his vorpal sword in hand:
Long time the manxome foe he sought--
So rested he by the Tumtum tree,
And stood awhile in thought.
And as in uffish thought he stood,
The Jabberwock, with eyes of flame,
Came whiffling through the tulgey wood,
And burbled as it came!""", "noir") == [4, 16, 7, 16]
    
How it is used: This task shows the variance of the positional ciphers. With this cipher you can 
hide a message within a book which allows you and receiver to send these coded messages.

Precondition: The word is given in lowercase
0 < |word| < 10
0 < |rhyme| < 300

JABBERWOCKY
“Twas brillig，还有那个傻子
在摇篮里有回旋和灵活的东西;
所有的模仿是borogoves，
而这个女人也是一个匪夷所思的人物。

“小心Jabberwock，我的儿子！
咬的爪子，抓的爪子！
当心那只Jubjub鸟，然后顺着
这个肮脏的Bandersnatch！

他拿着手中的刀剑：
很长一段时间他所寻求的手段 - 
因此，他在Tumtum树休息，
沉思了一会儿。

就在他站起来的时候，
Jabberwock有着火焰的眼睛，
通过tulgey木头来到，
当它来到时，它就会咕咕叫！

一二！一二！并贯穿始终
vorpal刀片去snicker小吃！
他把它丢了，头也死了
他跑回去了。

“你是不是杀了Jabberwock？
来到我的怀里，我的束缚的男孩！
O frabjous的一天！ Callooh！ Callay！”
他高兴地哼了一声。

“Twas brillig，还有那个傻子
在摇篮里有回旋和灵活的东西;
所有的模仿是borogoves，
而这个女人也是一个匪夷所思的人物。

“通过镜子”。刘易斯·卡罗尔

梦见墙上的苹果，
经常做梦，亲爱的，
我梦见，如果我算了一切，
- 会出现多少？

“仙境的困惑”刘易斯·卡罗尔

尼古拉已经解决了这个难题（我相信你会同样做得很好）。为了准备更多这样的谜题，尼古拉想要发明一种
方法来搜索诗歌里面的单词。你可以帮助他创建一个功能来搜索某些单词。

给你一个韵（多行字符串），其中行由“换行符”（\ n）分隔。你的搜索没有关系，但在搜索之前，
空格应该被删除。你应该在水平方向（从左到右）或垂直方向（从上到下）找到韵文中的单词。为此，
你需要将韵看成一个矩阵（二维数组）。在切韵中找出单词的坐标（没有空格）。

结果必须表示为一个列表 - [row_start，column_start，row_end，column_end]，其中

row_start是单词首字母的行号。
column_start是单词首字母的列号。
row_end是单词最后一个字母的行号。
column_end是单词最后一个字母的列号。
计数行和列从1开始。
童谣
输入：两个参数。押韵作为一个字符串和一个字作为一个字符串（小写）。
输出：单词的坐标。
如何使用：此任务显示位置密码的差异。有了这个密码，你可以在一本书中隐藏一条消息，允许你和接收者发送这些编码消息。
'''


def checkio(text, word):
    text_list = text.split('\n')
    text_new = []
    for i in text_list:
    	text = i.split(' ')
    	n_text = ''
    	for j in text:
    		n_text += j
    	text_new.append(n_text)
    #print(text_new)
    result = []
    for k in text_new:
    	if word in k:
    		result.append(text_new.index(k) + 1)
    		result.append(k.index(word) + 1)
    		result.append(text_new.index(k) + 1)
    		result.append(k.index(word) + len(word))
    		return result
   	
    reverse_list = []
    long_len = [len(row) for row in text_new]
    leng = max(long_len)
    for i in range(len(text_new)):
    	flag = len(text_new[i])
    	while flag < leng:
    		text_new[i] += ' '
    		flag += 1
    #print(text_new)
    for index in range(leng):
    	new_row = ''
    	for text_row in text_new:
    		new_row += text_row[index]
    	reverse_list.append(new_row)

    result = []
    for k in reverse_list:
    	if word in k:
    		result.append(k.index(word) + 1)
    		result.append(reverse_list.index(k) + 1)
    		result.append(k.index(word) + len(word))
    		result.append(reverse_list.index(k) + 1)
    		print(result)
    		return result
#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio("""DREAMING of apples on a wall,
And dreaming often, dear,
I dreamed that, if I counted all,
-How many would appear?""", "ten") == [2, 14, 2, 16]
    assert checkio("""He took his vorpal sword in hand:
Long time the manxome foe he sought--
So rested he by the Tumtum tree,
And stood awhile in thought.
And as in uffish thought he stood,
The Jabberwock, with eyes of flame,
Came whiffling through the tulgey wood,
And burbled as it came!""", "noir") == [4, 16, 7, 16]