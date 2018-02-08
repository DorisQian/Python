'''
The Robots have found an encrypted message. We cannot decrypt it at the moment, but we can take the first steps towards doing so. You have a set of "words", all in lower case, and each word contains symbols in "alphabetical order". (it's not your typical alphabetical order, but a new and different order.) We need to determine the order of the symbols from each "word" and create a single "word" with all of these symbols, placing them in the new alphabetial order. In some cases, if we cannot determine the order for several symbols, you should use the traditional latin alphabetical order. For example: Given words "acb", "bd", "zwa". As we can see "z" and "w" must be before "a" and "d" after "b". So the result is "zwacbd".

Input: Words as a list of strings.

Output: The order as a string.

Example:

checkio(["acb", "bd", "zwa"]) == "zwacbd"
checkio(["klm", "kadl", "lsm"]) == "kadlsm"
checkio(["a", "b", "c"]) == "abc"
checkio(["aazzss"]) == "azs"
checkio(["dfg", "frt", "tyg"]) == "dfrtyg"

How it is used: This concept can be useful for the cryptology, helping you to find regularities and patterns in natural text and ciphered messages.

Precondition: For each test, there can be the only one solution.
0 < |words| < 10


机器人发现了一条加密的消息。目前我们不能解密，但是我们可以采取第一步来做到这一点。你有一组“单词”，全部用小写字母表示，每个单词包含“按字母顺序排列”的符号。 （这不是你典型的字母顺序，而是一个新的和不同的顺序）。我们需要确定每个“单词”中符号的顺序，并用所有这些符号创建一个“单词”，并将它们置于新的字母顺序。在某些情况下，如果我们无法确定几个符号的顺序，则应使用传统的拉丁字母顺序。例如：给出单词“acb”，“bd”，“zwa”。我们可以看到“z”和“w”必须在“b”之前的“a”和“d”之前。所以结果是“zwacbd”。

输入：字作为字符串列表。
输出：作为字符串的顺序。

它是如何使用的：这个概念对于密码学是有用的，帮助你找到自然文本和加密信息的规律和模式。

先决条件：对于每个测试，只能有一个解决方案。
'''


def checkio(data):
    return ""

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(["acb", "bd", "zwa"]) == "zwacbd", \
        "Just concatenate it"
    assert checkio(["klm", "kadl", "lsm"]) == "kadlsm", \
        "Paste in"
    assert checkio(["a", "b", "c"]) == "abc", \
        "Cant determine the order - use english alphabet"
    assert checkio(["aazzss"]) == "azs", \
        "Each symbol only once"
    assert checkio(["dfg", "frt", "tyg"]) == "dfrtyg", \
        "Concatenate and paste in"