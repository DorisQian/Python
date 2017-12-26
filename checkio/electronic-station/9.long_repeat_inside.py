"""
There are four substring missions that were born all in one day and you shouldn’t be needed more than one day to solve them. All of those mission can be simply solved by brute force, but is it always the best way to go? (you might not have access to all of those missions yet, but they are going to be available with more opened islands on the map).

It is the fourth and the last mission of the series. But if in the first mission you needed to find repeating letters, then in this one you should find a repeating sequence inside the substring. I have an example for you: in a string "abababc" - "ab" is a sequence that repeats more than once, so the answer will be "ababab"

Input: String.

Output: String.

Example:

repeat_inside('aaaaa') == 'aaaaa'
repeat_inside('aabbff') == 'aa'
repeat_inside('aababcc') == 'abab'
repeat_inside('abc') == ''
repeat_inside('abcabcabab') == 'abcabc'

有四个子串任务都是在一天之内出生的，你不应该有超过一天的时间来解决它们。所有这些任务都可以用蛮力来解决，但它总是最好的方法吗?(你可能无法访问所有这些任务，但它们将在地图上更开放的岛屿上可用)。
这是该系列的第四次也是最后一次任务。但是如果在第一个任务中你需要找到重复的字母，那么在这个任务中你应该在子字符串中找到一个重复序列。我给你们举个例子，在一个字符串" abababc" - "ab "是一个重复多次的序列，所以答案是" ababab"


输入:字符串。
输出:字符串。
"""
def repeat_inside(line):
    """
        first the longest repeating substring
    """
    # your code here
    return line

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert repeat_inside('aaaaa') == 'aaaaa', "First"
    assert repeat_inside('aabbff') == 'aa', "Second"
    assert repeat_inside('aababcc') == 'abab', "Third"
    assert repeat_inside('abc') == '', "Forth"
    assert repeat_inside('abcabcabab') == 'abcabc', "Fifth"
    print('"Run" is good. How is "Check"?')