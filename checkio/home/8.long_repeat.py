"""
There are four substring missions that were born all in one day and you shouldn’t be needed more than one day to solve them. All of those mission can be simply solved by brute force, but is it always the best way to go? (you might not have access to all of those missions yet, but they are going to be available with more opened islands on the map).

This mission is the first one of the series. Here you should find the length of the longest substring that consists of the same letter. For example, line "aaabbcaaaa" contains four substrings with the same letters "aaa", "bb","c" and "aaaa". The last substring is the longest one which makes it an answer.

Input: String.

Output: Int.

Example:

long_repeat('sdsffffse') == 4
long_repeat('ddvvrwwwrggg') == 3

这个任务是这个系列的第一个任务。在这里，您应该找到由同一字母组成的最长子串的长度。
例如，line“aaabbcaaaa”包含四个带有相同字母“aaa”、“bb”、“c”和“aaaa”的子字符串。最后一个子串是最长的一个，它使它成为一个答案。
输入:字符串。
输出:Int。

"""

def long_repeat(line):
    """
        length the longest substring that consists of the same char
    
    num = 0
    for i in set(line):
    	if num < line.count(i):
    		num = line.count(i)
    return num
    """
    num = 0
    l = []
    for i in range(len(line)-1):
        if line[i+1] == line[i]:
            num += 1
            l.append((line[i],num+1))
        else:num = 0
    return(sorted(l,key = lambda x:x[1],reverse = True)[0][1])

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert long_repeat('sdsffffse') == 4, "First"
    assert long_repeat('ddvvrwwwrggg') == 3, "Second"
    assert long_repeat("abababaab") ==2 ,"third"
    print('"Run" is good. How is "Check"?')

