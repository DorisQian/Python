"""
Let's continue examining words. You are given two string with words separated by commas. Try to find what is common between these strings. The words are not repeated in the same string.

Your function should find all of the words that appear in both strings. The result must be represented as a string of words separated by commas in alphabetic order.

Input: Two arguments as strings.

Output: The common words as a string.

Example:

checkio("hello,world", "hello,earth") == "hello"
checkio("one,two,three", "four,five,six") == ""
checkio("one,two,three", "four,five,one,two,six,three") == "one,three,two"

How it is used: Here you can learn how to work with strings and sets. This knowledge can be useful for linguistic analysis.

Precondition: 
Each string contains no more than 10 words.
All words separated by commas.
All words consist of lowercase latin letters.

我们继续检查单词。用逗号分隔的单词给你两个字符串。试着找出这些字符串之间的共同点。在同一字符串中没有重复这些单词。
您的函数应该找到所有出现在两个字符串中的单词。结果必须以字母顺序的逗号分隔的字符串表示。

输入:两个参数作为字符串。
输出:普通单词作为字符串。

如何使用:在这里您可以学习如何使用字符串和集。这些知识对语言分析很有用。
先决条件:
每个字符串包含不超过10个单词。
所有的单词都用逗号隔开。
所有单词由小写的拉丁字母组成。
"""
def checkio(first, second):
    return ""

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio("hello,world", "hello,earth") == "hello", "Hello"
    assert checkio("one,two,three", "four,five,six") == "", "Too different"
    assert checkio("one,two,three", "four,five,one,two,six,three") == "one,three,two", "1 2 3"