"""
The infinite monkey theorem states that a monkey hitting keys at random on a typewriter keyboard for an infinite
length of time will almost surely type out a given text, such as the complete works of John Wallis, 
or more likely, a Dan Brown novel.

Let's suppose our monkeys are typing, typing and typing, and have produced a wide variety of short text segments. 
Let's try to check them for sensible word inclusions.

You are given some text potentially including sensible words. You should count how many words are included in the 
given text. A word should be whole and may be a part of other word. Text letter case does not matter. 
Words are given in lowercase and don't repeat. If a word appears several times in the text, it should be 
counted only once.

For example, text - "How aresjfhdskfhskd you?", words - ("how", "are", "you", "hello"). The result will be 3.

Input: Two arguments. A text as a string (unicode for py2) and words as a set of strings (unicode for py2).

Output: The number of words in the text as an integer.

Example:

count_words("How aresjfhdskfhskd you?", {"how", "are", "you", "hello"}) == 3
count_words("Bananas, give me bananas!!!", {"banana", "bananas"}) == 2
count_words("Lorem ipsum dolor sit amet, consectetuer adipiscing elit.",
            {"sum", "hamlet", "infinity", "anything"}) == 1

How it is used: Python is a useful and powerful language for text processing. This mission is only a simple
example of the kind of text searching tools you could build.

Precondition:
0 < len(text) ≤ 256
all(3 ≤ len(w) and w.islower() and w.isalpha for w in words)

无限猴子定理指出，猴子在打字机键盘上随意敲击键盘以获得无限
时间的长短几乎肯定会打印出一个给定的文本，如John Wallis的完整作品，
或者更有可能是丹·布朗的小说。

假设我们的猴子在打字、打字和打字，并产生了各种各样的短文本。
让我们来检查一下是否有合理的单词夹杂。

你有一些潜在的文本，包括一些明智的词语。你应该数一下其中包含了多少单词
给定的文本。一个单词应该是完整的，并且可能是其他单词的一部分。文本字母大小写无关紧要。
单词是小写的，不要重复。如果一个单词在文本中出现几次，它应该是
只计算一次。

例如，text -“aresjfhdskfhskd如何?”，单词-(“how”，“are”，“you”，“hello”)。结果是3。

输入:两个参数。文本作为字符串(py2的unicode)和单词的一组字符串(py2的unicode)。

输出:文本中单词的数量作为一个整数。

如何使用:Python是用于文本处理的一种有用而强大的语言。这个任务只是一个简单的任务
您可以构建的文本搜索工具的示例。
"""

def count_words(text, words):
    return sum(x in text.lower() for x in words)
    


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert count_words("How aresjfhdskfhskd you?", {"how", "are", "you", "hello"}) == 3, "Example"
    assert count_words("Bananas, give me bananas!!!", {"banana", "bananas"}) == 2, "BANANAS!"
    assert count_words("Lorem ipsum dolor sit amet, consectetuer adipiscing elit.",
                       {"sum", "hamlet", "infinity", "anything"}) == 1, "Weird text"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")