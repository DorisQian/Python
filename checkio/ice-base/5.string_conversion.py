'''
- Oh. This new generation of robots is trying to do everything faster than is needed.

- Come on!! Gaffer! Can I just replace a string and that's all.

- No, young man. You can’t “just replace a string”. You should respect your memory cards, even though you have a lot of them. Now sit and think a little bit. How can this string can be replaced in a most efficient way?

- Ok ok. As you wish. Now I should respect even my own hardware.

You are given two strings, line1 and line2. Answer, what is the smallest number of operations you need to transform line1 to line2?

Operations are:

Delete one letter from one of strings
Insert one letter into one of strings
Replace one of letters from one of strings with another letter


Input: two arguments, two strings.

Output: int, minimum number of operations.

Example:

steps_to_convert('line1', 'line1') == 0
steps_to_convert('line1', 'line2') == 1
steps_to_convert('ine', 'line2') == 2

Precondition: 0 <= len(line) < 100

- 哦。 这个新一代的机器人正在试图把所有的事情都做得比所需要的快。

- 来吧！！ 领班！ 我可以只更换一个字符串，这一切。

- 不，年轻人 你不能“只是替换一个字符串”。 你应该尊重你的记忆卡，即使你有很多。 现在坐下来思考一下。 如何以最有效的方式替换这个字符串？

- 好的好的。 如你所愿。 现在我应该尊重我自己的硬件。

给你两个字符串，line1和line2。 答案，将line1转换为line2所需的最小操作数是多少？

操作是：

从一个字符串中删除一个字母
将一个字母插入一个字符串中
用另一个字母替换字符串中的一个字母


输入：两个参数，两个字符串。
输出：int，最小操作数。
'''

def steps_to_convert(line1, line2):
    return 0


if __name__ == "__main__":
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert steps_to_convert('line1', 'line1') == 0, "eq"
    assert steps_to_convert('line1', 'line2') == 1, "2"
    assert steps_to_convert('line', 'line2') == 1, "none to 2"
    assert steps_to_convert('ine', 'line2') == 2, "need two more"
    assert steps_to_convert('line1', '1enil') == 4, "everything is opposite"
    assert steps_to_convert('', '') == 0, "two empty"
    assert steps_to_convert('l', '') == 1, "one side"
    assert steps_to_convert('', 'l') == 1, "another side"
    print("You are good to go!")