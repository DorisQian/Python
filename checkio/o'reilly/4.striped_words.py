"""
Our robots are always working to improve their linguistic skills. For this mission, they research the latin alphabet and its applications.

The alphabet contains both vowel and consonant letters (yes, we divide the letters).
Vowels -- A E I O U Y
Consonants -- B C D F G H J K L M N P Q R S T V W X Z

You are given a block of text with different words. These words are separated by white-spaces and punctuation marks. Numbers are not considered words in this mission (a mix of letters and digits is not a word either). You should count the number of words (striped words) where the vowels with consonants are alternating, that is; words that you count cannot have two consecutive vowels or consonants. The words consisting of a single letter are not striped -- do not count those. Casing is not significant for this mission.

Input: A text as a string (unicode)

Output: A quantity of striped words as an integer.

Example:

checkio("My name is ...") == 3
checkio("Hello world") == 0
checkio("A quantity of striped words.") == 1, "Only of"
checkio("Dog,cat,mouse,bird.Human.") == 3

How it is used: This idea in this task is a useful exercise for linguistic research and analysis. Text processing is one of the main tools used in the analysis of various books and languages and can help translate print text to a digital format.

Precondition:The text contains only ASCII symbols.
0 < len(text) < 105

我们的机器人总是努力提高他们的语言技能。为了这个使命，他们研究拉丁字母和它的应用。
字母表中包含元音和辅音字母(是的，我们分字母)。
元音——E I O U Y
辅音——bcdf G H J K L M N P Q R S T V W X Z
你被赋予了一段文字的不同文字。这些单词由空格和标点符号隔开。在这个任务中，数字不被认为是单词(字母和数字的组合也不是一个单词)。你应该计算单词的数量(有条纹的单词)和辅音的元音是交替的，也就是;你计算的单词不能有两个连续的元音或辅音。由单个字母组成的单词没有条纹——不要数它们。外壳对这个任务不重要。

输入:作为字符串的文本(unicode)
输出:作为整数的条纹字的数量。

如何使用:这个任务中的这个想法是语言学研究和分析的有用的练习。文本处理是分析各种书籍和语言的主要工具之一，可以帮助将打印文本转换成数字格式。
"""
VOWELS = "AEIOUY"
CONSONANTS = "BCDFGHJKLMNPQRSTVWXZ"


def checkio(text):

    return 0

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio("My name is ...") == 3, "All words are striped"
    assert checkio("Hello world") == 0, "No one"
    assert checkio("A quantity of striped words.") == 1, "Only of"
    assert checkio("Dog,cat,mouse,bird.Human.") == 3, "Dog, cat and human"