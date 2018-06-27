'''
Lets cow say!
Our cow is young and can only say some of the words we teach it. Not only does it talk, 
but this cow can turn into the famous Tux (wiki/Cowsay) if we ask it nicely.

You are given some text and your function should format it in the "cows" speech. Let's 
examine the rules for this problem:
The cow is always the same, only quote changes.
Multiple spaces in a row are replaced by one space.
The top border consists of underscore characters. It starts from a single space and ends 
before the border column.
Each line of the quote consists of these parts: quote border(1), space(1), line(1-39), 
space(1), quote border(1).
If line is less than 40 characters, it will fit into one string. The string is quoted in <>.
If the line is greater than or equal to 40 characters, it should be split by these rules:
Max line size is 39 chars. If any spaces are in the line, split it by the rightmost space 
(this space is removed from text) otherwise take the first 39 characters.
After the split align all lines to same length by adding spaces at the end of each line.
First line borders: /\
Middle line borders: ||
Last line borders: \/
The bottom border consists of the minus sign. Has same length as top.
cowsay console program has strange behavior in certain cases, this cases will not be tested here.
     _________________________________
    / Dog goes woof                   \
    | Cat goes meow                   |
    | Bird goes tweet                 |
    | And mouse goes squeek           |
    | Cow goes moo                    |
    | Duck goes quack                 |
    \ And the solution will go to you /
     ---------------------------------
            \   ^__^
             \  (oo)\_______
                (__)\       )\/\
                    ||----w |
                    ||     ||
    
What does the cow say?

Input: Text as a string.

Output: The result for the console as a string.

Hint: Read python docs (2.7, 3.3) about formatting styles (str.format and %). Notice for r before 
the string. It is a raw string and they use different rules for interpreting backslash escape sequences.

How it is used: The original Cowsays are written in the Perl programming language, and as such are easily adaptable to system tasks in Unix. They can perform functions such as telling users their home directories are full, that they have new mail, etc. Now you will write your own realisation for this classic unix program. This concept can teach you how to prepare and format text for the console output.

Precondition: 0 < len(text) < 858;
text can't consist of spaces only;
text contains only ASCII letters, digits and punctuation.

让牛说！
我们的牛年轻，只能说一些我们教它的话。它不仅会说话，
但如果我们问得好，这头牛可以变成着名的Tux（wiki / Cowsay）。

给你一些文本，你的函数应该在“奶牛”的演讲中进行格式化。让我们
检查这个问题的规则：
牛总是一样的，只是报价有变化。
一行中的多个空格被一个空格替换。
顶部边框由下划线字符组成。它从一个空间开始并结束
在边界栏之前。
报价的每一行由以下部分组成：报价边界（1），空间（1），行（1-39），
空格（1），引用边界（1）。
如果行少于40个字符，它将适合一个字符串。该字符串在<>中引用。
如果该行大于或等于40个字符，则应按以下规则拆分：
最大行数是39个字符。如果有任何空格在该行中，请将其分割为最右侧的空格
（这个空间从文本中删除），否则取前39个字符。
分割后，通过在每行末尾添加空格将所有行对齐到相同的长度。
第一行边界：/ \
中线边界：||
最后一行边框：\ /
底部边框由减号组成。长度与顶部相同。
Cowsay控制台程序在某些情况下有奇怪的行为，这种情况在这里不会被测试。
     _________________________________
    /狗去woof \
    |猫去喵|
    |鸟去tweet |
    |然后鼠标就会吱吱作响
    |牛去moo |
    |鸭去嘎嘎|
    \解决方案将发给你/
     ---------------------------------
            \ ^ __ ^
             \（oo）\ _______
                （__）\）\ / \
                    || ---- w |
                    || ||
    
牛说什么？

输入：文本为字符串。

输出：控制台的结果作为字符串。

提示：阅读关于格式化样式（str.format和％）的python文档（2.7,3.3）。注意r之前
字符串。它是一个原始字符串，它们使用不同的规则来解释反斜杠转义序列。

它是如何使用的：最初的Cowsays是用Perl编程语言编写的，因此很容易适应Unix中的系统任务。
他们可以执行诸如告诉用户他们的主目录已满，他们有新邮件等功能。现在您将为这个经典的unix程
序编写自己的实现。这个概念可以教你如何为控制台输出准备和格式化文本。

先决条件：0 <len（text）<858;
文本不能只包含空格;
文本只包含ASCII字母，数字和标点符号。
'''


'''

def cowsay(text):
    length = len(text)
    if length < 40:
        result = ' ' + '_' * (length +2) + '\n' \
                + '< ' + text + ' >' + '\n' \
                + ' ' + '-' * (length+2)  \
                + COW
    else:       
        word = text.split(' ')
        row_list = []
        while len(word):
            len_row = 0
            length = 0
            for w in word:
                length += len(w) + 1
            if length - 1 <= 38:
                row_list.append(' '.join(word))
                word = []
            else:
                row = ''
                for n in word:
                    len_row += len(n) + 1
                    row += n + ' '
                    # word.remove(n)
                    if len_row >= 39:
                        row = row.rstrip(n + ' ')
                        row_list.append(row)
                        for i in range(len(word) - 1):
                            word.pop(i)
                        break

        result = ' ' + '_' * 40 + '\n'
        for i in range(len(row_list)):
            if i == 0:
                result += '/' + ' ' + row_list[i] + ' ' * (39- len(row_list[i])) + '\\' + '\n'
            elif i == len(row_list) - 1:
                result += '\\' + ' ' + row_list[i] + ' ' * (39- len(row_list[i])) + '/' + '\n'
            else:
                result += '|' + ' ' + row_list[i] + ' ' * (38- len(row_list[i])) + '|' + '\n'
        result += ' ' + '-' * 40 + COW

    return result
    #return 'Cow say "%s"' % text
'''
"""
import re
from functools import reduce
 

def cowsay(text):

    lst = re.findall(r'''(?x) (?P<cut> [^\s]{39} ) \s?
                     | (?= ( .{1,39} ) (?: \s | $ ) ) \2 \s?''',
                    re.sub(r'\s+', r' ', text))
    print(re.sub(r'\s+', r' ', text))
    print(lst)
    lst = [ match for el in lst for match in el if match ]
    print(lst)
    just = max(len(s) for s in lst)
    lst = list(map(lambda s: s.ljust(just), lst))
    forms = [ '< {0} >\n' ] if len(lst) == 1 else \
            [ '/ {0} \\\n' ] + [ '| {0} |\n' ]*(len(lst)-2) + ['\\ {0} /\n' ]
    print(forms)
    res = ['\n '+(just+2)*'_'+'\n'] + \
            [fmt.format(el) for (fmt, el) in zip(forms, lst)] + [' '+(just+2)*'-']
    return reduce(lambda acc,v: acc + v, res, '') + COW

"""
import re
COW = r'''
        \   ^__^
         \  (oo)\_______
            (__)\       )\/\
                ||----w |
                ||     ||
'''
TOP = '_'
BOTTOM = '-'
BORDERS = '/\\|'

MAX_ROW = 39


def make_rows(text):
    rows, num = [''], 0
    words = text.split(' ')
    for i, w in enumerate(words):
        # slice words that have over MAX_ROW characters
        if len(w) > MAX_ROW:
            words.insert(words.index(w) + 1, w[MAX_ROW:])
            w = w[:MAX_ROW]
        # if the word is first, don't append row
        if len(rows[num]) + len(w) >= MAX_ROW and i:
            num += 1
            rows.append('')
        rows[num] += w if not rows[num] else ' ' + w
    return rows


def cowsay(text):
    text = re.sub('\s+', ' ', text)
    if len(text) <= MAX_ROW:
        quote = r'''
 {}
< {} >
 {}'''
        width = len(text) + 2
    else:
        quote = r'''
 {}
{}
 {}'''
        rows = make_rows(text)
        width = max(len(x) for x in rows) + 2
        for i, row in enumerate(rows):
            if i == 0:
                rows[i] = ' '.join([BORDERS[0], rows[i].ljust(width - 2), BORDERS[1]])
            elif i == len(rows) - 1:
                rows[i] = ' '.join([BORDERS[1], rows[i].ljust(width - 2), BORDERS[0]])
            else:
                rows[i] = ' '.join([BORDERS[2], rows[i].ljust(width - 2), BORDERS[2]])
        text = '\n'.join(rows)
    return quote.format(TOP * width, text, BOTTOM * width) + COW

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    expected_cowsay_one_line = r'''
 ________________
< Checkio rulezz >
 ----------------
        \   ^__^
         \  (oo)\_______
            (__)\       )\/\
                ||----w |
                ||     ||
'''
    expected_cowsay_two_lines = r'''
 ________________________________________
/ A                                      \
\ longtextwithonlyonespacetofittwolines. /
 ----------------------------------------
        \   ^__^
         \  (oo)\_______
            (__)\       )\/\
                ||----w |
                ||     ||
'''

    expected_cowsay_many_lines = r'''
 _________________________________________
/ Lorem ipsum dolor sit amet, consectetur \
| adipisicing elit, sed do eiusmod tempor |
| incididunt ut labore et dolore magna    |
\ aliqua.                                 /
 -----------------------------------------
        \   ^__^
         \  (oo)\_______
            (__)\       )\/\
                ||----w |
                ||     ||
'''

    cowsay_one_line = cowsay('Checkio rulezz')
    assert cowsay_one_line == expected_cowsay_one_line, 'Wrong answer:\n%s' % cowsay_one_line

    cowsay_two_lines = cowsay('A longtextwithonlyonespacetofittwolines.')
    assert cowsay_two_lines == expected_cowsay_two_lines, 'Wrong answer:\n%s' % cowsay_two_lines

    cowsay_many_lines = cowsay('Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do '
                                'eiusmod tempor incididunt ut labore et dolore magna aliqua.')
    assert cowsay_many_lines == expected_cowsay_many_lines, 'Wrong answer:\n%s' % cowsay_many_lines

