"""
There are four substring missions that were born all in one day and you shouldn’t be needed more than one day to solve them. All of those mission can be simply solved by brute force, but is it always the best way to go? (you might not have access to all of those missions yet, but they are going to be available with more opened islands on the map).

This mission is the first one of the series. Here you should find the length of the longest substring that consists of the same letter. For example, line "aaabbcaaaa" contains four substrings with the same letters "aaa", "bb","c" and "aaaa". The last substring is the longest one which makes it an answer.

Input: String.

Output: Int.

Example:

long_repeat('sdsffffse') == 4
long_repeat('ddvvrwwwrggg') == 3

有四个子串任务都是在一天之内出生的，你不应该有超过一天的时间来解决它们。所有这些任务都可以用蛮力来解决，但它总是最好的方法吗?(你可能无法访问所有这些任务，但它们将在地图上更开放的岛屿上可用)。
这个任务是这个系列的第一个任务。在这里，您应该找到由同一字母组成的最长子串的长度。例如，line“aaabbcaaaa”包含四个带有相同字母“aaa”、“bb”、“c”和“aaaa”的子字符串。最后一个子串是最长的一个，它使它成为一个答案。
输入:字符串。
输出:Int。

"""

def long_repeat(line):
    """
        length the longest substring that consists of the same char
    """
    # your code here
    return 0

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert long_repeat('sdsffffse') == 4, "First"
    assert long_repeat('ddvvrwwwrggg') == 3, "Second"
    print('"Run" is good. How is "Check"?')

