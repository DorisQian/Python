"""
There are four substring missions that were born all in one day and you shouldn’t be needed 
more than one day to solve them. All of those mission can be simply solved by brute force, 
but is it always the best way to go? (you might not have access to all of those missions yet, 
but they are going to be available with more opened islands on the map).

This is the third mission of the series, and it’s the only one where you have to return not 
a substring but a substring length. You need to find a substring that repeats more than once 
in a given string. This reiteration shouldn't have overlaps. For example, in a string "abcab" 
the longest substring that repeats more than once is "ab", so the answer should be 2 (length of "ab")

Input: String.

Output: Int.

Example:

double_substring('aaaa') == 2
double_substring('abc') == 0
double_substring('aghtfghkofgh') == 3 # fgh

有四个子串任务都是在一天之内出生的，你不应该有超过一天的时间来解决它们。所有这些任务都可以
用蛮力来解决，但它总是最好的方法吗?(你可能无法访问所有这些任务，但它们将在地图上更开放的岛屿上可用)。
这是本系列的第三个任务，它是唯一一个必须返回非子字符串，而只能返回子字符串长度的任务。您需要
找到一个在给定字符串中重复多次的子字符串。这种重复不应该重叠。例如，在一个字符串“abcab”中，
最长的子字符串会重复多次，所以答案应该是2(“ab”的长度)
"""

def double_substring(line):

    if len(line) <= 3:
        return 0
    else:
        sub = len(line) // 2
        while sub:
            #print(sub)
            for i in range(len(line) - sub):
                substring = line[i: i + sub]
                if line.count(substring) > 1:
                    print(substring)
                    return sub
            sub -= 1
        return 0
        '''
        for i in range(len(line) -1):
            substring = line[i] + line[i+1]
            sums = line.count(substring)
            num = max(num, sums)
        return num
        '''


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert double_substring('aaaa') == 2, "First"
    assert double_substring('abc') == 0, "Second"
    assert double_substring('aghtfghkofgh') == 3, "Third"
    assert double_substring("abababaab") == 3, "forth"
    print('"Run" is good. How is "Check"?')
