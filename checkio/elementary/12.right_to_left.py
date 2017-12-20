"""
One of the robots is charged with a simple task: to join a sequence of strings into one sentence to produce instructions on how to get around the ship. But this robot is left-handed and has a tendency to joke around and confuse its right-handed friends.

You are given a sequence of strings. You should join these strings into chunk of text where the initial strings are separated by commas. As a joke on the right handed robots, you should replace all cases of the words "right" with the word "left", even if it's a part of another word. All strings are given in lowercase.

Input: A sequence of strings as a tuple of strings (unicode).

Output: The text as a string.

Example:

left_join(("left", "right", "left", "stop")) == "left,left,left,stop"
left_join(("bright aright", "ok")) == "bleft aleft,ok"
left_join(("brightness wright",)) == "bleftness wleft"
left_join(("enough", "jokes")) == "enough,jokes"

How it is used: This is a simple example of operations using strings and sequences.

Precondition:
0 < len(phrases) < 42

其中一个机器人负责一个简单的任务：将一系列的字符串合并成一个句子来产生如何绕过船的指示。但是这个机器人是左撇子，并且倾向于开玩笑和混淆右撇子的朋友。

给你一串字符串。您应该将这些字符串连接到初始字符串用逗号分隔的文本块中。作为对右手机器人的一个笑话，你应该用“左”这个词来代替“right”的所有情况，即使它是另一个词的一部分。所有字符串都以小写字母给出。

输入：字符串序列作为字符串的元组（unicode）。

输出：文本为字符串。

它是如何使用的： 这是使用字符串和序列的简单操作示例。

def left_join(phrases):
    """
        Join strings and replace "right" to "left"
    """
    return "left"

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert left_join(("left", "right", "left", "stop")) == "left,left,left,stop", "All to left"
    assert left_join(("bright aright", "ok")) == "bleft aleft,ok", "Bright Left"
    assert left_join(("brightness wright",)) == "bleftness wleft", "One phrase"
    assert left_join(("enough", "jokes")) == "enough,jokes", "Nothing to replace"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")

"""

def left_join(phrases):
    """
        Join strings and replace "right" to "left"
    """
    return "left"

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert left_join(("left", "right", "left", "stop")) == "left,left,left,stop", "All to left"
    assert left_join(("bright aright", "ok")) == "bleft aleft,ok", "Bright Left"
    assert left_join(("brightness wright",)) == "bleftness wleft", "One phrase"
    assert left_join(("enough", "jokes")) == "enough,jokes", "Nothing to replace"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
