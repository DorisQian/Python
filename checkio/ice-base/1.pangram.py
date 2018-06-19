'''
A pangram (Greek:παν γράμμα, pan gramma, "every letter") or holoalphabetic 
sentence for a given alphabet is a sentence using every letter of the alphabet 
at least once. Perhaps you are familiar with the well known pangram "The quick 
brown fox jumps over the lazy dog".

For this mission, we will use the latin alphabet (A-Z). You are given a text with 
latin letters and punctuation symbols. You need to check if the sentence is a pangram 
or not. Case does not matter.

Input: A text as a string.

Output: Whether the sentence is a pangram or not as a boolean.

Example:

check_pangram("The quick brown fox jumps over the lazy dog.") == True
check_pangram("ABCDEF.") == False

How it is used: Pangrams have been used to display typefaces, test equipment, and develop 
skills in handwriting, calligraphy, and keyboarding for ages.

Precondition:

all(ch in (string.punctuation + string.ascii_letters + " ") for ch in text)
0 < len(text)

一个希腊语（希腊语：πανγράμμα，泛文法，“每个字母”）或全汉字
给定字母表的句子是使用字母表中的每个字母的句子至少一次。 也许你熟悉着名的“快速”
棕色的狐狸跳过懒惰的狗“。

为了这个任务，我们将使用拉丁字母（A-Z）。 给你一个文本
拉丁文字母和标点符号。 你需要检查句子是否是一个庞然大物或不。 情况并不重要。

输入：文本为字符串。
输出：句子是否是一个布尔值。

如何使用：Pangrams已被用于显示字体，测试设备和开发手写技巧，书法和键盘技术。
'''


def check_pangram(text):
    alpha_list = [i.lower() for i in text if i.isalpha()]
    alpha_text = ''.join(alpha_list)
    alpha = set(alpha_text)
    if len(alpha) == 26:
        return True
    else:
        return False
if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert check_pangram("The quick brown fox jumps over the lazy dog."), "brown fox"
    assert not check_pangram("ABCDEF"), "ABC"
    assert check_pangram("Bored? Craving a pub quiz fix? Why, just come to the Royal Oak!"), "Bored?"
    print('If it is done - it is Done. Go Check is NOW!')