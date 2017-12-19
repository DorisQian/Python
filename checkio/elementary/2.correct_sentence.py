"""
For the input of your function will be given one sentence. You have to return its fixed copy in a way so it’s always starts with a capital letter and ends with a dot.

Pay attention to the fact that not all of the fixes is necessary. If a sentence already ends with a dot then adding another one will be a mistake.

Input: A string.

Output: A string.
Example:
correct_sentence("greetings, friends") == "Greetings, friends."
correct_sentence("Greetings, friends") == "Greetings, friends."
correct_sentence("Greetings, friends.") == "Greetings, friends."

对于你的功能的输入将被给予一个句子。您必须以某种方式返回其固定副本，以便始终以大写字母开始，并以点结束。

注意并不是所有的修复都是必须的。如果一个句子已经以一个点结尾，那么添加另一个就是一个错误。

先决条件： 没有前导和尾随空格，文本只包含空格，a-z A-Z和. 
No leading and trailing spaces, text contains only spaces, a-z A-Z , and .
"""


def correct_sentence(text: str) -> str:
    """
        returns a corrected sentence which starts with a capital letter
        and ends with a dot.
    """
    if text[-1] != '.':
        text += '.'
    text = text[0].upper() + text[1:]
    return text

if __name__ == '__main__':
    print(correct_sentence("hi"))
    print(correct_sentence("greetings, friends"))
    print(correct_sentence("Greetings, friends"))
    print(correct_sentence("Greetings, friends."))
    # These "asserts" are used for self-checking and not for an auto-testing
    assert correct_sentence("greetings, friends") == "Greetings, friends."
    assert correct_sentence("Greetings, friends") == "Greetings, friends."
    assert correct_sentence("Greetings, friends.") == "Greetings, friends."
    assert correct_sentence("hi") == "Hi."

