'''
You have been given two anagrams as a string, separated by dash. You need 
to rearrange the letters to turn the first word into the second. The tools 
you have for this mission are two stacks and a one-letter buffer. The first 
stack is the beginning of a word; the second stack is where you will put the 
anagram. The word is placed in the stack, letter by letter. The first letter 
of the anagram is placed in the bottom stack and the last letter in the middle 
stack, until it is needed as the end of the anagram. You need to return the 
shortest sequence of actions to move and turn the word in the first stack into 
the anagram in the second. The first stack is labeled 1, the second is labeled 2, 
and the buffer as 0. The action is written as a string of two numbers which signify 
the original location of the letter and the new location. For example: 12 means that 
from the first stack, we take the last letter and place it at the end of the second 
stack. For the result, you need to get a string that lists the steps, separated by commas.

anagrams_by_stacks
Input: Two words separated by dash as a string.

Output: A sequence of actions as a string.

Example:

checkio("rice-cire") == "10,12,12,12,02"
checkio("tort-trot") == "12,12,12,12"
checkio("hello-holle") == "12,12,12,12,10,21,21,21,21,02,12,12,12,12"
checkio("anagram-mragana") == "12,10,12,02,12,12,12,12"
checkio("mirror-mirorr") == "12,12,10,12,12,02,10,21,21,21,21,21,02,12,12,12,10,21,21,21,02,12,12,12,12"
#It can be solved more the one way.

How it is used: Here you can play with stacks and how they work in games. We see stacks 
in everyday life, they’re in the books in our library, and the blank sheets of paper in our printer tray.

Precondition: 1 ≤ |word| < 10
Words contains only ASCII letters in lowercase.

你被赋予了两个字符串，用短划线分开。你需要
重新排列字母把第一个字变成第二个字。工具
你有这个任务是两个堆栈和一个字母的缓冲区。首先
堆栈是一个词的开始;第二个堆栈是你将放置的地方
字谜。这个词是一字排开的。第一个字母
的字谜被放置在底部堆栈中，最后一个字母在中间
直到需要作为字谜的结尾。你需要返回
移动最短的动作序列并将第一个栈中的单词转换为
在第二个字谜。第一个堆栈标记为1，第二个标记为2，
和缓冲区为0.该行动被写为一个两个数字的字符串表示
信件的原始位置和新的位置。例如：12意味着
从第一个堆栈中，我们把最后一个字母放在第二个字符的末尾
叠加。对于结果，您需要获取一个字符串列出的步骤，用逗号分隔。

anagrams_by_stacks
输入：用短划线分隔的两个单词作为字符串。

输出：作为字符串的一系列操作。

＃它可以更多地解决这个问题。

如何使用：在这里你可以玩堆栈，以及他们如何在游戏中工作。我们看到堆栈
在日常生活中，它们在我们图书馆的书籍中，以及我们的打印机托盘中的空白纸张上。
'''
