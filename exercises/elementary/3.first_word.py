"""
You are given a string where you have to find its first word.

When solving a task pay attention to the following points:

There can be dots and commas in a string.
A string can start with a letter or, for example, a dot or space.
A word can contain an apostrophe and it's a part of a word.
The whole text can be represented with one word and that's it.
Input: A string.

Output: A string.
Example:

first_word("Hello world") == "Hello"
first_word("greetings, friends") == "greetings"

How it is used: the first word is a command in a command line
它是如何使用的： 第一个单词是命令行中的命令

Precondition: the text can contain a-z A-Z , . '

给你一个字符串，你必须找到它的第一个字。

解决任务时要注意以下几点：

字符串中可以有点和逗号。
一个字符串可以以一个字母开头，例如一个点或空格。
一个词可以包含一个撇号，它是一个词的一部分。
整个文本可以用一个词表示，就是这样。
"""


def first_word(text: str) -> str:
    """
        returns the first word in a given text.
    """
    if text[0] == '.':
        text1 = text.strip('.')
    elif text[0] == ',':
        text1 = text.strip(',')
    else: text1 = text
    if '.' in text1:
        text = text1.strip().split('.')
    elif ',' in text1:
        text = text1.strip().split(',')
    else:
        text = text1.strip().split()
    return text[0]


if __name__ == '__main__':
    print(first_word("Hello world"))
    print(first_word("greetings, friends"))
    print(first_word("... and so on ..."))
    # These "asserts" are used for self-checking and not for an auto-testing
    assert first_word("Hello world") == "Hello"
    assert first_word(" a word ") == "a"
    assert first_word("don't touch it") == "don't"
    assert first_word("greetings, friends") == "greetings"
    assert first_word("... and so on ...") == "and"
    assert first_word("hi") == "hi"

