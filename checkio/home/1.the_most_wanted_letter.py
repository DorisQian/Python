"""
You are given a text, which contains different english letters and punctuation symbols. You should find the most frequent letter in the text. The letter returned must be in lower case.
While checking for the most wanted letter, casing does not matter, so for the purpose of your search, "A" == "a". Make sure you do not count punctuation symbols, digits and whitespaces, only letters.

If you have two or more letters with the same frequency, then return the letter which comes first in the latin alphabet. For example -- "one" contains "o", "n", "e" only once for each, thus we choose "e".

Input: A text for analysis as a string.

Output: The most frequent letter in lower case as a string.

Example:

checkio("Hello World!") == "l"
checkio("How do you do?") == "o"
checkio("One") == "e"
checkio("Oops!") == "o"
checkio("AAaooo!!!!") == "a"
checkio("abe") == "a"
How it is used: For most decryption tasks you need to know the frequency of occurrence for various letters in a section of text. For example: we can easily crack a simple addition or substitution cipher if we know the frequency in which letters appear. This is interesting stuff for language experts!

Precondition:
A text contains only ASCII symbols.
0 < len(text) ≤ 105

你得到了一个文本，包含不同的英文字母和标点符号。你应该在课文中找到最频繁的字母。回信必须是小写的。
在检查最需要的字母时，外壳并不重要，因此对于搜索的目的，“A”= =“A”。确保你不计算标点符号，数字和空格，只有字母。

如果你有两个或两个以上相同频率的字母，那就把第一个字母放在拉丁字母中。例如，“one”包含“o”，“n”，“e”只有一次，因此我们选择“e”。

输入:作为字符串的分析文本。

输出:小写字母中最频繁的字母作为字符串。

"""

import re
def checkio(text):

    text = re.search('[a-zA-Z]+', text.replace(' ','')).group(0).lower()
    norepeat = set(text)
    num = 0
    l = [ ]
    for i in norepeat:
        num = text.count(i)
        l.append((i,num))
    return sorted(l,key = lambda x:x[1],reverse = True)[0][0]
    

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio("Hello World!") == "l", "Hello test"
    assert checkio("How do you do?") == "o", "O is most wanted"
    assert checkio("One") == "e", "All letter only once."
    assert checkio("Oops!") == "o", "Don't forget about lower case."
    assert checkio("AAaooo!!!!") == "a", "Only letters."
    assert checkio("abe") == "a", "The First."
    print("Start the long test")
    assert checkio("a" * 9000 + "b" * 1000) == "a", "Long."
    print("The local tests are done.")
