In this mission your task is to determine the popularity of certain words in the text.

At the input of your function are given 2 arguments: the text and the array of words the popularity of which you need to determine.

When solving this task pay attention to the following points:

The text can consist of multiple lines with punctuation.
The words should be sought in all registers. This means that if you need to find a word "one" then words like "one", "One", "oNe", "ONE" etc. will do.
The search words are always indicated in the lowercase.
If the word wasn’t found even once, it has to be returned in the dictionary with 0 (zero) value.
Input: The text and the search words array.

Output: The dictionary where the search words are the keys and values are the number of times when those words are occurring in a given text.

Example:

popular_words('''
When I was One,
I had just begun.
When I was Two,
I was nearly new.
''', ['i', 'was', 'three']) == {
    'i': 4,
    'was': 3,
    'three': 0
}

在这个任务中，你的任务是确定文本中某些单词的受欢迎程度。
在函数的输入中给出了两个参数:文本和需要确定的单词的受欢迎程度。
在解决这个问题时，要注意以下几点:
该文本可以由多行标点符号组成。
在所有的登记册中都应寻找这些词。这意味着，如果你需要找到一个单词“one”，那么单词“one”，“one”，“one”，“one”等都可以。
搜索词总是用小写字母表示。
如果这个单词没有被找到，它必须在字典中返回0(零)值。
输入:文本和搜索词数组。
输出:字典中搜索词的键值和值是这些单词在给定文本中出现的次数。

def popular_words(text, words):
    # your code here
    return None


if __name__ == '__main__':
    print("Example:")
    print(popular_words('''
When I was One,
I had just begun.
When I was Two,
I was nearly new.
''', ['i', 'was', 'three']))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert popular_words('''
When I was One,
I had just begun.
When I was Two,
I was nearly new.
''', ['i', 'was', 'three']) == {
        'i': 4,
        'was': 3,
        'three': 0
    }
    print("Coding complete? Click 'Check' to earn cool rewards!")

