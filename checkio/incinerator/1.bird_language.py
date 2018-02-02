'''
Stephan has a friend who happens to be a little mechbird. Recently, he was trying to 
teach it how to speak basic language. Today the bird spoke its first word: "hieeelalaooo". 
This sounds a lot like "hello", but with too many vowels. Stephan asked Nikola for 
help and he helped to examine how the bird changes words. With the information they 
discovered, we should help them to make a translation module.

The bird converts words by two rules:
- after each consonant letter the bird appends a random vowel letter (l ⇒ la or le);
- after each vowel letter the bird appends two of the same letter (a ⇒ aaa);
Vowels letters == "aeiouy".

You are given an ornithological phrase as several words which are separated by 
white-spaces (each pair of words by one whitespace). The bird does not know how to 
punctuate its phrases and only speaks words as letters. All words are given in 
lowercase. You should translate this phrase from the bird language to something more understandable.

Input: A bird phrase as a string.

Output: The translation as a string.

Example:

translate("hieeelalaooo") == "hello"
translate("hoooowe yyyooouuu duoooiiine") == "how you doin"
translate("aaa bo cy da eee fe") == "a b c d e f"
translate("sooooso aaaaaaaaa") == "sos aaa"
    
How it is used: This a similar cipher to those used by children when they invent 
their own "bird" language. Now you will be ready to crack the code.

Precondition: re.match("\A([a-z]+\ ?)+(?<!\ )\Z", phrase)
A phrase always has the translation.

斯蒂芬有一个朋友，他恰好是一只小小的小鸟。最近，他正在努力
教它如何说基本的语言。今天，这只鸟说出了第一个字：“hieeelalaooo”。
这听起来很像“你好”，但元音太多了。斯蒂芬问尼古拉
帮助他帮助检查鸟儿如何改变话语。随着他们的信息
发现了，我们应该帮助他们做一个翻译模块。

这只鸟用两条规则来转换文字：
- 在每个辅音字母之后，鸟附加一个随机元音字母（l？la或le）;
- 在每个元音字母后附加两个相同的字母（a⇒aaa）;
元音字母==“aeiouy”。

你被赋予了一个鸟类词汇作为被分隔的几个词
白色空格（每一对单词由一个空格）。这只鸟不知道如何
打断它的短语，只说字母。所有的单词都在
小写。你应该把这个短语从鸟语翻译成更容易理解的东西。

输入：一个鸟的短语作为一个字符串。
输出：作为字符串的翻译。

它是如何使用的：这与孩子们在创造时使用的密码相似
他们自己的“鸟”语言。 现在你将准备好破解代码。
'''

VOWELS = "aeiouy"

def translate(phrase):
    return phrase

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert translate("hieeelalaooo") == "hello", "Hi!"
    assert translate("hoooowe yyyooouuu duoooiiine") == "how you doin", "Joey?"
    assert translate("aaa bo cy da eee fe") == "a b c d e f", "Alphabet"
    assert translate("sooooso aaaaaaaaa") == "sos aaa", "Mayday, mayday"