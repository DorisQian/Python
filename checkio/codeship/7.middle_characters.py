'''
You are given some string where you need to find its middle characters. The string may contain one word, a few symbols or a whole sentence. If the length of the string is even, then you should return two middle characters, but if the length is odd, return just one. For more details look at the Example.

example

Input: A string.

Output: The middle characters.

Example:

middle('example') == 'm'
middle('test') == 'es'    
middle('very-very long sentence') == 'o'
middle('I') == 'I'
middle('no') == 'no'

How it is used: For work with texts.

Precondition:
1 <= the length of the text <= 100


给你一些字符串，你需要找到它的中间字符。 该字符串可能包含一个词，几个符号或整个句子。 如果字符串的长度是偶数，那么你应该返回两个中间字符，但是如果长度是奇数，只返回一个。 有关更多详细信息，请参阅示例。

例

输入：一个字符串。
输出：中间的字符。
如何使用它：用于处理文本。
'''

def middle(text):
    #replace this for solution
    return text

if __name__ == '__main__':
    print("Example:")
    print(middle('example'))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert middle('example') == 'm'
    assert middle('test') == 'es'    
    assert middle('very-very long sentence') == 'o'
    assert middle('I') == 'I'
    assert middle('no') == 'no'
    print("Coding complete? Click 'Check' to earn cool rewards!")