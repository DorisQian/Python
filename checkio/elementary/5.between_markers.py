"""
You are given a string and two markers (the initial and final). You have to find a substring enclosed between these two markers. But there are a few important conditions:

The initial and final markers are always different.
If there is no initial marker then the beginning should be considered as the beginning of a string.
If there is no final marker then the ending should be considered as the ending of a string.
If the initial and final markers are missing then simply return the whole string.
If the final marker is standing in front of the initial one then return an empty string.
Input: Three arguments. All of them are strings. The second and third arguments are the initial and final markers.

Output: A string.

Example:
between_markers('What is >apple<', '>', '<') == 'apple'
between_markers('No[/b] hi', '[b]', '[/b]') == 'No'


给你一个字符串和两个标记（最初和最后）。你必须在这两个标记之间找到一个子串。但是有一些重要的条件：

最初和最后的标记总是不同的。
如果没有初始标记，那么应该将开始视为字符串的开始。
如果没有最后的标记，则结尾应该被认为是字符串的结尾。
如果缺少初始标记和最终标记，则只需返回整个字符串。
如果最后一个标记站在最前面，那么返回一个空字符串。
输入：三个参数。所有这些都是字符串。第二和第三个参数是最初和最后的标记。

输出：一个字符串。


如何使用它： 解析文本

先决条件： 不能超过一个最后的标记，不能超过一个最初的标记

"""
import sys

def between_markers(text: str, begin: str, end: str) -> str:
    """
        returns substring between two given markers
    """

    try:
        begin_index = text.index(begin) + len(begin)
    except ValueError:
        begin_index = 0
    try:
        end_index = text.index(end)
    except ValueError:
        end_index = (len(text) + 1)
    return text[begin_index:end_index]


if __name__ == '__main__':
    print(between_markers('No[/b] hi', '[b]', '[/b]'))

    # These "asserts" are used for self-checking and not for testing
    assert between_markers('What is >apple<', '>', '<') == "apple", "One sym"
    assert between_markers("<head><title>My new site</title></head>",
                           "<title>", "</title>") == "My new site", "HTML"
    assert between_markers('No[/b] hi', '[b]', '[/b]') == 'No', 'No opened'
    assert between_markers('No [b]hi', '[b]', '[/b]') == 'hi', 'No close'
    assert between_markers('No hi', '[b]', '[/b]') == 'No hi', 'No markers at all'
    assert between_markers('No <hi>', '>', '<') == '', 'Wrong direction'
    # assert between_markers('yes') == 'yes', 'wrong'
